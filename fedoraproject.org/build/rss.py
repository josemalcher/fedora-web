import feedparser

# TODO: This fetches once for every build.py run.  Need to make it
# cache the results (pickle?) and delete after a full website build.  
def feedparse(url):
    return feedparser.parse(url)

