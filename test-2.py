# import requests
# import json

# # 定義URL
# url = "https://raw.githubusercontent.com/wazho/lawsnote-exam/main/inputs/%E4%B8%AD%E5%A4%AE%E6%B3%95%E8%A6%8F%E6%A8%99%E6%BA%96%E6%B3%95/93-05-19/%E7%AC%AC%20%E4%BA%94%20%E7%AB%A0%20%E6%B3%95%E8%A6%8F%E4%B9%8B%E4%BF%AE%E6%AD%A3%E8%88%87%E5%BB%A2%E6%AD%A2/%E7%AC%AC%2020%20%E6%A2%9D"

# # 發送GET請求
# response = requests.get(url)

# # 檢查請求是否成功
# if response.status_code == 200:
#     # 取得文本內容
#     text = response.text.strip()

#     # 按段落分割文本
#     paragraphs = text.split("\n")

#     # 構建JSON對象
#     json_obj = {"level": "項", "items": []}

#     # 初始化臨時變量來存儲條款
#     current_item = None
#     child_items = []

#     for paragraph in paragraphs:
#         paragraph = paragraph.strip()
#         if paragraph.startswith("法規有左列情形之一者，修正之："):
#             if current_item:
#                 current_item["child"] = {"level": "款", "items": child_items}
#                 json_obj["items"].append(current_item)
#             current_item = {"content": paragraph}
#             child_items = []
#         elif (
#             paragraph.startswith("一、")
#             or paragraph.startswith("二、")
#             or paragraph.startswith("三、")
#             or paragraph.startswith("四、")
#         ):
#             child_items.append({"content": paragraph})
#         else:
#             if current_item:
#                 current_item["child"] = {"level": "款", "items": child_items}
#                 json_obj["items"].append(current_item)
#                 current_item = None
#                 child_items = []
#             json_obj["items"].append({"content": paragraph})

#     # 處理最後一個條款
#     if current_item:
#         current_item["child"] = {"level": "款", "items": child_items}
#         json_obj["items"].append(current_item)

#     # 將JSON對象轉換為字符串並打印
#     json_str = json.dumps(json_obj, ensure_ascii=False, indent=4)
#     print(json_str)

#     # 如果需要保存為文件
#     with open("output.json", "w", encoding="utf-8") as f:
#         f.write(json_str)
# else:
#     print(f"Failed to retrieve data from URL. Status code: {response.status_code}")

import requests
import json

# 定義URL
url = "https://raw.githubusercontent.com/wazho/lawsnote-exam/main/inputs/%E4%B8%AD%E5%A4%AE%E6%B3%95%E8%A6%8F%E6%A8%99%E6%BA%96%E6%B3%95/93-05-19/%E7%AC%AC%20%E4%BA%94%20%E7%AB%A0%20%E6%B3%95%E8%A6%8F%E4%B9%8B%E4%BF%AE%E6%AD%A3%E8%88%87%E5%BB%A2%E6%AD%A2/%E7%AC%AC%2020%20%E6%A2%9D"

# 發送GET請求
response = requests.get(url)

# 檢查請求是否成功
if response.status_code == 200:
    # 取得文本內容
    text = response.text.strip()

    # 按段落分割文本
    paragraphs = text.split("\n")

    # 構建JSON對象
    json_obj = {"level": "項", "items": []}

    # 構建條款和項目列表
    items = []
    second_level_items = []
    third_level_items = []

    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if paragraph.startswith("法規有左列情形之一者，修正之："):
            if second_level_items:
                if third_level_items:
                    second_level_items[-1]["child"] = {
                        "level": "第三層",
                        "items": third_level_items,
                    }
                items[-1]["child"] = {"level": "第二層", "items": second_level_items}
                second_level_items = []
                third_level_items = []
            items.append({"content": paragraph})
        elif (
            paragraph.startswith("一、")
            or paragraph.startswith("二、")
            or paragraph.startswith("三、")
            or paragraph.startswith("四、")
            or paragraph.startswith("五、")
            or paragraph.startswith("六、")
            or paragraph.startswith("七、")
            or paragraph.startswith("八、")
            or paragraph.startswith("九、")
            or paragraph.startswith("十、")
        ):
            if third_level_items:
                second_level_items[-1]["child"] = {
                    "level": "第三層",
                    "items": third_level_items,
                }
                third_level_items = []
            second_level_items.append({"content": paragraph})
        elif (
            paragraph.startswith("（一）")
            or paragraph.startswith("（二）")
            or paragraph.startswith("（三）")
            or paragraph.startswith("（四）")
            or paragraph.startswith("（五）")
            or paragraph.startswith("（六）")
            or paragraph.startswith("（七）")
            or paragraph.startswith("（八）")
            or paragraph.startswith("（九）")
            or paragraph.startswith("（十）")
        ):
            third_level_items.append({"content": paragraph})
        else:
            if second_level_items:
                if third_level_items:
                    second_level_items[-1]["child"] = {
                        "level": "第三層",
                        "items": third_level_items,
                    }
                items[-1]["child"] = {"level": "第二層", "items": second_level_items}
                second_level_items = []
                third_level_items = []
            items.append({"content": paragraph})

    # 處理最後一個條款
    if second_level_items:
        if third_level_items:
            second_level_items[-1]["child"] = {
                "level": "第三層",
                "items": third_level_items,
            }
        items[-1]["child"] = {"level": "第二層", "items": second_level_items}

    json_obj["items"] = items

    # 將JSON對象轉換為字符串並打印
    json_str = json.dumps(json_obj, ensure_ascii=False, indent=4)
    print(json_str)

    # 如果需要保存為文件
    with open("output.json", "w", encoding="utf-8") as f:
        f.write(json_str)
else:
    print(f"Failed to retrieve data from URL. Status code: {response.status_code}")
