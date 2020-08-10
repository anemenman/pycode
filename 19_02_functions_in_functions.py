def mul(a):
    def helper(b):
        return a * b

    return helper


print(mul(2)(5))
