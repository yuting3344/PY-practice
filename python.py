import requests
import psycopg2


# 定義函數以獲取地點詳細資訊
def get_place_details(place_id, api_key):
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": place_id,
        "fields": "name,latitude, longitude,address,phone,rating,url",
        "key": api_key,
        "language": "zh-TW",
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["result"] if data.get("status") == "OK" else None


# API 金鑰
api_key = "AIzaSyCZzfaT30wnP7RD1eUtvA1U3K-fCLn4O4w"  # Google Places API 金鑰

# 連接到 PostgreSQL 資料庫
conn = psycopg2.connect(
    dbname="TripWay",  # 更改為您的資料庫名稱
    user="yuting",  # 更改為您的使用者名稱
    password="",  # 更改為您的密碼
    host="localhost",  # 更改為您的主機
    port="5432",  # 更改為您的連接埠
)
cur = conn.cursor()

# # 創建地點表，包含所需的欄位
# cur.execute(
#     """
#     CREATE TABLE IF NOT EXISTS places (
#         name TEXT,
#         address TEXT,
#         latitude FLOAT,
#         longitude FLOAT,
#         rating FLOAT,
#         phone TEXT,
#         website TEXT
#     )
# """
# )

# 請求 URL
url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

# 準備請求參數
query = "熱門景點"  # 查詢關鍵字（根據需要更改）
parameters = {
    "query": query,
    "language": "zh-TW",
    "key": api_key,
}

# 發送 GET 請求
response = requests.get(url, params=parameters)

# 處理響應數據
if response.status_code == 200:
    data = response.json()

    if data.get("status") == "OK":
        for place in data["results"]:
            place_id = place["place_id"]
            place_details = get_place_details(place_id, api_key)
            if place_details:
                # 將資料插入地點表
                cur.execute(
                    """
                    INSERT INTO spots_spot (name, latitude, longitude,address, phone, rating, url)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                    (
                        place_details.get("name"),
                        place_details.get("formatted_address"),
                        place_details["geometry"]["location"]["lat"],
                        place_details["geometry"]["location"]["lng"],
                        place_details.get("rating"),
                        place_details.get("formatted_phone_number", "N/A"),
                        place_details.get("url", "N/A"),
                    ),
                )

# 提交更改並關閉連接
conn.commit()
conn.close()
