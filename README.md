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
## How It Works
1 Sends request to e-commerce website

2 Extracts product titles + prices

3 Cleans currency using regex

4 Fetches live exchange rate from API

5 Handles API failures (403 fallback system)

6 Converts prices into multiple currencies

7 Saves structured dataset to CSV

## Installation & Usage
1. Clone repository
```bash
git clone https://github.com/mutheumbuta/Scrapedbooks_currencycoverter.git
cd pricesrappe_currencyconverter
```
3. Install dependencies
```bash
pip install requests beautifulsoup4 pandas
```
5. Add API key

Replace in script:
```python
API_KEY = "YOUR_API_KEY"
```
4. Run script
```python
python scraped_books.py
```
## Error Handling & Reliability

This project includes production-grade safeguards:

1.  Handles 403 Forbidden API errors
   
2.  Handles network failures
  
3.  Handles invalid currency formats
  
4.  Prevents script crashes with fallback values
  
5.  Validates HTTP responses before processing

##  Business Use Cases

This system can be used for: 

- E-commerce price monitoring
  
- Competitor price tracking
  
- Financial data aggregation
  
- Market analysis dashboards
  
- Currency-based pricing systems
  
## Future Improvements
-  Deploy as FastAPI service
  
- Build Streamlit dashboard
  
- Docker
  
- Database integration (PostgreSQL)
  
-  Multi-site scraping engine
  
## 📜 License

This project is licensed under the MIT License.

## Author

Nancy Mutheu Mbuta

email:mutheumbuta@gmail.com

Github: mutheumbuta


