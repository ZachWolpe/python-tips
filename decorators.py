


import time

def timer_decorator(function):
    def wrapper(*args, **kwargs):
        start   = time.time()
        rt      = function(*args, **kwargs)
        end     = time.time()
        print(f'function: {function.__name__} was executed in {end-start} seconds.')
        return rt
    return wrapper


@timer_decorator
def funct(x):
    a = 1
    for i in range(1,x):
        a *= i
    return a


funct(10000)



# # example 2: timing
# import time
# def timed(function):
#     def wrapper(*args, **kwargs):
#         before  = time.time()
#         value   = function(*args, **kwargs)
#         after   = time.time()
#         fname   = function.__name__
#         print(f'function:{fname} took {after-before} seconds to execute.')
#         return value
#     return wrapper

# DEPRECATED ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++





# def mydecorator(function):

#     def wrapper(*args, **kwargs):
#         rt = function(*args, **kwargs)
#         print('     \nI am decorating your function!\n')
#         return rt
        
    
#     return wrapper

# @mydecorator
# def hello_world(person):
#     print('ok')
#     return f'     \nhello {person}!'



# # mydecorator(hello_world)()

# # x = hello_world('mike')
# # print(x)
# # parameters

# # practical example ------------------------------------------------------------++

# # example 1: logging

# def logged(function):
#     def wrapper(*args, **kwargs):
#         value = function(*args, **kwargs)
#         with open('logfile.txt', 'a+') as f:
#             fname = function.__name__
#             print(f'{fname} return value {value}')
#             f.write(f'{fname} return value {value}\n')
#         return value
#     return wrapper

# @logged
# def add(x,y):
#     return x+y
            
# # print(add(10,10))


# # example 2: timing
# import time
# def timed(function):
#     def wrapper(*args, **kwargs):
#         before  = time.time()
#         value   = function(*args, **kwargs)
#         after   = time.time()
#         fname   = function.__name__
#         print(f'function:{fname} took {after-before} seconds to execute.')
#         return value
#     return wrapper

# @timed
# def looper(x):
#     result = 1
#     for i in range(1,x):
#         result *= i
#     return result

# looper(10000)
