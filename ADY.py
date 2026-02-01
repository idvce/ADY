import requests

url = 'https://xe.chotot.com/mua-ban-oto-da-nang'
response = requests.get(url)
html_content = response.text

import requests
from bs4 import BeautifulSoup

def fetch_web_data(url):
    try:
        # Gửi yêu cầu HTTP GET
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Báo lỗi nếu HTTP status != 200

        # Phân tích HTML bằng BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ví dụ: Lấy tiêu đề trang
        title = soup.title.string if soup.title else "Không có tiêu đề"

        # Ví dụ: Lấy tất cả liên kết <a>
        links = [a['href'] for a in soup.find_all('a', href=True)]

        return {
            "title": title,
            "links": links
        }

    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi kết nối: {e}")
        return None

# --- Chạy thử ---
if __name__ == "__main__":
    url = "https://xe.chotot.com/mua-ban-oto-da-nang"  # Thay bằng URL bạn muốn lấy dữ liệu
    data = fetch_web_data(url)

    if data:
        print("Tiêu đề trang:", data["title"])
        print("Các liên kết tìm thấy:")
        for link in data["links"]:
            print("-", link)

