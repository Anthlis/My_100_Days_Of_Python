import collections
# test
# import webbrowser

Feed = collections.namedtuple(
    'Feed',
    'name, url, xml')

def get_url():
    data = [
        Feed('Stuff News', 'https://www.stuff.co.nz/rss/', 'stuffnews.xml'),
        Feed('MacRumors', 'http://feeds.macrumors.com/MacRumors-All', 'macrumors.xml'),
        Feed('BBC UK News', 'http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/front_page/rss.xml', 'bbcuk.xml')
        ]
    return data

def get_index():
    for i, idx in enumerate(get_url(), start=1):
        print(f"{i}. {idx.name}")
    url_feed_index = input("\nChoose the index number of the RSS feed to view: ")
    print(f"You entered index value: {idx.url}", idx.url)
    ### test will open url here
    #webbrowser.open(idx.url, new=2)
    #testurl = idx.url
#    
    if 0 < int(idx) <= len(idx):
        get_specific_search_result = idx.url[int(idx)-1]
        print(f"Your browser will now open: " + get_specific_search_result)
        #web_url = get_specific_search_result.link
        #webbrowser.open(web_url, new=2)
    else:
        pass # TODO here?
    
    return idx.url
    
        
if __name__ == '__main__':
    get_index()