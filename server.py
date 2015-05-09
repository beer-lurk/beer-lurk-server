import sys
import scrape
from bottle import run as _run, route as _route
import query
import json


# prep data
_posts_per_store = scrape.get_all_posts()

# config the server
@_route('/find/<beer>')
def find_stores(beer):
    # find the stores
    stores = query.find_beer(_posts_per_store, beer)
    
    # form API
    j = { 'beer_locations': [{ 'address_with_name': s } for s in stores] }
    
    # respond
    return json.dumps(j)

# run the server
_run(host='0.0.0.0', port=8080)
