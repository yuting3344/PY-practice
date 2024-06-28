# import requests


# def get_place_details(place_id, api_key):
#     url = "https://maps.googleapis.com/maps/api/place/details/json"
#     params = {
#         "place_id": place_id,
#         "fields": "name,formatted_address,formatted_phone_number,geometry,rating,website",
#         "key": api_key,
#     }
#     response = requests.get(url, params=params)
#     data = response.json()
#     return data["result"] if data.get("status") == "OK" else None


# def search_places(query, api_key):
#     url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
#     params = {"query": query, "key": api_key}
#     response = requests.get(url, params=params)
#     data = response.json()
#     return data["results"] if data.get("status") == "OK" else []


# def main():
#     # 在這裡填入你的 Google Maps API 金鑰
#     api_key = "AIzaSyCZzfaT30wnP7RD1eUtvA1U3K-fCLn4O4w"

#     # 要搜索的景點關鍵字
#     query = "熱門景點"

#     # 搜索景點
#     places = search_places(query, api_key)

#     # 爬取每個景點的詳細資訊並打印
#     for place in places:
#         place_id = place["place_id"]
#         details = get_place_details(place_id, api_key)
#         if details:
#             print("名稱:", details.get("name", "N/A"))
#             print("地址:", details.get("formatted_address", "N/A"))
#             print("電話號碼:", details.get("formatted_phone_number", "N/A"))
#             print("經度:", details["geometry"]["location"]["lat"])
#             print("緯度:", details["geometry"]["location"]["lng"])
#             print("評分:", details.get("rating", "N/A"))
#             print("網址:", details.get("website", "N/A"))
#             print("-" * 50)


# if __name__ == "__main__":
#     main()
import requests


def search_places(query, api_key):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "language": "zh-TW",
        "key": api_key,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["results"] if data.get("status") == "OK" else []


def get_place_details(place_id, api_key):
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": place_id,
        "fields": "name,formatted_address,formatted_phone_number,geometry,rating,website,opening_hours",
        "key": api_key,
    }
    response = requests.get(url, params=params)
    data = response.json()
    result = data["result"] if data.get("status") == "OK" else None
    if result and "formatted_address" in result:
        formatted_address = result["formatted_address"]
        # 檢查地址是否包含中文字符，如果是，則優先使用中文地址
        if any(char >= "\u4e00" and char <= "\u9fff" for char in formatted_address):
            result["formatted_address"] = formatted_address
    if result and "name" in result:
        name = result["name"]
        # 檢查名稱是否包含中文字符，如果是，則優先使用中文名稱
        if any(char >= "\u4e00" and char <= "\u9fff" for char in name):
            result["name"] = name
    return result


def get_district_or_city(details):
    address = details.get("formatted_address", "")
    parts = address.split(",")
    for part in parts:
        if "district" in part.lower():  # 如果地址中包含 "district" 字樣
            return part.strip()
    return "N/A"


def get_day_name(day):
    days = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    return days[day]


def main():
    # 在這裡填入你的 Google Maps API 金鑰
    api_key = "AIzaSyCZzfaT30wnP7RD1eUtvA1U3K-fCLn4O4w"

    # 要搜索的景點關鍵字
    query = "熱門景點"

    # 搜索景點
    places = search_places(query, api_key)

    # 爬取每個景點的詳細信息並打印
    for place in places:
        place_id = place["place_id"]
        # print(place)
        details = get_place_details(place_id, api_key)
        if details:
            print("名稱:", details.get("name", "N/A"))
            print("地址:", details.get("formatted_address", "N/A"))
            district_or_city = get_district_or_city(details)
            print("區或城市:", district_or_city)
            print("電話號碼:", details.get("formatted_phone_number", "N/A"))
            print("經度:", details["geometry"]["location"]["lat"])
            print("緯度:", details["geometry"]["location"]["lng"])
            print("評分:", details.get("rating", "N/A"))
            print("網址:", details.get("website", "N/A"))
            opening_hours = details.get("opening_hours", {})
            if opening_hours:
                print("營業時間:")
                for period in opening_hours.get("periods", []):
                    open_time = period.get("open", {}).get("time", "N/A")
                    close_time = period.get("close", {}).get("time", "N/A")
                    day_name = get_day_name(period["open"]["day"])
                    formatted_open_time = f"{open_time[:-2]}:{open_time[-2:]}"
                    formatted_close_time = f"{close_time[:-2]}:{close_time[-2:]}"
                    print(
                        f"  {day_name}: {formatted_open_time} - {formatted_close_time}"
                    )
            else:
                print("營業時間: N/A")
            print("-" * 50)


if __name__ == "__main__":
    main()
