from movie_api import MovieSearchClient


def main():
    val = 'RUN'

    while val:
        print("What would you like to do next?")
        val = input('[w]rite a post or [r]ead them all?')

        if val == 'w':
            write_post()
        elif val == 'r':
            read_post()


def read_post():
    svc = MovieSearchClient()
    response = svc.all_entries()
    response.raise_for_status()

    print(type(response), response)

    posts = response.json()

    print(posts.get('hits')[2])

    for i in posts['hits']:
        print(i['title'])


    print()
    for idx, p in enumerate(posts['hits'], 1):
        print(" {}. {}". format(idx, p['title']))
    print()




def write_post():
    pass


if __name__ == '__main__':
    main()