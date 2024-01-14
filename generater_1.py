def xyz():
    yield 10
    yield 20
    yield 30
    return 50
    print(xyz())
a = xyz()
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(xyz())
