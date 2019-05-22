import api


def main():
    print(f"\n************** Search Talk Python *************\n")
    keyword = input('Enter search term to look for: ').lower()
    results = api.search_talk_python(keyword)
    print(f"You searched for '{keyword}'.")

    print(f'\n<<< There are {len(results)} results found. >>>\n')
    for i, r in enumerate(results, start=1):
        print(f"{i}: {r.title}")


if __name__ == '__main__':
    main()
