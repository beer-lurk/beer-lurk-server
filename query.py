import json
import re


def find_beer(all_posts, beer):
    stores = []
    beer = re.escape(beer)
    
    def _find_in_posts(store, posts):
        for p in posts:
            # remember the store if it mentioned the beer in any post
            num = len(re.findall(beer, p, flags=re.IGNORECASE))
            if num > 0:
                stores.append(store)
                return
    
    for store, url, posts in all_posts:
        _find_in_posts(store, posts)
        
    return stores
