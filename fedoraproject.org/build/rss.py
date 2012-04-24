import os
import cPickle
import feedparser

def feedparse(url):
    # TODO: Should the directory be hardcoded like this? 
    # Maybe use ConfigParser to get some stuff?
    feeds = [{}] 
    cachefile = os.path.join(os.getcwd(), 'build/rss.cache')
    if os.path.isfile(cachefile):
        f = open(cachefile)
        feeds = cPickle.load(f)
        f.close()

    # We parse the list
    for i in feeds:
        feed_url = i
        # and here the dictionary
        for j in feed_url:
           try:
               if j["url"] == url:
                   return j["feed"]   
           except KeyError:
               pass

    # Ok, the url was not in the cache, process it
    main_feed = dict()
    main_feed = feedparser.parse(url)
    entry = [{}]
    for feed in main_feed["entries"]:
        '''We only need to save the link, title and date of blog posts'''
        if "updated" in feed:
            entry.append({'link':feed["link"], 'title':feed["title"], 'date':feed["date"]})
        else:
            entry.append({'link':feed["link"], 'title':feed["title"], 'date':""})
    url_entries = [{}]
    url_entries.append({'url':url, 'feed':entry})
    feeds.append(url_entries)

    f = open(cachefile, 'w')
    cPickle.dump(feeds, f)
    f.close()
    feed_url = dict()
    return entry
