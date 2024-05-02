# 儲存檔案 -1
# file = open("data.txt", mode="w", encoding="utf-8")  # 開啟
# file.write("正妹\nHey!")  # 寫入
# file.close()  # 關閉
# 儲存檔案 -2
# with open("data.txt", mode="w", encoding="utf-8") as file:
#     file.write("5\n9\n10")
# 讀取檔案
# with open("data.txt", mode="r", encoding="utf-8") as file:
#     data = file.read()
# print(data)

# 讀取後加總 - 小練習
# sum = 0
# with open("data.txt", mode="r", encoding="utf-8") as file:
#     for line in file:
#         sum += int(line)
# print(sum)

# 使用JSON格式讀取、複寫檔案
import json

# 從檔案中讀取資料並且更新
with open("config.json", mode="r") as file:
    data = json.load(file)  # data 是一個字典資料
print(data)
data["name"] = "New Name"  # 修改變數中的資料
# 把最新的資料複寫回檔案
with open("config.json", mode="w") as file:
    json.dump(data, file)
