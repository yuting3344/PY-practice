nums = [1,2,3]

result = [n * 2 for n in nums]

print(result)
#[2,4,6]
                
for i in range(1,10):
    for j in range(1,10):
        print(f"{i}x{j}={i*j}")

# 九九乘法表

for i in range(1,10,2):
    print(f"{'*'* i:^11}")
print(f"{'*':^11}")
print(f"{'*':^11}")

# 置中聖誕樹＋樹幹

def print_star(n):
    n = n * 2

    for i in range(1,n,2):
        print(f"{"*" * i :^{n}}")

print_star(5)

# 置中聖誕樹＋樹幹 --> for...in

result = [n for n in range(10) if n % 2 == 0 ]
print(result)

# [0,2,4,6,8]

nums = [9, 5, 2, 7]
result=[n * 2 if n % 2 == 0 else n for n in nums]
print(result)

# [9, 5, 2, 7] -> [9, 5, 4, 7]
