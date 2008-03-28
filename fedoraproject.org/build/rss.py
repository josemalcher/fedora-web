import os
import cPickle
import feedparser

# TODO: This fetches once for every build.py run.  Need to make it
# cache the results (pickle?) and delete after a full website build.  

def feedparse(url):
    feeds = dict()
    cachefile = os.path.join(os.getcwd(), 'build/rss.cache')
    if os.path.isfile(cachefile):
        f = open(cachefile)
        feeds = cPickle.load(f)
        f.close()
    if not feeds.has_key(url):
        feeds[url] = feedparser.parse(url)
        f = open(cachefile, 'w')
        cPickle.dump(feeds, f)
        f.close()
    return feeds[url]

