from functools import wraps


def make_html(element):
    def tag(func):
        def wrapper(text):
            return "<{0}>{1}</{0}>".format(element, func(text), element)
        return wrapper
    return tag

@make_html("p")
@make_html("strong")
def get_text(text='I code with PyBites'):
    return text

print(get_text(text='I can code with PyBites'))