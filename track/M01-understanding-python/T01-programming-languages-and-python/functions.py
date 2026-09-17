# add 2 numbers

def add1():
    a, b = 10, 10
    c = a + b
    print(c)

add1()


# no arguments + return value

def add2():
    a, b = 10, 20
    c = a + b
    return c

print(add2())


# arguments + no return value

def add3(a, b):
    c = a + b
    print(c)

add3(10, 50)


# arguments + return value

def add4(a, b):
    c = a + b
    return c

print(add4(100, 200))