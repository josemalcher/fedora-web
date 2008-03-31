import os
import cPickle
import feedparser

def feedparse(url):
    feeds = dict()
    # TODO: Should the directory be hardcoded like this? 
    # Maybe use ConfigParser to get some stuff?
    cachefile = os.path.join(os.getcwd(), 'build/rss.cache')
    if os.path.isfile(cachefile):
        f = open(cachefile)
        feeds = cPickle.load(f)
        f.close()
    if not url in feeds:
        feeds[url] = feedparser.parse(url)
        f = open(cachefile, 'w')
        cPickle.dump(feeds, f)
        f.close()
    return feeds[url]

