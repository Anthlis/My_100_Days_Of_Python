import pyperclip

AFFILIATE_CODE = '&tag=pyb0f-20'

url = pyperclip.paste()

if 'amazon' not in url:
    print('Sorry, invalid link.')
else:
    new_link = url + AFFILIATE_CODE
    # Needs improvement here to stop this: https://www.amazon.com/&tag=pyb0f-20&tag=pyb0f-20&tag=pyb0f-20
    pyperclip.copy(new_link)
    print('Affiliate link generated > copied to the clipboard now!')
    print(f"new_link = {new_link}")