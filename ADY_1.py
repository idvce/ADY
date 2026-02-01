
import requests
from bs4 import BeautifulSoup
import  pandas as pd
import time
from datetime import datetime

HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_page(url, vehicle_type):
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    rows = []
    # adjust selector to the actual listing wrapper on the site
    for card in soup.select("a.AdItem_wrapper__item"):
        title_tag = card.select_one("h3")
        price_tag = (card.select_one("span.AdItem_price__value")
                     or card.find("span", string=lambda t: t and "đ" in t))

        title = title_tag.get_text(strip=True) if title_tag else "N/A"
        price = price_tag.get_text(strip=True) if price_tag else "N/A"
        link  = card.get("href", "")

        rows.append({
            "vehicle_type": vehicle_type,
            "title": title,
            "price_text": price,
            "url": "https://xe.chotot.com" + link,
            "scraped_date": datetime.now().strftime("%Y-%m-%d")
        })
    return rows

def crawl_danang(pages=3):
    all_rows = []

    # cars
    for p in range(1, pages+1):
        url = f"https://xe.chotot.com/mua-ban-oto-da-nang?page={p}"
        all_rows += scrape_page(url, "car")
        time.sleep(2)

    # motorcycles
    for p in range(1, pages+1):
        url = f"https://xe.chotot.com/mua-ban-xe-may-da-nang?page={p}"
        all_rows += scrape_page(url, "motorcycle")
        time.sleep(2)

    df = pd.DataFrame(all_rows)
    df.to_csv("danang_used_vehicles_raw.csv", index=False, encoding="utf-8")
    return df

df_raw = crawl_danang(pages=3)
print(df_raw.head())
