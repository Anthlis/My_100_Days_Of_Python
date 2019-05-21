import TPS_api
from pprint import pprint


def main():
    print(f'***************** SEARCH TALK PYTHON ************************')
    keyword = input('Keyword of title search: ').upper()
    print(f"You entered '{keyword}' to search for: ")
    results = TPS_api.search_talk_python(keyword)
    
    pprint(results.get('results')[0]['title'])
    
    for item in results:
        print(item)
    
    
    # for x in results:
      #  pprint(('results')[0]['category'])
        
    '''    
    for i in data['routes'][0]['legs'][0]['steps']:
    lattitude = i['start_location']['lat']
    longitude = i['start_location']['lng']
    print('{}, {}'.format(lattitude, longitude))'''
    
    
    
    # for r in results:
    #    print(f"Title: {results.get('results')['title']}")
     
    # print(f'There are {len(results)} search results found.')
    '''    
    for r in results:
        print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
    
    
    for item in results:
        print(item.get('id'))
        
'''
       
    
if __name__ == '__main__':
    main()

'''
{'elapsed_ms': 0.9909999999999999,
 'keywords': ['test'],
 'results': [{'category': 'Transcript',
              'description': 'Writing good, clean code and having a deep '
                             'working knowledge of Python is critical to your '
                             'success as a Python developer. But if you look '
                             'at those who have truly excelled in their '
                             "career, it's often because they bring something "
                             'in addition to coding skills.',
              'id': 71,
              'title': "Soft Skills: The software developer's life manual ",
              'url': '/episodes/transcript/71/soft-skills-the-software-developer-s-life-manual'},
             {'category': 'Episode',
              'description': 'There has been a bunch of new Python web '
                             'frameworks coming out in the past few years. '
                             'Generally, these have been focused solely on '
                             "Python 3 and have tried to leverage Python's new "
                             'async and await features.',
                             
                             '''
