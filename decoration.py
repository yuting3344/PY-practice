# function decoration 純裝飾
# ---------------------> example 1
def dec(x):
    return x


@dec
def dog():
    print("Woof!Woof!")


dog()


# --------------------> example 2 --> double call
def double(fn):
    fn()
    return fn


@double
def go():
    print("go!")


go()

# -----------------------> example 3
