from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print('I am doing some boring work before executing a_func()')
        
        a_func()
        
        print('I am doing some other work after executing a_func()')
        
    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    """ Hey you! Decorate me! """
    print('I am the function which needs some decoration to remove my foul smell')

a_function_requiring_decoration()
print()
print(a_function_requiring_decoration.__name__)

'''
Note: @wraps takes a function to be decorated and adds the functionality of
copying over the function name, docstring, arguments list, etc. This allows to
access the pre-decorated function’s properties in the decorator.
'''