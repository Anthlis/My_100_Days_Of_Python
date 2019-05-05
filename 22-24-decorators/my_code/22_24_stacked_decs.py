from functools import wraps

def timeit(func):
    '''Decorator to time a function'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        # before calling the decorated function
        print('== starting timer')
        start = time.time()
        
        # call the decorated function
        func(*args, **kwargs)
        
        # after calling the decorated function
        end = time.time()
        print(f'== {func.__name__} took {int(end-start)} seconds to complete')
    
    return wrapper


def print_args(func):
    '''Decorator to print function arguments'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        # before
        print()
        print('*** args:')
        for arg in args:
            print(f'- {arg}')
        
        print('**** kwargs:')
        for k, v in kwargs.items():
            print(f'- {k}: {v}')
        print()
        
        # call func
        func(*args, **kwargs)
    return wrapper


def generate_report(*months, **parameters):
    time.sleep(2)
    print('(actual function) Done, report links ...')
    
    
@timeit
@print_args
def generate_report(*months, **parameters):
    time.sleep(2)
    print('(actual function) Done, report links ...')
    


parameters = dict(split_geos=True, include_suborgs=False, tax_rate=33)

generate_report('October', 'November', 'December', **parameters)