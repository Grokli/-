# requests设置代理
# http代理
import requests

proxy = '183.47.40.35:8088'
# 如果代理需要认证，则
# proxy = 'username:password@183.47.40.35:8088'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)

# socks5代理
import requests

proxy = '183.47.40.35:8088'
proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)

import requests
import socks
import socket

socks.set_default_proxy(socks.SOCKS5, '183.47.40.35', 8088)
socket.socket = socks.socksocket
try:
    response = requests.get('http://httpbin.org/get')
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)

# selenium代理设置
# from selenium import webdriver
#
# proxy = '183.47.40.35:8088'
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=http://' + proxy)
# browser = webdriver.Chrome(chrome_options=chrome_options)
# browser.get('http://httpbin.org/get')
#
# # selenium认证代理设置
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import zipfile
#
# ip = '183.47.40.35'
# port = 8088
# username = 'foo'
# password = 'bar'
#
# manifest_json = """
# {
#     "version":"1.0.0",
#     "manifest_version": 2,
#     "name":"Chrome Proxy",
#     "permissions":[
#         "proxy",
#         "tabs",
#         "unlimitedStorage",
#         "storage",
#         "<all_urls>",
#         "webRequest",
#         "webRequestBlocking"
#     ],
#     "background":{
#         "scripts":["background.js"]
#     }
# }
# """
#
# background_js = """
# var config = {
#         mode:"fixed_servers",
#         rules:{
#             singleProxy:{
#                 scheme:"http",
#                 host:"%(ip)s",
#                 port:%(port)s
#             }
#         }
#     }
#
# chrome.proxy.settings.set({value:config,scope:"regular"},function(){});
# function callbackFn(details){
#     return {
#         authCredentials:{
#             username: "%(username)s",
#             password: "%(password)s"
#         }
#     }
# }
# chrome.webRequest.onAuthRequired.addListener(
#         callbackFn,
#         {urls:["<all_urls>"]},
#         ['blocking']
# )
# """ %{'ip':ip, 'port':port,'username':username,'password':password}
#
# plugin_file = 'proxy_auth_plugin.zip'
# with zipfile.ZipFile(plugin_file,'w') as zp:
#     zp.writestr("manifest.json",manifest_json)
#     zp.writestr("background.js",background_js)
# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_extension(plugin_file)
# browser = webdriver.Chrome(chrome_options=chrome_options)
# browser.get('http://httpbin.org/get')

# PhantomJS代理设置
from selenium import webdriver

service_args = [
    '--proxy=183.47.40.35:8088',
    '--proxy-type=http',
    '--proxy-auth=username:password'
]
browser = webdriver.PhantomJS(service_args=service_args)
browser.get('http://httpbin.org/get')
print(browser.page_source)
