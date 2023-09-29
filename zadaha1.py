x = int(input())
y = int(input())


if x < 10000 or y < 10000:
    if x <= y:
        b = y - x
        c = x - 1
        a = c/b

        print(b)
        print(c)
        print(a)
        if isinstance(a, int):
            print("YES")
        else:
            print("NO")


