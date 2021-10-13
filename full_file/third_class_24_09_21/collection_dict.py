d = {}

# key value pair -> key:value
d = {"key1": "value1", 2: 10, 3: 10.50}
# print(d)
# print(d["key1"])

# for i, j in d.items():
#     if i == "key1":
#         print(i, j)

# print(d.get('key1'))

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


print(students.get("5234"))

# student_info = students.get(input())

# if student_info == None:
#     print("No Data")
# else:
#     print(student_info['name'], student_info['dept'])

# type casting
# v = int(input())
# v = int(v)
# v = float(v)

print(d.keys())
print(d.values())

d2 = {"key2": "value2"}

d.update(d2)
print(d)
