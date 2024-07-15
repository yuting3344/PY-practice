import requests
import json

url = "https://raw.githubusercontent.com/wazho/lawsnote-exam/main/inputs/%E5%B0%8D%E5%A4%96%E6%BC%81%E6%A5%AD%E5%90%88%E4%BD%9C%E7%AE%A1%E7%90%86%E8%BE%A6%E6%B3%95/113-02-20/%E7%AC%AC%204%20%E6%A2%9D"


response = requests.get(url)


if response.status_code == 200:

    text = response.text.strip()

    paragraphs = text.split("\n")

    json_obj = {"level": "項", "items": []}

    items = []
    current_item = None
    current_subitem = None
    current_subsubitem = None

    for paragraph in paragraphs:
        paragraph = paragraph.strip()

        if paragraph.startswith(
            "漁業合作國有指定合作漁船之卸魚或轉載港口者，應符合下列條件之一："
        ):
            current_item = {"content": paragraph, "child": {"level": "款", "items": []}}
            items.append(current_item)
        elif paragraph.startswith("一、") or paragraph.startswith("二、"):
            current_subitem = {
                "content": paragraph,
                "child": {"level": "目", "items": []},
            }
            current_item["child"]["items"].append(current_subitem)
        elif paragraph.startswith("（一）") or paragraph.startswith("（二）"):
            current_subsubitem = {"content": paragraph}
            current_subitem["child"]["items"].append(current_subsubitem)
        elif paragraph.startswith("一") or paragraph.startswith("二"):
            if current_subitem is None:
                current_subitem = {
                    "content": paragraph,
                    "child": {"level": "目", "items": []},
                }
                current_item["child"]["items"].append(current_subitem)
            else:
                current_subsubitem = {"content": paragraph}
                current_subitem["child"]["items"].append(current_subsubitem)
        else:
            current_item = {"content": paragraph, "child": {"level": "款", "items": []}}
            items.append(current_item)
            current_subitem = None
            current_subsubitem = None

    json_obj["items"] = items

    json_str = json.dumps(json_obj, ensure_ascii=False, indent=4)
    print(json_str)

    with open("output.json", "w", encoding="utf-8") as f:
        f.write(json_str)
else:
    print(f"Failed to retrieve data from URL. Status code: {response.status_code}")
