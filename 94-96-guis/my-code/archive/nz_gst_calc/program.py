import sys
import gstapi

def main():
    print()
    print("--------------------------------------")
    print("    NZ GST CALC (CLI EDITION)")
    print("--------------------------------------")
    print()
    print('My amazing NZ GST Calculator!')
    mode = input("Do you want to [a]dd or [s]ubtract GST from a total? [q] to quit ").strip().lower()

    if mode == 'a':
        add_total = float(input("\nEnter the amount to add GST to: $"))
        gst = (add_total*15)/100
        gt = add_total + (add_total*15)/100
        print(f'Subtotal = ${add_total:.2f}')
        print(f'GST amount = ${gst:.2f}')
        print(f'Grand total = ${gt:.2f}')

    elif mode == 's':
        subt_total = float(input("\nEnter the amount to subtract GST from:  "))
        gst = (subt_total * 15) / 100
        gt = (1-0.15) * subt_total
        print(f'Subtotal = ${subt_total:.2f}')
        print(f'GST amount = ${gst:.2f}')
        print(f'Grand total = ${gt:.2f}')
    elif mode == 'q':
        print('Bye!')
        sys.exit()
    else:
        print("Didn't recognise that input. Halting now...")

    print("")


if __name__ == '__main__':
    main()
