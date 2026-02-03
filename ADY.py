import requests

url = 'https://xe.chotot.com/mua-ban-oto-da-nang'
response = requests.get(url)
html_content = response.text

import requests
from bs4 import BeautifulSoup

def fetch_web_data(url):
    try:
        # send request HTTP GET
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Report an error if HTTP status != 200

        # HTML parsing using Beautifulsoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # example for take title
        title = soup.title.string if soup.title else "Không có tiêu đề"

        # examp for get all links
        links = [a['href'] for a in soup.find_all('a', href=True)]

        return {
            "title": title,
            "links": links
        }

    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi kết nối: {e}")
        return None

if __name__ == "__main__":
    url = "https://xe.chotot.com/mua-ban-oto-da-nang"  #replace with URL if you wait to get data
    data = fetch_web_data(url)

    if data:
        print("Tiêu đề trang:", data["title"])
        print("Các liên kết tìm thấy:")
        for link in data["links"]:
            print("-", link)


