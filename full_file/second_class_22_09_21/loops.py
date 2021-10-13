# loop -> for, while

# for i in range(0, 20, 2):
#     print (i)


# i=0
# n=10

# while i<n:
#     if i == 7:
#         print(i)
#     print("not found")
#     i = i+1

count=0
for i in ["one", 'two', 'three', 'two']:
    if i == "two":
        print(i, " found")
        count+=1
       
else:
    print("not found")
print(count)




