'''
Bite 128. Work with datetime's strptime and strftime
In this Bite you get some more practice with datetime's useful strptime and stftime.

Complete the two functions: years_ago and convert_eu_to_us_date following the instructions in their docstrings.

This is the defintion and difference between the two:

strptime: parse (convert) string to datetime object.
strftime: create formatted string for given time/date/datetime object according to specified format.
Reference: 8.1.8. strftime() and strptime() Behavior. Good luck and keep calm and code in Python!

import pytest

from dt_convert import years_ago, convert_eu_to_us_date


def test_years_ago():
    assert years_ago('8 Aug, 2015') == 3
    assert years_ago('6 Sep, 2014') == 4
    assert years_ago('1 Oct, 2010') == 8
    assert years_ago('31 Dec, 1958') == 60


def test_years_ago_wrong_input():
    with pytest.raises(ValueError):
        # Sept != valid %b value 'Sep'
        assert years_ago('6 Sept, 2014') == 4


def test_convert_eu_to_us_date():
    assert convert_eu_to_us_date('11/03/2002') == '03/11/2002'
    assert convert_eu_to_us_date('18/04/2008') == '04/18/2008'
    assert convert_eu_to_us_date('12/12/2014') == '12/12/2014'
    assert convert_eu_to_us_date('1/3/2004') == '03/01/2004'


def test_convert_eu_to_us_date_invalid_day():
    with pytest.raises(ValueError):
        convert_eu_to_us_date('41/03/2002')


def test_convert_eu_to_us_date_invalid_month():
    with pytest.raises(ValueError):
        convert_eu_to_us_date('11/13/2002')


def test_convert_eu_to_us_date_invalid_year():
    with pytest.raises(ValueError):
        convert_eu_to_us_date('11/13/year')
        
'''

# from datetime import datetime
# from datetime import date
import datetime

THIS_YEAR = 2018


def years_ago(date):
    """Receives a date string of 'DD MMM, YYYY', for example: 8 Aug, 2015
       Convert this date str to a datetime object (use strptime).
       Then extract the year from the obtained datetime object and subtract
       it from the THIS_YEAR constant above, returning the int difference.
       So in this example you would get: 2018 - 2015 = 3"""
    f_date = datetime.datetime.strptime(date, "%d %b, %Y")
    date_year = datetime.datetime.strftime(f_date, "%Y")
    return THIS_YEAR - int(date_year)

#   dt = datetime.strptime(date, '%d %b, %Y')
#   return THIS_YEAR - dt.year
#   think this will require (as per the original test): from datetime import datetime
        

def convert_eu_to_us_date(date):
    """Receives a date string in European format of dd/mm/yyyy, e.g. 11/03/2002
       Convert it to an American date: mm/dd/yyyy (in this case 03/11/2002).
       To enforce the use of datetime's strptime / strftime (over slicing)
       the tests check if a ValueError is raised for invalid day/month/year
       ranges (no need to code this, datetime does this out of the box)"""
    f_date = datetime.datetime.strptime(date, "%d/%m/%Y")
    converted_date = datetime.datetime.strftime(f_date, "%m/%d/%Y")
    return converted_date

#   dt = datetime.strptime(date, '%d/%m/%Y')
#   return dt.strftime('%m/%d/%Y')


def main():
    print(years_ago('6 Sep, 2014'))
    print(convert_eu_to_us_date('11/03/2002'))
    
if __name__ == '__main__':
    main()
    


