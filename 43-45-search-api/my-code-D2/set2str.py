def test():
    some_var_set=set('abca')
    print("here is the set:",some_var_set,type(some_var_set))
    some_var_string=''.join(some_var_set)    
    print("here is the string:",some_var_string,type(some_var_string))

test()