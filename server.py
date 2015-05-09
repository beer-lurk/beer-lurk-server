import sys
import scrape
from bottle import run as _run, route as _route
import query
import json
from sys import argv


if __name__ == "__main__":
    # prep data
    _posts = scrape.get_all_posts()

    # set up search route
    @_route('/find/<beer>')
    def find_stores(beer):
        # find the stores
        stores = query.find_beer(_posts, beer)

        # form API
        j = { 'beer_locations': [{ 'address_with_name': s } for s in stores] }

        # respond
        return json.dumps(j)
    
    # set up update route
    @_route('/update')
    def update_stores():
        global _posts
        _posts = scrape.get_all_posts(_posts) + _posts

    # run the server
    _run(host='0.0.0.0', port=argv[1])
