import random


def get_lottery(n):

    numbers = list(range(1, 50))

    lottery_numbers = random.sample(numbers, n)  # 帶 n 個給他

    lottery_numbers.sort()
    return lottery_numbers


print(get_lottery(6))  # [1, 2, 3, 7, 10, 12]
print(get_lottery(3))  # [7, 10, 12]
