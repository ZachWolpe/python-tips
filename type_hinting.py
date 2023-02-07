
#!pip install mypy
def func(arg_1:int, arg_2:list[int]) -> tuple:
    return arg_1, arg_2

func('12', [1,2,3])
