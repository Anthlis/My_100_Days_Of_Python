#!python3
#pull_xml.py uses the requests module to pull down the feed xml file for use in the xml parser script.
#This will result in just one call/request to the Steam webserver hosting this XML file.

import requests
import url_feeds

#URL = "https://www.stuff.co.nz/rss/"
#URL1 = 'https://www.rnz.co.nz/rss/pacific.xml'
#URL2 = 'http://rss.nzherald.co.nz/rss/xml/nzhrsscid_000000005.xml'
#URL3 = 'https://www.rbnz.govt.nz/feeds/news'
## careful with RP - no title
#URL4 = 'https://realpython.com/atom.xml'
#URL5 = 'https://pybit.es/feeds/all.rss.xml'
#URL6 = 'http://feeds.macrumors.com/MacRumors-All'
#URL7 = 'https://9to5mac.com/feed/'
#URL8 = 'https://stackabuse.com/rss/'
#URL9 = 'http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/front_page/rss.xml'
#URL10 = 'https://www.yahoo.com/news/rss/'
#URL11 = 'http://www.huffingtonpost.co.uk/feeds/index.xml'
#URL12 = 'http://feeds.feedburner.com/TechCrunch/'
#URL13 = 'https://www.nasa.gov/rss/dyn/shuttle_station.rss'
#URL14 = 'https://www.nasa.gov/rss/dyn/aeronautics.rss'
#URL15 = 'https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss'
#URL16 = 'https://www.nasa.gov/rss/dyn/breaking_news.rss'


if __name__ == "__main__":
    #url_feeds()
    r = requests.get(url_feeds.get_index(), verify=False)
    with open('newreleases.xml', 'wb') as f:
        f.write(r.content)