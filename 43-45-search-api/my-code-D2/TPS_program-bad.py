'''
Once you display the results, ask the user if they want to view any of them
(use an index, ask for a number of the listed ones or use the episode ID returned from the service (e.g. 142)).

When they pick one, use the URL from the service response and open the users default web browser to that page.

Sounds complicated, in Python it's just:

import webbrowser
webbrowser.open(full_url, new=2)
'''



import TPS_api
from pprint import pprint
import webbrowser


def main():
    print(f'***************** SEARCH TALK PYTHON ************************')
    keyword = input('Keyword of title search: ').lower()
    print(f"You entered '{keyword}' to search for: ")
    results = TPS_api.search_talk_python(keyword)
    
    # pprint(results.get('results')[0]['title'])
    print(f"\n** There are {len(results)} searches for '{keyword}' found **\n")

    for number, r in enumerate(results, start=1):
        # print(f"{number}. (id={r.id}) {r.title}")
        # example string formatting: line_new = f'{word[0]:>12}  {word[1]:>12}  {word[2]:>12}'
        # https://stackoverflow.com/questions/8234445/python-format-output-string-right-alignment
        print(f"{number:>4}. Found in: {r.category:<11} | Podcast title:  {r.title}")
    
    print(f"\nDone! Found {len(results)} searches for '{keyword}'")
    value = input("\nEnter an index number of the podcast to open: ")
    print(f"You entered index value:", value)
    print()
    # https://duckduckgo.com/?q=returning+tuple+items+python&atb=v159-1&ia=web
    # https://stackoverflow.com/questions/354883/how-to-return-multiple-values-from-a-function#356695
    if 0 < int(value) <= len(results):
        print(f"The full API result for your chosen index is: \n", results[int(value)-1])
        get_specific_search_result = results[int(value)-1]
        print()
        print(f"The suffix URL obtained for your chosen index is: \n", get_specific_search_result.url)
        
        base_url = 'https://talkpython.fm'
        full_url = base_url + get_specific_search_result.url
        print(f"\nYour browser will now open: " + full_url)
        webbrowser.open(full_url, new=2)
    else:
        pass

if __name__ == '__main__':
    main()