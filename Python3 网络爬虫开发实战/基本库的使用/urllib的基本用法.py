import urllib.request

response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

#data参数
import urllib.parse

data = bytes(urllib.parse.urlencode({"word":"hello"}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

# timeout参数

# response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# print(response.read())

import urllib.error
import socket

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

# Request模块的使用
from urllib import request, parse
url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Host':'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
#req = request.Request(url=url, data=data, method='POST')
#req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
response = request.urlopen(req)
print(response.read().decode('utf-8'))