from typing import List

import requests
import collections

Searched = collections.namedtuple('Searched', 'category, id, url, title, description')


def search_talk_python(keyword: str) -> List[Searched]:
    url = f'https://search.talkpython.fm/api/search?q={keyword}'

    resp = requests.get(url)
    resp.raise_for_status()

    results = resp.json()

    content = []
    for r in results.get('results'):
        content.append(Searched(**r))

    return content