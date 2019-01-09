# 文件上传

import requests

files = {'file':open('favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)

# Cookies
import requests

r = requests.get('https://www.baidu.com')
print(r.cookies)
for key,value in r.cookies.items():
    print(key + '=' + value)

headers = {
    'Cookie':'_ga=GA1.2.446772569.1528874557; _octo=GH1.1.880934807.1528874557; user_session=3oLY9pOw1pmc_EOtQnePFoWiaOc1OiSn9pBu2AaCkx7XC6v0; __Host-user_session_same_site=3oLY9pOw1pmc_EOtQnePFoWiaOc1OiSn9pBu2AaCkx7XC6v0; logged_in=yes; dotcom_user=Grokli; has_recent_activity=1; tz=Asia%2FShanghai; _gh_sess=SkkvZ3h0eHgvZ092ZmpMK2FkR3pBWTBJSEdYbVlTelZUd3l6aUxWZGlPMDhzWVdTb1A2TFZEUU5jamRiaXVyR2tXTlZxa2d4cEwvcWcrT3kra09TYUg1RndIQ3NLWXBVVDdRaTRwQXpJRlZkOFJmanh0dzNjL2JNMnZFN1p6RzBSQ1RiTHQ3RFVxVmtaQitnV0R5dWF3PT0tLWJaWTVJV1REVktNMzU1NklGVVlSZVE9PQ%3D%3D--714dfd459f9fd9d12a1f92b26ad52d0264c4478d',
    'Host': 'github.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
r = requests.get('https://github.com/', headers=headers)
print(r.text)

cookies = "_ga=GA1.2.446772569.1528874557; _octo=GH1.1.880934807.1528874557; user_session=3oLY9pOw1pmc_EOtQnePFoWiaOc1OiSn9pBu2AaCkx7XC6v0; __Host-user_session_same_site=3oLY9pOw1pmc_EOtQnePFoWiaOc1OiSn9pBu2AaCkx7XC6v0; logged_in=yes; dotcom_user=Grokli; has_recent_activity=1; tz=Asia%2FShanghai; _gh_sess=SkkvZ3h0eHgvZ092ZmpMK2FkR3pBWTBJSEdYbVlTelZUd3l6aUxWZGlPMDhzWVdTb1A2TFZEUU5jamRiaXVyR2tXTlZxa2d4cEwvcWcrT3kra09TYUg1RndIQ3NLWXBVVDdRaTRwQXpJRlZkOFJmanh0dzNjL2JNMnZFN1p6RzBSQ1RiTHQ3RFVxVmtaQitnV0R5dWF3PT0tLWJaWTVJV1REVktNMzU1NklGVVlSZVE9PQ%3D%3D--714dfd459f9fd9d12a1f92b26ad52d0264c4478d"
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host': 'github.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r = requests.get('https://github.com/', cookies=jar, headers=headers)
print(r.text)

# 会话维持
import requests

requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)

# SSL证书验证
import requests

response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

# 忽略警告
import requests
from requests.packages import urllib3

urllib3.disable_warnings()
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

import logging

logging.captureWarnings(True)
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

# response = requests.get('https://www.12306.cn', cert=('/path/server.crt','/path/key'))
# print(response.status_code)

# 代理设置

# import requests
#
# proxies = {
#     'http':'http://10.10.1.10:3128',
#     'https':'http://10.10.1.10:1080'
# }
# requests.get('https://www.taobao.com', proxies=proxies)

# HTTP Basic Auth

# import requests
#
# proxies = {"http": "http://user:password@10.10.1.10:3128/"}
# requests.get('https://www.taobao.com', proxies=proxies)
#
# import requests
#
# proxies = {'http':'socks5://user:password@host:port',
#            'https':'socks5://user:password@host:port'}
# requests.get('https://www.taobao.com', proxies=proxies)

# 超时设置
import requests

r = requests.get('https://www.taobao.com', timeout=1)
print(r.status_code)

r = requests.get('https://www.taobao.com', timeout=(11, 30))
print(r.status_code)

# 身份认证
import requests
from requests.auth import HTTPBasicAuth

r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
print(r.status_code)

r = requests.get('http://localhost:5000', auth=('username', 'password'))
print(r.status_code)

import requests
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET','USER_OAUTH_TOKEN','USER_OAUTH_TOKEN_SECRET')
requests.get(url,auth=auth)

# Prepared Request
from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name':'germey'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)