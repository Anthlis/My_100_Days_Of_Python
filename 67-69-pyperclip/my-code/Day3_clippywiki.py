import time
import pyperclip
import wikipedia
import subprocess

old_word = ""

while True:
    time.sleep(2)
    new_word = pyperclip.paste()
    if new_word != old_word:
        # print(pyperclip.paste())
        search_word = pyperclip.paste()
        wiki_str = wikipedia.summary(search_word, sentences=2)
        script = '\ndisplay dialog "Wikipedia found:   \n\n ' + wiki_str + '"¬\nwith title "Clipboard Wikipedia Search For: ' + search_word + '" ¬\nwith icon caution ¬\nbuttons {"OK"}\n'
        subprocess.call("osascript -e '{}'".format(script), shell=True)
        old_word = pyperclip.paste()