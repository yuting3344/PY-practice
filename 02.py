
# sum 類似JS's reduce()

def sum_of_numbers(n):
    return sum([int(n) for n in str(n)])


print(sum_of_numbers(1450))  # 10
print(sum_of_numbers(9527))  # 23

# ------------------------------------>
data = [7, 1, 4, 9, 10, 8]


def double_list(n):
    for i in range(len(n)):
        n[i] *= 2


double_list(data)
print(data)  # 兩倍

# ------------------------------------>

# 索引值/enumerate
chars = ["a", "b", "c"]

for i, c in enumerate(chars, start=1):
    print(f"{i}-{c}")

# ----------------------------------->

# slice 搭配 list

import math

numbers = [1, 6, 8, 3, 5, 7, 9]
result = [0 for _ in range(math.ceil(len(numbers) / 2))]

numbers[::2] = result # 把奇數元素換成0(result裡面期望替換的)


print(numbers)

# --------------------------------------->

# 字典
hero = {"name": "悟空", "age": 100}

age = hero.setdefault("age", 5) # 如果字典裡面本來就有，就不會改動原本的物件；如果沒有，加進去！
print(age)
print(hero)

