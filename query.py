import json
import re


def find_beer(posts_per_store, beer):
    stores = []
    beer = re.escape(beer)
    
    def _find_in_posts(store, posts):
        for p in posts:
            # remember the store if it mentioned the beer in any post
            num = len(re.findall(beer, p, flags=re.IGNORECASE))
            if num > 0:
                stores.append(store)
                return
    
    for store, posts in posts_per_store.iteritems():
        _find_in_posts(store, posts)
        
    return stores
                

def get_beer_stores(beer):
    pass
