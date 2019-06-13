import time
import pyperclip

old_word = ""
while(True):
    time.sleep(2)
    new_word=pyperclip.paste()
    if new_word != old_word:
        print(pyperclip.paste())
        old_word=pyperclip.paste()