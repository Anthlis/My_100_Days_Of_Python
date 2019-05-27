import time
import timeit


def fast():
    print("I run fast")


def slow():
    time.sleep(3)
    print("I run slow")


def medium():
    time.sleep(1)
    print("I run a little slowly")


def for_loop_square(n):
    new_list = []
    for n in range(0, 100):
        if n % 2 == 0:
            new_list.append(n**2)


def list_comp_square(n):
    new_list = [n**2 for n in range(0, 100) if n % 2 == 0]


def main():
    fast()
    slow()
    medium()
    
    
if __name__ == '__main__':
    print('\nStarting... ')

    main()

    print("Time taken by the For Loop: {}"
          .format(timeit.timeit('for_loop_square(100)', 'from __main__ import for_loop_square')))

    print("Time taken by the List Comprehension: {}"
          .format(timeit.timeit('list_comp_square(100)', 'from __main__ import list_comp_square')))

    print('... finished.')
