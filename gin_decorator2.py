def memo(n):
    print(n)
    def memo_inner(f):
        # def wrapper(*args, **kwargs):
        #     print(f"args: {args}")
        #     print(f"kwargs: {kwargs}")
        #     return f(*args, **kwargs)
        # return wrapper
        # return lambda x, y, z, a: f(x, y, z, a)
        return f
    return memo_inner

@memo(42)
def f(d, b, c, mn):
    a = 0
    def g():
        nonlocal a
        a += 2
        return a
    a += 1
    print(f"g() inside f: {g()}")
    return g



# print(f)
# print(f())
xs = { 0, 1, 2 }
print(f(*xs, mn=3)())
