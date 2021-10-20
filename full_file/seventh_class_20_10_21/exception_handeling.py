print(5 / 2)
# exception
try:
    number = int(input())
    print(100 / number)
except ZeroDivisionError as e:
    print("Do not input zero")
except Exception as e:
    print(e)
try:
    print(400 / "asdd")
except Exception as e:
    print(e)
print(15 / 3)


def error_handling():
    try:
        number = int(input())
        print(100 / number)
    except Exception as e:
        print(e)
        error_handling()


error_handling()


# Custom exception
# small number and big number exception

class SmallNumberException(Exception):

    def __init__(self, message="number is smaller than 10"):
        self.message = message
        super().__init__(self.message)


class BigNumberException(Exception):
    def __init__(self, message="number is bigger than 100"):
        self.message = message
        super().__init__(self.message)


class NumberNotInRange(Exception):
    def __init__(self, number, message="Number is not in range"):
        self.number = number
        self.message = str(number) + " is not in range"
        super().__init__(self.message)


class Number:
    def takeNumber(self, number):
        try:
            if number < 10:
                raise SmallNumberException
            if number > 100:
                raise BigNumberException
            print(number)
        except SmallNumberException as e:
            print(e)
        except BigNumberException as e:
            print(e)

    def number2(self, number):
        try:
            if not 200 < number < 300:
                raise NumberNotInRange(number)
            print(number, "is in perfect range")
        except NumberNotInRange as e:
            print(e)


number = Number()
number.takeNumber(15)
number.number2(250)
