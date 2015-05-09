import json
import urllib

KEY = r'f9a98378-b97f-4ef8-a5e4-d9ec01ac110c%3A3VcrY4Nkm2OAg%2BOcknCmV00wDu1cdczgNLMzpBQzEHBDgRVflrrjqzD8hj3wN1orx81xb0En9%2BhcfqGTZBqlcQ%3D%3D'

def get_stats(posts, stats={}):
    for s in posts:
        words = re.sub(r'[,\.\-:\(\)\[\]]', '', s, re.UNICODE).replace('\n', ' ').split(' ')
        for w in words:
            if w not in stats:
                stats[w] = 1
            else:
                stats[w] += 1
    return stats

def get_posts(url):
    # form the request
    url = urllib.quote(url)
    request = r'https://api.import.io/store/data/868ddafc-971b-4581-8810-5bf5f428553e/_query?input/webpage/url=%s&_user=f9a98378-b97f-4ef8-a5e4-d9ec01ac110c&_apikey=%s' % (url, KEY)
    
    # load the data
    j = json.loads(urllib.urlopen(request).read())
    
    if 'results' not in j:
        raise Exception('No results: ', j)
    
    # fetch posts
    op = j['results'][0]['thead_value']
    posts = [r['alt1_content'] for r in j['results'] if r['thead_value'] == op]
    
    return posts

def find_beer(posts, beer):
    pass

def get_beer_stores(beer):
    pass

def test():
    posts = get_posts(r'http://www.browar.biz/forum/showthread.php?t=111581')
    stats = get_stats(posts)
    print sorted(stats.items(), key=lambda x: x[1])

