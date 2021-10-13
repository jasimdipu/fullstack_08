for i in range(10):
    print(i, end=" ")

# iteration function
print(range(0, 20, 2))

print('-' * 100)


# 1. iterator vs 2. generator -> 1. default iterator func, 2. custom iterator function

def my_range(endpoint):
    for i in range(endpoint):
        yield i


for i in my_range(10):
    print(i, end=" ")
print()

# map(func, iter), reduce(func, seq), filter
print('-' * 100)
num = lambda x: x + x
# print(num([10, 20, 30, 40, 50]))
numbers = [10, 20, 30, 40, 50]

result = map(lambda x: x, numbers)

for i in result:
    print(i, end=" ")
print()
# reduce
from functools import reduce

print(reduce(lambda x, y: x + y, [10, 20, 30, 40, 50]))
print(reduce(lambda x, y: x if x > y else y, [20, 40, 10, 30, 50]))
print(reduce(lambda x, y: x if x < y else y, [20, 40, 10, 30, 50]))

# filter function
print("--filter--" * 10)


def even_number(number):
    if number % 2 == 0:
        return True
    return False


res = filter(even_number, [1, 3, 4, 7, 8, 10])
print(list(res))
