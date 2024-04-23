# 編號：CANDY-010
# 程式語言：Python
# 題目：把數字以 10 進位展開式呈現，數字均為大於 0 的正整數
# 範例：9527 變成 "1000 x 9 + 100 x 5 + 10 x 2 + 7"


def expanded_form(num):
    digits_list = list(str(num))
    terms = []
    for i, value in enumerate(digits_list):  # 用 enumerate 來得到索引
        pow_num = len(digits_list) - 1 - i  # 設定次方所需變數
        if value != "0":  # 當值不等於0
            if i == len(digits_list) - 1:  # 當索引等於個位數，直接印出
                terms.append(value)
            else:
                terms.append(f"{10 ** pow_num}x{value}")  # 其他位數按照次方變數處理

    return " + ".join(terms)


print(expanded_form(8))
# 印出 8
print(expanded_form(25))
# 印出 10 x 2 + 5
print(expanded_form(148))
# 印出 100 x 1 + 10 x 4 + 8
print(expanded_form(1450))
# 印出 1000 x 1 + 100 x 4 + 10 x 5
print(expanded_form(60308))
# 印出 10000 x 6 + 100 x 3 + 8
