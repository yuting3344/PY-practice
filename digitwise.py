# Program a function that takes two numbers, n and k, and outputs the number of digits in n after applying Digitwise addition k times. Since the answer can be very large, return the answer modulo 1_000_000_007.
# Your solution is expected to be O(klogn).


MOD = 1_000_000_007


def digitwise_addition(n):
    result = []
    for digit in str(n):
        if digit == "9":
            result.append("10")
        else:
            result.append(str(int(digit) + 1))
    return "".join(result)


def digitwise_addition_k_times(n, k):
    n = str(n)
    for _ in range(k):
        n = digitwise_addition(n)
    return len(n) % MOD
