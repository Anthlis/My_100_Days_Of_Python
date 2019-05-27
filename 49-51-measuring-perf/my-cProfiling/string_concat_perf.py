import timeit

list_of_words = [" half way through #100days!!! "] * 10


def using_join(list_of_words):  
    return "".join(list_of_words)


def using_concat_operator(list_of_words):  
    final_string = ""
    for i in list_of_words:
        final_string += i
    return final_string


print("Using join() takes {} s"
      .format(timeit.timeit('using_join(list_of_words)', 'from __main__ import using_join, list_of_words')))


print("Using += takes {} s"
      .format(timeit.timeit('using_concat_operator(list_of_words)', 'from __main__ import using_concat_operator, list_of_words')))

