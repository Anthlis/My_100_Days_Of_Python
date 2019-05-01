
# http://scottlobdell.me/2015/04/decorators-arguments-python/


# def decorator(arg1, arg2):
#
#     def real_decorator(function):
#
#         def wrapper(*args, **kwargs):
#             print("<{0}><{1}>Congratulations!</{0}></{1}>".format(arg1, arg2))
#             function(*args, **kwargs)
#         return wrapper
#
#     return real_decorator
#
# @decorator("arg1", "arg2")
# def print_args(*args):
#     for arg in args:
#         print(arg)
#
# # Getting crazy down here:
# decorator("arg1", "arg2")(print_args)(1, 2, 3)

from functools import wraps

def make_html(arg1):
    # @wraps(text)
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            print("<{0}>words</{0}>".format(arg1))
            function(*args, **kwargs)
        return wrapper

    return real_decorator

@make_html("p")
# @make_html("strong")
def get_text(text="I can code with PyBites"):
    return text

# print(get_text(text="I'm trying to pass Bite 22!"))
print(get_text())
