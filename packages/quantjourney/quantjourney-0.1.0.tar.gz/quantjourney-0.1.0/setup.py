from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="quantjourney",
    version="0.1.0",
    author="QuantJourney",
    author_email="jakub@quantjourney.pro",
    description="A client library for the QuantJourney API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QuantJourneyOrg/quantjourney",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
        "pandas",
        "python-jose[cryptography]",
        "pydantic[email]",
        "passlib==1.7.4",
        "python-dotenv",
        "aiohttp"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
)