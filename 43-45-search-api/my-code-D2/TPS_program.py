import TPS_api
from pprint import pprint
import webbrowser

# TODO PyTest
# TODO Logging


def main():
    print(f'***************** SEARCH TALK PYTHON ************************')
    keyword = input('Keyword of title search: ').lower()
    # TODO test for something forms of entry (just enter, mixed alphanumeric nonsense etc)
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
    # TODO use a try/except/finally block here
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
    # TODO deal with exceptions

if __name__ == '__main__':
    main()