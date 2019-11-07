import module
import timeit
a=module.fibonacci(100)
code="""
import module
a=module.fibonacci(100)
"""
t=timeit.timeit(code,number=1);print(t)

"""it take 0.1131 sec"""
