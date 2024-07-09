import re


def size_to_number(size):
    base_sizes = {"s": 36, "m": 38, "l": 40}
    if not re.match(r"^(x*)[sml]$", size):
        return None

    base_size = size[-1]
    modifier = size[0:-1]

    if base_size == "m" and modifier:
        return None

    num_modifier = len(modifier)
    adjusted_num = (
        -2 * num_modifier
        if base_size == "s"
        else 2 * num_modifier if base_size == "l" else 0
    )

    return base_sizes[base_size] + adjusted_num


# 測試
print(size_to_number("xs"))  # 34
print(size_to_number("s"))  # 36
print(size_to_number("m"))  # 38
print(size_to_number("l"))  # 40
print(size_to_number("xl"))  # 42
