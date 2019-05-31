from collections import Counter

text = "I took my feedparser app from yesterday and improved it to allow the user to choose from a number of pre-determined list of RSS feeds (or exit), and then have it check if the cached file needed updating or not based on the HTTP header's Etag. Seems to work well!".split()

#words = text.replace("'", '')
#words = text.replace('.', '')
word_count = Counter(text)

print(word_count)
 
print(word_count.values())

list = word_count.values()

sum = 0
for i in list:
    sum += i

print(sum)
    