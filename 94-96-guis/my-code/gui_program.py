import sys
from gooey import GooeyParser, Gooey



@Gooey(program_name='NZ GST Calculator',
       program_description='My Amazing NZ GST Calculator!',
       show_success_modal=False)
def main():
    print()
    print("--------------------------------------")
    print("    NZ GST CALC (GUI EDITION)")
    print("--------------------------------------")
    print()

    mode, value = get_params()

    if mode == 'add':
        print('Add GST to the amount:')
        float(value)
        gst = (float(value) * 15) / 100
        gt = float(value) + (float(value)*15)/100

    elif mode == 'subtract':
        print('Subtract GST from the amount:')
        gst = (float(value) * 15) / 100
        gt = float((1-0.15) * float(value))

    else:
        print('Something caused else to run')

    print(f'Subtotal = ${value}')
    print(f'GST amount = ${gst:.2f}')
    print(f'Grand total = ${gt:.2f}')


def get_params():
    parser = GooeyParser()
    parser.add_argument('value', help='Calculate GST on amount')
    parser.add_argument(
        dest='mode',
        widget='Dropdown',
        choices=['add', 'subtract']
    )
    args = parser.parse_args()
    return args.mode, args.value



if __name__ == '__main__':
    main()
