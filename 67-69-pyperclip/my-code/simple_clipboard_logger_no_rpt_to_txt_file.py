import time
import pyperclip

old_word = ""
while(True):
    time.sleep(2)
    new_word=pyperclip.paste()
    with open("clippy_history.txt", "a") as f:
        if new_word != old_word:
            f.write(pyperclip.paste())
            f.write("\n")
            old_word=pyperclip.paste()