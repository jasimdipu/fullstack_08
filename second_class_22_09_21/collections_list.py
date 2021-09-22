# list, tuple, set, dictionaries

l = [1, 2, 3, 4.5, 5.5, 6.5, "seven", 'eight', 'nine']
print(type(l))

print(l)

# for i in l:
#     print(i)
#     print(type(i))

# indexing
print(l[0], l[7])
print(l[3])
print(l[6])
print(l[8])

# slicling
print(l[2:5])
print(l[:4])
print(l[-1])
print(l[::-1])

# list mutable collection
print(l)
l[0] = 100
print(l)

l = l+[1000]
print(l)

# built in func

l.append(200)
print(l)

l.reverse()
print(l)

# l.sort()
# print(l)

p = l.pop()
print(p)
print(l)

print(l.count(200))

# comprehension
l1 = [i for i in range(10)]
print(l1)
