from functools import wraps


def make_html(text):
    #@wraps(text)
    def tag(func):
        def wrapper(*args, **kwargs):
            return "<{0}>{1}</{0}>".format(text, func(text),text)
        return wrapper
    return tag


@make_html("p")
@make_html("strong")
def get_text(text='I can code with PyBites'):
    return text

# print(get_text('Some random text here'))
# how do I get default text to print though? 
# print(get_text)
# print(get_text('text'))
# print(get_text())