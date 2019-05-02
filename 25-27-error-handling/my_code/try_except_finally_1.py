short_list = [1, 2, 3]

while True:
    value = input('Position [q to quit]? ').lower()
    if value == 'q':
        print('Bye!')
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Need a position between 0 and', len(short_list)-1, 'but got', position)
    except Exception as other:
        print('Something else broke:', other)
    finally:
        print("Try again?")
              