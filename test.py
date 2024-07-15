import json


text = """
法規條文應分條書寫，冠以「第某條」字樣，並得分為項、款、目。項不冠數字，空二字書寫，款冠以一、二、三等數字，目冠以（一）、（二）、（三）等數字，並應加具標點符號。
前項所定之目再細分者，冠以１、２、３等數字，並稱為第某目之１、２、３。
"""

paragraphs = text.strip().split("\n")

json_obj = {
    "level": "項",
    "items": [{"content": paragraph.strip()} for paragraph in paragraphs],
}

json_str = json.dumps(json_obj, ensure_ascii=False, indent=4)
print(json_str)


with open("output.json", "w", encoding="utf-8") as f:
    f.write(json_str)
