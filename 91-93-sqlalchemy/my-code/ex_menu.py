import sys, os

menu_actions = {}
room_menu = {}


# Main menu
def main_menu():
    # os.system('clear')

    print("\n*****************************************")
    print("*         Home Inventory App            *")
    print("*****************************************\n")
    print("1. Add Room")
    print("2. Add Inventory")
    print("3. View Inventory List")
    print("4. Total Value")
    print("\n0. Exit")
    choice = input(" >>  ")
    exec_menu(choice)

    return


# Execute menu
def exec_menu(choice):
    # os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return


# Menu 1
def rooms():
    print("\n*****************************************")
    print("*   Home Inventory App - ADD A ROOM     *")
    print("*****************************************\n")
    print("Add Room !\n")
    print("9. Back")
    # print("0. Quit") # careful this still works!
    choice = input(" >>  ")
    exec_menu(choice)
    return


def add_room():
    pass


def list_rooms():
    pass


# Menu 2
def menu2():
    print("Hello Menu 2 !\n")
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return


# Back to main menu
def back():
    menu_actions['main_menu']()


# Exit program
def exit():
    print("Byeeee!")
    sys.exit()


# =======================
#    MENU DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': rooms,
    '2': menu2,
    '9': back,
    '0': exit,
}

room_menu = {
    'room_menu': room_menu,
    '1': add_room,
    '2': list_rooms,
    '9': back
}

# =======================
#      MAIN PROGRAM
# =======================

if __name__ == "__main__":
    main_menu()