
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="polymarket",  
    version="0.1.2",
    description="A package to export historical odds for an outcome of a market on Polymarket",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Matt Maximo",
    author_email="matt@pioneerdigital.org",
    url="https://github.com/MattMaximo/polymarket-py",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        "pytz"

    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["polymarket", "crypto", "data", "api", "exporter", "market", "odds"],
    python_requires='>=3.6',
)
