from typing import List

import requests
import collections
from pprint import pprint

Searches = collections.namedtuple('Searches', 'category, id, url, title, description')

def search_talk_python(keyword: str) -> List[Searches]:
    url = f'https://search.talkpython.fm/api/search?q={keyword}'
    
    print(url)
    
    resp = requests.get(url, verify=False)
    resp.raise_for_status()
    
    # print(resp.text)  # string only
    
    results = resp.json()
    # print(type(results), results)
    
    # pprint(results.get('results')[0]['title'])
    # pprint(results['title'])
    
    content = []
    for r in results.get('results'):
        content.append(Searches(**r))
    
    # print(type(content))
    return content