#!python3
import feedparser
import webbrowser

# import pull_xml

FEED_FILE = "newreleases.xml"

feed = feedparser.parse(FEED_FILE)

if 'title' in feed.entries[0]:
    for index, entry in enumerate(feed.entries, start=1):
        # print(f"{index:<2}. " + entry.published + " - " + entry.title + ": " + entry.link)
        print(f"{index:<2}. " + entry.published + " - " + entry.title)
#       For RealPython use:
#       print(entry.title + ": " + entry.link +": " + entry.summary + "\n")

    
    value = input("\nEnter an index number of the web page you would like to read: ")
    print(f"You entered index value:", value)
    # https://duckduckgo.com/?q=returning+tuple+items+python&atb=v159-1&ia=web
    # https://stackoverflow.com/questions/354883/how-to-return-multiple-values-from-a-function#356695
    if 0 < int(value) <= len(feed.entries):
        get_specific_search_result = feed.entries[int(value)-1]
        print(f"Your browser will now open: " + get_specific_search_result.link)
        web_url = get_specific_search_result.link
        webbrowser.open(web_url, new=2)
    else:
        pass # TODO here?
# else here? 

#if __name__ == '__main__':
#    main()