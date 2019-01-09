from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq

base_url = "https://www.zhihu.com/api/v3/feed/topstory/recommend?"

headers = {
    'referer': 'https://www.zhihu.com/',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'x-requested-with': 'fetch',
    'cookie': '_zap=99a901c7-4459-4afb-a03f-59eaa557abc3; d_c0="ANAgEYr4kw6PTrQalG5NH2vLyO1tW7fHsyA=|1543228324"; _xsrf=Nw1nAqqRjvYnjftgRCSXGvNSnePVQMXa; capsion_ticket="2|1:0|10:1543655785|14:capsion_ticket|44:ZjMzNmYyODU2NWNhNGY0MGFiMTUwMTZkZDQ0ZjlkNjY=|36b6d4ab55edfa99e2c5ae4430f56e3987813c1acc88f74b9d63ae6b303691db"; z_c0="2|1:0|10:1543655788|4:z_c0|92:Mi4xVzhhT0FBQUFBQUFBMENBUml2aVREaVlBQUFCZ0FsVk5iSl92WEFBRDhWVHZQLW9lWTFlTGRyUHYyN2JkOFZhTUp3|1ad764d3398b24ce9e94b436d824e87bad65e8e45a16068d1c617299839268e0"; tst=r; tgw_l7_route=b3dca7eade474617fe4df56e6c4934a3'
}

def get_page(page):
    params = {
        'session_token':'f178abf42a939b224484b65bd72b6a18',
        'desktop' : 'true',
        'limit' :'7',
        'action' : 'down',
        'after_id' : page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

def parse_page(json):
    if json:
        items = json.get('data')
        for item in items:
            item = item.get('target')
            zhihu = {}
            zhihu['question'] = item.get('question').get('title') if item.get('question') else None
            zhihu['author'] = item.get('author').get('name') if item else None
            zhihu['content'] = pq(item.get('content')).text() if item else None
            zhihu['comments'] = item.get('comment_count') if item else None
            yield zhihu

if __name__ == '__main__':
    i = 1
    for page in range(11):
        json = get_page(page * 7)
        results = parse_page(json)
        for result in results:
            print(result)
            i += 1
    print(i)

