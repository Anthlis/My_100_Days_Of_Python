from functools import wraps

def show_args(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("hi from decorator - args: ")
        print(args)
        result = function(*args, **kwargs)
        print("hi again from decorator - kwargs: ")
        print(kwargs)
        return result
    # return wrapper as a decorated function
    return wrapper

@show_args
def get_profile(name, active=True, *sports, **awards):
    print("\n\thi from the get_profile function\n")
    
get_profile('bob', True, 'basketball', 'soccer',
            pythonista='special honor of the community', topcoder='2017 code camp')