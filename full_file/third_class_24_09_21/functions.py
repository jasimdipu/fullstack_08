students = {
    "1234": {
        "name": "Md Shahin Alom",
        "dept": "BBA"
    },
    "3123": {
        "name": "Md Torikul Islam",
        "dept": "CSE"
    },
    "34534": {
        "name": "Md Jahid Islam",
        "dept": "IT"
    },
    "65342": {
        "name": "Md Obaidul Hasan",
        "dept": "SWE"
    }
}


def find_student(id):
    student_info = students.get(id)
    if student_info == None:
        print("No Student Found")
    else:
        print(student_info['name'], student_info['dept'])


find_student("34534")


def get_name(name, name2):
    print(name, name2)


def get_number(*args, **kwargs):
    print(args)
    print(kwargs)


# def getNames(*args, **kwargs):

get_name("sorif", "khan")

numbers = get_number(10, 20, 30, name='Tamim', age='42', dept='CSE')


def mixed_arguments(name, age, *args, **kwargs):
    return name + " " + str(age)


info = mixed_arguments("shohel", 25)
print(info)
print(numbers)
