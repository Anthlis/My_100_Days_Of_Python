from movie_api import MovieSearchClient


def main():
    print_header()
    keyb_entry()


def print_header():
    print()
    print('----------------------------------------------')
    print('     MOVIE SEARCH USING UPLINK API')
    print('----------------------------------------------')
    print()


def keyb_entry():
    val = 'RUN'

    while val:
        print("What would you like to do next?")
        val = input('[s] to search movie by keyword, '
                    'or [d] to search by movie director, '
                    'or [i] to search by IMDB code, '
                    'or [q] to quit? ').lower()

        if val == 'q':
            print('\nExciting program now... bye.')
            break
        elif val == 'l':
            list_movies()
        elif val == 's':
            search_movie_key()
        elif val == 'd':
            search_director_key()
        elif val == 'i':
            continue
        else:
            print('OK, quitting anyway')
            break


def search_movie_key():
    print('\nKEYWORD MOVIE SEARCH >>> ')
    keyword_entry = input('Enter keyword to search movie by: ')
    svc = MovieSearchClient()
    response = svc.search_movies_by_keyword(keyword_entry)
    posts = response.json()
    print()
    for idx, p in enumerate(posts['hits'], 1):
        print(" {:4}. {} directed by {}".format(idx, p['title'], p['director']))
    print()
    return


def search_director_key():
    print('\nDIRECTOR MOVIE SEARCH >>> ')
    keyword_entry = input('Enter director to search movie by: ')
    svc = MovieSearchClient()
    response = svc.search_movies_by_director(keyword_entry)
    posts = response.json()
    print()

    # TODO This doesn't search by dictionary key! "director": "Tony Scott" properly. Tony found.
    for idx, p in enumerate(posts['hits'], 1):
        print(" {:4}. {} directed by {}".format(idx, p['title'], p['imdb_number']))
    print()
    return

def list_movies():
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
        print(" {:4}. {}". format(idx, p['title']))
    print()


def write_post():
    pass


if __name__ == '__main__':
    main()


# while True:
#
#
#     print(f'A {active_creature.name} of level {active_creature.level} '
#           f'has appeared from a dark and foggy forest...')
#
#     cmd = input('Do you [a]ttack, [r]unaway or [l]ookaround? ')
#     if cmd == 'a':
#         if hero.attack(active_creature):
#             creatures.remove(active_creature)
#         else:
#             print(f'The Wizard runs and hides taking time to recover....')
#             time.sleep(5)
#             print(f'The Wizard returns revitalized')
#
#     elif cmd == 'l':
#         print(f'The Wizard {hero.name} takes in the surroundings and sees: ')
#         for c in creatures:
#             print(f' * A {c.name} of level {c.level}')
#
#     elif cmd == 'r':
#         print('The Wizard has become unsure of its power and flees....')
#     else:
#         print('OK... exiting game')
#         break
#
#     if not creatures:
#         print(f'You have defeated all the creatures, well done!')
#         break
#
#     print()