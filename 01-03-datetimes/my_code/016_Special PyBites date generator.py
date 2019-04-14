'''
Bite 16. Special PyBites date generator
Write a generator that returns special dates for PyBites:

Every year mark counting from PYBITES_BORN date
Every 100 days mark counting from PYBITES_BORN
See the tests for more details how your code will be tested:
as this is a beginner's challenge we only calculate a few years ahead,
leaving the next leap year (2020) out of this challenge.

We will revisit this in an intermediate challenge. Have fun!

import datetime
from itertools import islice

from gendates import gen_special_pybites_dates


def test_gen_special_pybites_dates():
    gen = gen_special_pybites_dates()
    dates = list(islice(gen, 100))

    expected = [datetime.datetime(2017, 3, 29, 0, 0),
                datetime.datetime(2017, 7, 7, 0, 0),
                datetime.datetime(2017, 10, 15, 0, 0),
                datetime.datetime(2017, 12, 19, 0, 0),
                datetime.datetime(2018, 1, 23, 0, 0),
                datetime.datetime(2018, 5, 3, 0, 0),
                datetime.datetime(2018, 8, 11, 0, 0),
                datetime.datetime(2018, 11, 19, 0, 0),
                datetime.datetime(2018, 12, 19, 0, 0),
                datetime.datetime(2019, 2, 27, 0, 0)]

    assert dates[:10] == expected
    
% 365
% 100

'''
from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)

def gen_special_pybites_dates():
    days = 0
    while True:
        days += 1
        if days % 100 == 0 or days % 365 == 0:
            yield PYBITES_BORN + timedelta(days=days)


# def gen_special_pybites_dates():
#     start_date = PYBITES_BORN
#     end_date = start_date + timedelta(days=100)
#     while start_date <= end_date:
#         yield start_date
#         start_date = start_date + timedelta(days=1) # this counts every day for a hundred days.

        # failed because I hadn't shown the 100 days mark??? So elected to do % 365 above.

# def main():
#     print(PYBITES_BORN)
#     print(list(gen_special_pybites_dates()))
#
# if __name__ == '__main__':
#     main()
