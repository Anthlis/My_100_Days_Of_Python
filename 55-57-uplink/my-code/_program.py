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
    # response.raise_for_status()

    # This prints out "<class 'requests.models.Response'> <Response [200]>"
    # print(type(response), response)

    posts = response.json()

    # This prints out "{'imdb_code': 'tt2199571', 'title': 'Run All Night', 'director': 'Jaume ..."
    # print(posts.get('hits')[2])

    # This prints out the list of all the movie titles
    # for i in posts['hits']:
    #     print(i['title'])

    # This prints out an enumerated list of movie titles.
    print()
    for idx, p in enumerate(posts['hits'], 1):
        print(" {}. {}". format(idx, p['title']))
    print()




def write_post():
    pass


if __name__ == '__main__':
    main()

