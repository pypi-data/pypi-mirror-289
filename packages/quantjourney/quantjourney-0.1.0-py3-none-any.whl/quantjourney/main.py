import aiohttp
import asyncio
from typing import Dict, Any, Optional, List
import pandas as pd

from dataclasses import dataclass, field
from typing import List, Union, Dict, Optional, Any, Tuple

from fastapi.background import P


# QuantJourneyClient --------------------------------------------------------
@dataclass
class QuantJourneyClient:
	"""
	Client to interact with the QuantJourney API

	"""
	base_url: str
	user_token: Optional[str] = None
	admin_token: Optional[str] = None

	def __post_init__(self):
		self.user_token = None
		self.admin_token = None

		if not self.base_url.startswith("http"):
			raise ValueError("base_url must be a valid URL")


	# Authentication --------------------------------------------------------

	async def async_login(	self,
							username: str,
							password: str) -> Dict[str, Any]:
		"""
		Async function to authenticate the user and get the access token
			- username: str: The username of the user
			- password: str: The password of the user
		"""
		url = f"{self.base_url}/auth/login"
		async with aiohttp.ClientSession() as session:
			async with session.post(url, data={"username": username, "password": password}) as response:
				if response.status == 200:
					data = await response.json()
					self.user_token = data["access_token"]
					return data
				else:
					error_text = await response.text()
					raise Exception(f"Authentication failed: Status {response.status}, Response: {error_text}")


	def get_token(	self,
					username: str,
					password: str) -> str:
		"""
		Wrapper function to run the async_login function synchronously
			- username: str: The username of the user
			- password: str: The password of the user
		"""
		try:
			auth_data = asyncio.run(self.async_login(username, password))
			return auth_data["access_token"]
		except Exception as e:
			print(f"Error during authentication: {str(e)}")
			return None


	# OHLCV ------------------------------------------------------------------

	async def async_get_ohlcv(	self,
								ticker: str,
								exchange: str = "US",
								source: str = "yf",
								granularity: str = "1d",
								period_start: str = "2021-01-01",
								period_end: str = "2021-12-31",
								read_db: bool = False,
								write_db: bool = False) -> Dict[str, Any]:
		"""
		Async function to fetch OHLCV data from the QuantJourney API
			- ticker: str: The ticker symbol of the equity
			- exchange: str: The exchange where the equity is listed
			- source: str: The data source to fetch the OHLCV data from
			- granularity: str: The granularity of the OHLCV data
			- period_start: str: The start date of the period to fetch the OHLCV data
			- period_end: str: The end date of the period to fetch the OHLCV data
			- read_db: bool: Whether to read the OHLCV data from the database
			- write_db: bool: Whether to write the OHLCV data to the
		"""
		url = f"{self.base_url}/ohlcv/{ticker}"
		params = {
			"exchange": exchange,
			"source": source,
			"granularity": granularity,
			"period_start": period_start,
			"period_end": period_end,
			"read_db": str(read_db).lower(),
			"write_db": str(write_db).lower()
		}
		headers = {"Authorization": f"Bearer {self.user_token or self.admin_token}"}

		async with aiohttp.ClientSession() as session:
			async with session.get(url, headers=headers, params=params) as response:
				if response.status == 200:
					response_data = await response.json()
					if response_data["success"]:
						ohlcv_dict = response_data["data"][0]

						df = pd.DataFrame(ohlcv_dict['data'])
						# Explicitly parse the date column
						df['date'] = pd.to_datetime(df['date'], format='ISO8601')

						# Set the date as index
						df.set_index('date', inplace=True)
						# Convert numeric columns to float
						numeric_columns = ['open', 'high', 'low', 'close', 'volume']
						df[numeric_columns] = df[numeric_columns].astype(float)

						# Add metadata as attributes
						df.attrs.update({
							key: ohlcv_dict[key]
							for key in ['ticker', 'exchange', 'source', 'granularity']
						})
						return df
					else:
						raise Exception(f"Failed to fetch OHLCV data: {response_data}")
				else:
					raise Exception(f"Failed to fetch OHLCV data: {await response.text()}")


	# Indicators -------------------------------------------------------------

	async def async_calculate_indicator(self,
										indicator_name: str,
										data: Dict[str, List[float]],
										params: Dict[str, Any]) -> Dict[str, Any]:
		"""
		Async function to calculate an indicator
		"""
		url = f"{self.base_url}/indicators/{indicator_name}"
		payload = {
			"data": data,
			"params": params
		}
		headers = {"Authorization": f"Bearer {self.user_token or self.admin_token}"}

		async with aiohttp.ClientSession() as session:
			async with session.post(url, headers=headers, json=payload) as response:
				if response.status == 200:
					return await response.json()
				else:
					raise Exception(f"Failed to calculate indicator: {await response.text()}")


	async def async_calculate_multiple_indicators(	self,
													data: Dict[str, List[float]],
													indicators: List[Dict[str, Any]]) -> Dict[str, Any]:
		"""
		Async function to calculate multiple indicators
		"""
		url = f"{self.base_url}/indicators/calculate"
		payload = {
			"data": data,
			"indicators": indicators
		}
		headers = {"Authorization": f"Bearer {self.user_token or self.admin_token}"}

		async with aiohttp.ClientSession() as session:
			async with session.post(url, headers=headers, json=payload) as response:
				if response.status == 200:
					return await response.json()
				else:
					raise Exception(f"Failed to calculate multiple indicators: {await response.text()}")


	def calculate_indicator(self,
							indicator_name: str,
							data: Dict[str, List[float]],
							params: Dict[str, Any]) -> Dict[str, Any]:
		"""
		Wrap the async_calculate_indicator function to run synchronously
		"""
		return asyncio.run(self.async_calculate_indicator(indicator_name, data, params))


	def calculate_multiple_indicators(	self,
										data: Dict[str, List[float]],
										indicators: List[Dict[str, Any]]) -> Dict[str, Any]:
		"""
		Wrap the async_calculate_multiple_indicators function to run synchronously
		"""
		return asyncio.run(self.async_calculate_multiple_indicators(data, indicators))


	# Fundamental Data --------------------------------------------------------

	async def async_get_fundamentals(	self,
										ticker: str,
										exchange: str) -> Dict[str, Any]:
		"""
		Async function to fetch fundamental data for an equity
		"""
		url = f"{self.base_url}/fundamental/{ticker}/general"
		params = {"exchange": exchange}
		headers = {"Authorization": f"Bearer {self.user_token or self.admin_token}"}

		async with aiohttp.ClientSession() as session:
			async with session.get(url, headers=headers, params=params) as response:
				if response.status == 200:
					return (await response.json())["data"]
				else:
					raise Exception(f"Failed to fetch fundamental data: {await response.text()}")


	async def async_get_fundamental_metrics(self,
											ticker: str,
											exchange: str,
											metrics: List[str]) -> Dict[str, Any]:
		"""
		Async function to fetch specific fundamental metrics for an equity
		"""
		url = f"{self.base_url}/fundamental/{ticker}/metrics"
		params = {"exchange": exchange, "metrics": metrics}
		headers = {"Authorization": f"Bearer {self.user_token or self.admin_token}"}

		async with aiohttp.ClientSession() as session:
			async with session.get(url, headers=headers, params=params) as response:
				if response.status == 200:
					return (await response.json())["data"]
				else:
					raise Exception(f"Failed to fetch fundamental metrics: {await response.text()}")


	async def async_get_income_statement(	self,
											ticker: str,
											exchange: str = "US",
											option: str = "q") -> Dict[str, Any]:
		"""
		Async function to fetch the income statement for an equity
		"""
		url = f"{self.base_url}/fundamental/{ticker}/income-statement"
		params = {"exchange": exchange, "option": option}
		headers = {"Authorization": f"Bearer {self.user_token or self.admin_token}"}

		async with aiohttp.ClientSession() as session:
			async with session.get(url, headers=headers, params=params) as response:
				if response.status == 200:
					return (await response.json())["data"]
				else:
					raise Exception(f"Failed to fetch income statement: {await response.text()}")


	async def async_get_income_statement_item(	self,
												ticker: str,
												exchange: str = "US",
												item: str = "totalRevenue",
												option: str = "q",
												period: Optional[str] = None) -> Dict[str, Any]:
		"""
		Async function to fetch a specific item from the income statement
		"""
		url = f"{self.base_url}/fundamental/{ticker}/income-statement/{item}"
		params = {"exchange": exchange, "option": option, "period": period}
		headers = {"Authorization": f"Bearer {self.user_token or self.admin_token}"}

		async with aiohttp.ClientSession() as session:
			async with session.get(url, headers=headers, params=params) as response:
				if response.status == 200:
					return (await response.json())["data"]
				else:
					raise Exception(f"Failed to fetch income statement item: {await response.text()}")


	async def async_get_cash_flow(	self,
									ticker: str,
									exchange: str = "US",
									option: str = "q") -> Dict[str, Any]:
		"""
		Async function to fetch the cash flow for an equity
		"""
		url = f"{self.base_url}/fundamental/{ticker}/cash-flow"
		params = {"exchange": exchange, "option": option}
		headers = {"Authorization": f"Bearer {self.user_token or self.admin_token}"}

		async with aiohttp.ClientSession() as session:
			async with session.get(url, headers=headers, params=params) as response:
				if response.status == 200:
					return (await response.json())["data"]
				else:
					raise Exception(f"Failed to fetch cash flow: {await response.text()}")


	async def async_get_cash_flow_item(	self,
											ticker: str,
											exchange: str = "US",
											item: str = "totalRevenue",
											option: str = "q",
											period: Optional[str] = None) -> Dict[str, Any]:
		"""
		Async function to fetch a specific item from the cash flow
		"""
		url = f"{self.base_url}/fundamental/{ticker}/cash-flow/{item}"
		params = {"exchange": exchange, "option": option, "period": period}
		headers = {"Authorization": f"Bearer {self.user_token or self.admin_token}"}

		async with aiohttp.ClientSession() as session:
			async with session.get(url, headers=headers, params=params) as response:
				if response.status == 200:
					return (await response.json())["data"]
				else:
					raise Exception(f"Failed to fetch cash flow item: {await response.text()}")


	async def async_balance_sheet(	self,
									ticker: str,
									exchange: str = "US",
									option: str = "q") -> Dict[str, Any]:
		"""
		Async function to fetch the balance sheet for an equity
		"""
		url = f"{self.base_url}/fundamental/{ticker}/balance-sheet"
		params = {"exchange": exchange, "option": option}
		headers = {"Authorization": f"Bearer {self.user_token or self.admin_token}"}

		async with aiohttp.ClientSession() as session:
			async with session.get(url, headers=headers, params=params) as response:
				if response.status == 200:
					return (await response.json())["data"]
				else:
					raise Exception(f"Failed to fetch balance sheet: {await response.text()}")


	async def async_get_balance_sheet_item(	self,
											ticker: str,
											exchange: str = "US",
											item: str = "totalRevenue",
											option: str = "q",
											period: Optional[str] = None) -> Dict[str, Any]:
		"""
		Async function to fetch a specific item from the balance sheet
		"""
		url = f"{self.base_url}/fundamental/{ticker}/balance-sheet/{item}"
		params = {"exchange": exchange, "option": option, "period": period}
		headers = {"Authorization": f"Bearer {self.user_token or self.admin_token}"}

		async with aiohttp.ClientSession() as session:
			async with session.get(url, headers=headers, params=params) as response:
				if response.status == 200:
					return (await response.json())["data"]
				else:
					raise Exception(f"Failed to fetch balance sheet item: {await response.text()}")


# QuantJourneyConnect --------------------------------------------------------
@dataclass
class QuantJourney:
	"""
	QuantJourneyConnect class to connect to the QuantJourney API

	Multiple classes are defined within this class to interact with different
		- Equities
		- EOD
		- YFinance

	"""
	username: str
	password: str
	base_url: str = "http://localhost:8000"
	client: QuantJourneyClient = field(init=False)
	equities: Optional['QuantJourney.Equities'] = field(init=False, default=None)
	fundamentals: Optional['QuantJourney.Fundamentals'] = field(init=False, default=None)

	def __post_init__(self):
		"""
		Connect to the QuantJourney API
		"""
		self.client = QuantJourneyClient(self.base_url)
		token = self.client.get_token(self.username, self.password)
		if token:
			self.client.user_token = token
			self.equities = self.Equities(self.client)
			self.fundamentals = self.Fundamentals(self.client)
		else:
			raise Exception("Failed to authenticate. Please check your credentials and server status.")

		#self.indices = self.Indices(self.client)

	# Equities ----------------------------------------------------------------
	@dataclass
	class Equities:
		"""
		Class to interact with the Equities API
		"""
		client: QuantJourneyClient


		def get_equity(	self,
						ticker: str,
						exchange: str = "US",
						source: str = "yf",
						granularity: str = "1d",
						period_start: str = "2021-01-01",
						period_end: str = "2021-12-31",
						read_db: bool = False,
						write_db: bool = False) -> pd.DataFrame:
			"""
			Get the OHLCV data for an equity
			"""
			return asyncio.run(self.client.async_get_ohlcv(	ticker,
															exchange=exchange,
															source=source,
															granularity=granularity,
															period_start=period_start,
															period_end=period_end,
															read_db=read_db,
															write_db=write_db
			))

	# Fundamentals ------------------------------------------------------------
	@dataclass
	class Fundamentals:
		"""
		Class to interact with the Fundamentals API
		"""
		client: QuantJourneyClient


		def get_general(self, ticker: str, exchange: str = "US") -> Dict[str, Any]:
			return asyncio.run(self.client.async_get_fundamentals(ticker, exchange))

		def get_metrics(self, ticker: str, exchange: str = "US", metrics: List[str] = None) -> Dict[str, Any]:
			if metrics is None:
				metrics = ["mcap", "pe", "peg"]  # Default metrics
			return asyncio.run(self.client.async_get_fundamental_metrics(ticker, exchange, metrics))

		def get_income_statement(self, ticker: str, exchange: str = "US", option: str = "q") -> pd.DataFrame:
			data = asyncio.run(self.client.async_get_income_statement(ticker, exchange, option))
			return pd.DataFrame(data)

		def get_income_statement_item(self, ticker: str, exchange: str = "US", item: str = "totalRevenue", option: str = "q", period: Optional[str] = None) -> Dict[str, Any]:
			return asyncio.run(self.client.async_get_income_statement_item(ticker, exchange, item, option, period))

		def get_cash_flow(self, ticker: str, exchange: str = "US", option: str = "q") -> pd.DataFrame:
			data = asyncio.run(self.client.async_get_cash_flow(ticker, exchange, option))
			return pd.DataFrame(data)

		def get_cash_flow_item(self, ticker: str, exchange: str = "US", item: str = "operatingCashFlow", option: str = "q", period: Optional[str] = None) -> Dict[str, Any]:
			return asyncio.run(self.client.async_get_cash_flow_item(ticker, exchange, item, option, period))

		def get_balance_sheet(self, ticker: str, exchange: str = "US", option: str = "q") -> pd.DataFrame:
			data = asyncio.run(self.client.async_balance_sheet(ticker, exchange, option))
			return pd.DataFrame(data)

		def get_balance_sheet_item(self, ticker: str, exchange: str = "US", item: str = "totalAssets", option: str = "q", period: Optional[str] = None) -> Dict[str, Any]:
			return asyncio.run(self.client.async_get_balance_sheet_item(ticker, exchange, item, option, period))

		def calculate_ratios(self, ticker: str, exchange: str = "US", option: str = "q") -> Dict[str, float]:
			income_statement = self.get_income_statement(ticker, exchange, option)
			balance_sheet = self.get_balance_sheet(ticker, exchange, option)
			cash_flow = self.get_cash_flow(ticker, exchange, option)

			latest_period = income_statement.index[0]

			total_revenue = income_statement.loc[latest_period, 'totalRevenue']
			net_income = income_statement.loc[latest_period, 'netIncome']
			total_assets = balance_sheet.loc[latest_period, 'totalAssets']
			total_equity = balance_sheet.loc[latest_period, 'totalStockholderEquity']
			operating_cash_flow = cash_flow.loc[latest_period, 'operatingCashFlow']

			ratios = {
				'net_profit_margin': net_income / total_revenue if total_revenue else None,
				'return_on_assets': net_income / total_assets if total_assets else None,
				'return_on_equity': net_income / total_equity if total_equity else None,
				'operating_cash_flow_ratio': operating_cash_flow / total_revenue if total_revenue else None,
			}

			return ratios


	# Indicators --------------------------------------------------------------
	@dataclass
	class Indicators:
		"""
		Class to interact with the Indicators API
		"""
		client: QuantJourneyClient

		def calculate(self, indicator_name: str, data: Dict[str, List[float]], params: Dict[str, Any]) -> Dict[str, Any]:
			return self.client.calculate_indicator(indicator_name, data, params)

		def calculate_multiple(self, data: Dict[str, List[float]], indicators: List[Dict[str, Any]]) -> Dict[str, Any]:
			return self.client.calculate_multiple_indicators(data, indicators)



	# EOD ---------------------------------------------------------------------
	@dataclass
	class EOD:
		"""
		Class to interact with the EOD API
		"""
		client: QuantJourneyClient

		# Add EOD-specific methods here


	# YFinance ----------------------------------------------------------------
	@dataclass
	class YF:
		"""
		Class to interact with the YFinance API
		"""
		client: QuantJourneyClient



if __name__ == "__main__":
	# user = "ania"
	# password = "Ania"
	user = "jakub"
	password =  "Pojecia1"
	from pprint import pprint
	#import QuantJourney

	qjc = QuantJourney(user, password)
	AAPL = qjc.equities.get_equity("AAPL")

	
	print(AAPL)
	exit()
	# AAPL = qjc.equities.get_equity("AAPL", period_start="2022-02-01", period_end="2023-12-31")
	# print(AAPL)

	# AAPL = qjc.equities.get_equity("AAPL", source="yf") #, source="eod")
	# print(AAPL)

	# Test OHLCV data
	# AAPL = qjc.equities.get_equity("AAPL", source="yf", period_start="2023-01-01", period_end="2023-12-31")
	# print("AAPL OHLCV Data:")
	# print(AAPL.head())
	# print("\n")

	# Test fundamental data
	AAPL_fundamentals = qjc.fundamentals.get_general("AAPL")
	print("AAPL General Fundamentals:")
	pprint(AAPL_fundamentals)
	print("\n")


	exit()
	# Test fundamental metrics
	AAPL_metrics = qjc.fundamentals.get_metrics("AAPL", metrics=["mcap", "pe", "peg", "div_yield"])
	print("AAPL Fundamental Metrics:")
	pprint(AAPL_metrics)
	print("\n")

	# Test income statement
	AAPL_income = qjc.fundamentals.get_income_statement("AAPL")
	print("AAPL Income Statement:")
	print(AAPL_income.head())
	print("\n")

	# Test balance sheet
	AAPL_balance = qjc.fundamentals.get_balance_sheet("AAPL")
	print("AAPL Balance Sheet:")
	print(AAPL_balance.head())
	print("\n")


	# Test cash flow
	AAPL_cash_flow = qjc.fundamentals.get_cash_flow("AAPL")
	print("AAPL Cash Flow:")
	print(AAPL_cash_flow.head())
	print("\n")


	exit()

	# Test specific items
	# AAPL_revenue = qjc.fundamentals.get_income_statement_item("AAPL", item="totalRevenue")
	print("AAPL Total Revenue:")
	# pprint(AAPL_revenue)
	print("\n")

	# Test financial ratios
	# AAPL_ratios = qjc.fundamentals.calculate_ratios("AAPL")
	print("AAPL Financial Ratios:")
	# pprint(AAPL_ratios)
	print("\n")

	# # Test multiple stocks
	# tickers = ["AAPL", "MSFT", "GOOGL"]
	# for ticker in tickers:
	# 	print(f"{ticker} Metrics and Ratios:")
	# 	metrics = qjc.fundamentals.get_metrics(ticker, metrics=["mcap", "pe", "peg"])
	# 	ratios = qjc.fundamentals.calculate_ratios(ticker)
	# 	pprint({**metrics, **ratios})
	# 	print("\n")

	# Test yearly data
	AAPL_yearly_income = qjc.fundamentals.get_income_statement("AAPL", option="y")
	print("AAPL Yearly Income Statement:")
	print(AAPL_yearly_income.head())
	print("\n")

	# Test specific period
	AAPL_q4_revenue = qjc.fundamentals.get_income_statement_item("AAPL", item="totalRevenue", period="2023-12-31")
	print("AAPL Q4 2023 Revenue:")
	pprint(AAPL_q4_revenue)
	print("\n")

	


	# from pprint import pprint
	# pprint(AAPL_metrics)
	# print("\n")
	# Calculate a single indicator
	# data = {
	#     "open": AAPL["open"].tolist(),
	#     "high": AAPL["high"].tolist(),
	#     "low": AAPL["low"].tolist(),
	#     "close": AAPL["close"].tolist(),
	#     "volume": AAPL["volume"].tolist()
	# }
	# params = {"period": 14}
	# result = qjc.indicators.calculate("SMA", data, params)
	# print(result)

	# # Calculate multiple indicators
	# indicators = [
	#     {"name": "SMA", "params": {"period": 14}},
	#     {"name": "EMA", "params": {"period": 14}}
	# ]
	# multiple_results = qjc.indicators.calculate_multiple(data, indicators)
	# print(multiple_results)