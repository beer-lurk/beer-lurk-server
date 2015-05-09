import json
import urllib
import re

KEY = r'f9a98378-b97f-4ef8-a5e4-d9ec01ac110c%3A3VcrY4Nkm2OAg%2BOcknCmV00wDu1cdczgNLMzpBQzEHBDgRVflrrjqzD8hj3wN1orx81xb0En9%2BhcfqGTZBqlcQ%3D%3D'


def get_posts_in_thread(url):
    # form the request
    url = urllib.quote(url)
    request = r'https://api.import.io/store/data/868ddafc-971b-4581-8810-5bf5f428553e/_query?input/webpage/url=%s&_user=f9a98378-b97f-4ef8-a5e4-d9ec01ac110c&_apikey=%s' % (url, KEY)
    
    # load the data
    j = json.loads(urllib.urlopen(request).read())
    
    if 'results' not in j:
        raise Exception(j)
    
    # fetch posts
    op = j['results'][0]['thead_value']
    posts = [r['alt1_content'] for r in j['results'] if r['thead_value'] == op]
    
    return posts

def get_all_posts(except_these=[]):
    get_url = lambda page: urllib.quote(r'http://www.browar.biz/forum/forumdisplay.php?f=301&order=desc&page=%d' % page)
    posts = []
    
    # read several pages of threads
    threads = []
    print 'Fetching threads form the forum...'
    for i in range(5):
        # form the request
        request = r'https://api.import.io/store/data/b721eb59-3521-4306-bfdb-0186331065b8/_query?input%2Fwebpage%2Furl=' + get_url(1 + i) + '&_user=1e0a40f7-1454-4a5b-9214-e506d77db942&_apikey=' + KEY

        # load the data
        j = json.loads(urllib.urlopen(request).read())
        threads += j['results']
    num_threads = len(threads)
    print '...done (%d threads)' % num_threads

    # fetch all links and posts
    except_these = [x[1] for x in except_these]  # urls only
    for idx, r in enumerate(threads):
        name = r['shop/_text']
        url = r['shop']
        
        if url in except_these:
            continue
            
        print 'Fetching %d of %d...' % (1 + idx, num_threads)
        try:
            posts.append((name, url, get_posts_in_thread(url)))
            print '...done'
        except Exception as e:
            print '  FAILED:', e

    return posts
