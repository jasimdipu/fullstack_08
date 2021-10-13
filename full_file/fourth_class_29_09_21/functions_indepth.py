# nested functions

def first_func():
    def sec_func():
        print("this is an inner function")

    sec_func()
    print("this is an outter function")


def outter_func(name):
    def innner_func():
        print("welcome ", name)

    return innner_func()


def factorial(number):
    try:
        if not isinstance(number, int):
            raise TypeError("Sorry, number have to be integer")
        if number < 0:
            raise ValueError("please input number must be bigger then 0")

        def cal_fact(num):
            if num <= 1:
                return 1
            return num * cal_fact(num - 1)

        return cal_fact(number)
    except Exception as e:
        print(e)


print(factorial(5))

first_func()
outter_func("Jahid")
print("*" * 10)
# lambda function
#
# def num(x):
#   if x == 10:
#     return x**3
#   else:
#     return x

num = lambda x: x ** 3 if x == 10 else x

print(num(10))

another_lambda = lambda a, b: a + b if a == 100 and b == 200 else (b - a)
print(another_lambda(500, 1000))


