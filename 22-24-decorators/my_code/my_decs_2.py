def a_new_decorator(a_func):
    
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

# the @a_new_decorator is just a short way of saying:
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

print()
print(a_function_requiring_decoration.__name__)

'''
# output:wrapTheFunction

That’s not what we expected! Its name is “a_function_requiring_decoration”.
Well our function was replaced by wrapTheFunction. It overrode the name and
docstring of our function. Luckily Python provides us a simple function to solve
this problem and that is functools.wraps. Let’s modify our previous example
to use functools.wraps:
'''