'''
Bite 67. Working with datetimes
This Bite involves solving two problems using datetime:

We kicked off our 100 Days of Code project on March 30th, 2017. Calculate what date we finished the full 100 days!
PyBites was founded on the 19th of December 2016. We're attending our first PyCon together on May 8th, 2018.
Can you calculate how many days from PyBites' inception to our first PyCon meet up?

----------------

from calc_dts import (get_hundred_days_end_date,
                      get_days_between_pb_start_first_joint_pycon)


def test_get_hundred_days_end_date():
    assert get_hundred_days_end_date() == '2017-07-08'


def test_get_days_till_pycon_meetup():
    assert get_days_between_pb_start_first_joint_pycon() == 505
    
    
----------------

The datetime classes in Python are categorized into main 5 classes.

date – Manipulate just date ( Month, day, year)
time – Time independent of the day (Hour, minute, second, microsecond)
datetime – Combination of time and date (Month, day, year, hour, second, microsecond)
timedelta— A duration of time used for manipulating dates
tzinfo— An abstract class for dealing with time zones

https://www.guru99.com/date-time-and-datetime-classes-in-python.html

'''


from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    return str(start_100days + timedelta(days=100)) # needed to string'ify the class datetime.date here
    

def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    days_between = pycon_date - pybites_founded
    return days_between.days
    
def main():
    print(get_hundred_days_end_date())
    print(get_days_between_pb_start_first_joint_pycon())

if __name__ == '__main__':
    main()
    
