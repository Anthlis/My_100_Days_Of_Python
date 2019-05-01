'''
Write a decorator called make_html that wraps text inside one or more html tags.

As shown in the tests decorating get_text with make_html twice should
wrap the text in the corresponding html tags, so:

@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text
    
- would return: <p><strong>I code with PyBites</strong></p>


def make_html(element):
    """

    :type element: object
    """
    @wraps(element)
    def func_wrapper(text):
        return "<p>{0}</p>".format(element(text))
    return func_wrapper

@make_html
# @make_html('strong')
def get_text(text='I code with PyBites'):
    return text
'''

from functools import wraps

def make_html(element):
    @wraps(element)
    def func_wrapper(text):
        return "<p><strong>{0}</p></strong>".format(element(text))
    return func_wrapper

@make_html
# @make_html('strong')
def get_text(text='I code with PyBites'):
    return text

print(get_text('text'))
# print(get_text("I'm trying to pass Bite 22!"))

