import wikipedia
import subprocess

search_word = 'internet'

wiki_str = wikipedia.summary(search_word, sentences=2)


script = '\ndisplay dialog "Wikipedia found:   \n\n ' + wiki_str + '"¬\nwith title "Clipboard Wikipedia Search For: '+ search_word +'" ¬\nwith icon caution ¬\nbuttons {"OK"}\n'
subprocess.call("osascript -e '{}'".format(script), shell=True)


