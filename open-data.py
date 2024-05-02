# 網路連線
import urllib.request as request
import json

src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data = json.load(response)  # json模組取得
# print(data)

clist = data["result"]["results"]
print(clist)
# 串接、擷取公開資料
