from functools import wraps

def make_html(func):
    @wraps(func)
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))

    return func_wrapper

@make_html
def get_text(name):
    return "Lorem ipsum, {0} dolor sit amet".format(name)

print(get_text("John"))