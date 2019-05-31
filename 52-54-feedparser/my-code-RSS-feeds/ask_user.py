def ask_user():
    print("Do you want to save?")
    response = ''
    while response.lower() not in {"yes", "no"}:
        response = input("Please enter yes or no: ")
    return response.lower() == "yes"

ask_user()