import timeit


def for_square(n):  
    new_list = []
    for i in range(0, n):
        if i % 2 == 0:
            new_list.append(n**2)
    return new_list


def list_comp_square(n):  
    return [i**2 for i in range(0, n) if i % 2 == 0]


print("Time taken by For Loop: {}".format(timeit.timeit('for_square(10)', 'from __main__ import for_square')))


print("Time taken by List Comprehension: {}".format(timeit.timeit('list_comp_square(10)', 'from __main__ import list_comp_square')))  