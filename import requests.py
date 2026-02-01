import requests
import time

def get_car_data(page):
    url = f"https://xe.chotot.com/mua-ban-oto-da-nang={page}"
    headers = {"User-Agent": "Mozilla/5.0..."}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data'] # Giả sử dữ liệu nằm trong key 'data'
    return []

max_pages = 50
all_cars = []
for p in range(1, max_pages+1):
    print(f"Đang lấy dữ liệu trang {p}...")
    all_cars.extend(get_car_data(p))
    time.sleep(2) # Nghỉ 2 giây để tránh bị chặn (Anti-spam)