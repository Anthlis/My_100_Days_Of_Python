
# https://www.codementor.io/bolajiolajide/creating-a-simple-python-decorator-axx17yfwm


def noun(i):
    def tag(func):
        def wrapper(name):
            return "My {0} is {1}".format(i, func(name))

        return wrapper

    return tag


@noun("name")
@noun("age")
def say_something(something):
    return something


print(say_something('Bolaji'))



@noun("age")
def say_something(something):
    return something


print(say_something(24))
