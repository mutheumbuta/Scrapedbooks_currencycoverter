import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime


# clean_currency: removes non-numeric characters and converts to float

def clean_currency(value):
    try:
        cleaned = re.sub(r"[^\d.]", "", value)
        return float(cleaned) if cleaned else None
    except ValueError:
        return None



# safe requests http: manages errors and timeouts gracefully
def safe_get(url, name):
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 403:
            print(f"{name} ERROR 403 Forbidden (API blocked or invalid key)")
            return None

        if response.status_code != 200:
            print(f"{name} ERROR {response.status_code}")
            return None

        return response

    except requests.exceptions.RequestException as e:
        print(f"{name} Network Error:", e)
        return None

# excgange rate: fetches current USD to KES rate, with fallback if API fails

def get_exchange_rate(api_key, base="USD", target="KES"):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base}"

    response = safe_get(url, "Currency API")

    # fixes fallback system when API fails (403 or network issues)
    if not response:
        print("Using fallback exchange rate (130 KES per USD)")
        return 130.0

    try:
        data = response.json()

        if "conversion_rates" not in data:
            print("Invalid API response → using fallback rate")
            return 130.0

        return data["conversion_rates"].get(target, 130.0)

    except Exception:
        print("JSON parsing error → using fallback rate")
        return 130.0



# scrape the products: gets title and price, cleans price, and returns list of dicts

def scrape_products(url, limit=10):
    products = []

    response = safe_get(url, "Website")
    if not response:
        return products

    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("article", class_="product_pod")[:limit]

    for item in items:
        title = item.h3.a["title"]
        price_text = item.find("p", class_="price_color").text

        price = clean_currency(price_text)

        if price is None:
            continue

        products.append({
            "title": title,
            "price_gbp": price
        })

    return products


# convert currency: adds USD and KES prices to each product dict, with timestamp

def convert_currency(data, rate):
    for item in data:
        usd = item["price_gbp"] * 1.25
        item["price_usd"] = round(usd, 2)
        item["price_kes"] = round(usd * rate, 2)
        item["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return data



# save data: saves list of dicts to CSV file and prints the DataFrame

def save_data(data, filename="final_prices.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print("\nSaved successfully:", filename)
    print(df)



# MAIN FUNCTION: orchestrates the scraping, conversion, and saving process

def main():
    API_KEY = "YOUR_API_KEY"
    URL = "https://books.toscrape.com/"

    print("Starting scraper...\n")

    rate = get_exchange_rate(API_KEY)
    products = scrape_products(URL)

    if products:
        converted = convert_currency(products, rate)
        save_data(converted)
    else:
        print("No products scraped")


if __name__ == "__main__":
    main()
