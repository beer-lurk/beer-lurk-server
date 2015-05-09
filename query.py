import json
import re


def find_beer(posts_per_store, beer):
    stores = []
    
    def _find_in_posts(store, posts):
        for p in posts:
            # remember the store if it mentioned the beer in any post
            if re.findall(re.escape(beer), p) > 0:
                stores.append(store)
                return
    
    for store, posts in posts_per_store.iteritems():
        _find_in_posts(store, posts)
                
    return stores
                

def get_beer_stores(beer):
    pass
