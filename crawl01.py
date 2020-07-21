import time


def cal_time(fn):
    print("hi")

    def inner(x, *args, **kwargs):
        start = time.time()
        s = fn(x)
        end = time.time()
        # print(f"spend...{end - start}")
        return s, end - start

    return inner


@cal_time
def demo(n):
    x = 0
    for i in range(1, n):
        x += i
    # print(x)
    return x


m = demo(10000000, 'hello')
print(m)
