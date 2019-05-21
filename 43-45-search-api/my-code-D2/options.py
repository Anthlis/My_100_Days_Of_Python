# https://stackoverflow.com/questions/34927479/command-line-show-list-of-options-and-let-user-choose

options = ["Option 1", "Option 2", "Option 3"]

def let_user_pick(options):
    print("Please choose:")
    for idx, element in enumerate(options, start=1):
        print(f"{idx}) {element}")
    value = input("Enter number: ")
    print(value)
    if 0 < int(value) <= len(options):
        return options[int(value)-1]
    else: pass

print(let_user_pick(options))