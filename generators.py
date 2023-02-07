


import sys

# range items (generators)
r1 = range(1)
r2 = range(1000000)

# convert to list 
l1 = list(r1)
l2 = list(r2)

def ptr(obj, name):
    print(f'object:{name} is {sys.getsizeof(obj):>7} bytes.')

print()
ptr(r1, 'r1')
ptr(r2, 'r2')
ptr(l1, 'l1')
ptr(l2, 'l2')
print()



def power_x(x):
    y = 0
    while True:
        yield x**y
        y += 1

value = power_x(4)
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print()


# def mygenerator(n):
#     for x in range(n):
#         yield x**3
    
# values = mygenerator(141343232)

# import sys
# i = sys.getsizeof(values)
# # print(i)
# # print(next(values))
# # print(next(values))
# # print(next(values))
# # print(next(values))
# # print(next(values))


# # infinite sequences

# def infinite_sequences():
#     results = 1
#     while True:
#         yield results
#         results *= 5


# values = infinite_sequences()

# # print(next(values))
# # print(next(values))
# # print(next(values))
# # print(next(values))

# for x in values:
#     print(x)