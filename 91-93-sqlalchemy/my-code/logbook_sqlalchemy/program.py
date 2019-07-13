import sqlalchemy
import datetime


def main():
    header()
    last_flew()
    flight_details()
    print_flights()


def flight_details():
    # enter date and strpformat it into just yyyy-mm-dd
    # date = datetime.datetime.now()
    date = datetime.datetime.today().strftime('%A, %d %B %Y')  
    
    print("Enter flight details, below: \n")
    rego = input("[Q1/3] Aircraft registration: e.g. EYA:  ").upper()
    aircraft_type = input("[Q2/3] Aircraft type, e.g. PA-28-181: ")
    flight_time = input("[Q3/3] Flying time, e.g. 0.7: ")
    print(f"\nYour last flight recorded was on {date}, flying ZK-{rego}, {aircraft_type} for {flight_time} hrs")


def print_flights():
    flts = game_service.show_flights(flights)
    print(flts)


def header():
    print("\n***********************************")
    print("*  LOGBOOK DATABASE - SQLALCHEMY  *")
    print("***********************************\n")


def last_flew():
    pass


if __name__ == '__main__':
    main()