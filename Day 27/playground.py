def add(*args):
    sum_value = 0
    for num in args:
        sum_value += num
    return sum_value
print(add(1,2,3,4,5,6,7))

def calculate(n,**kwargs):
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2,add=3, multiply=5)
