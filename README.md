# Scrapedbooks_currencycoverter
A production-ready web scraping and currency conversion tool built with Python that extracts product prices from an e-commerce site, cleans messy data, converts 

currencies using live exchange rates, and exports structured datasets for analysis.

## Project Overview

This project demonstrates real-world data engineering and automation skills by combining:

- Web scraping (BeautifulSoup)

- API integration (currency exchange rates)

- Data cleaning (regex-based currency parsing)

- Error handling for production reliability

- Data export for analytics workflows

## Key Features

- Scrapes product data from Books to Scrape

- Cleans messy currency strings (£51.77 → 51.77)
  
- Converts prices using live USD → KES exchange rates
  
- Handles API failures (including 403 errors) gracefully
  
- Fallback system ensures scraper never breaks
  
- Adds timestamp for tracking price changes
  
- Exports clean data to CSV
  
- Fully modular function-based architecture
  
## Tech Stack
1 Python 3

2 Requests

3 BeautifulSoup4

4 Pandas

5 Regex (re module)

6 ExchangeRate API

## Project Structure
```
price-scraper/
│
├── scraper.py
├── final_prices.csv
└── README.md
```
