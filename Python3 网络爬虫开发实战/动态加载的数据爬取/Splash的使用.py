# Splash API调用
# render.html
# import requests
#
# url = 'http://localhost:8050/render.html?url=https://www.baidu.com&wait=5'
# response = requests.get(url)
# print(response.text)

# render.png
import requests

url = "http://localhost:8050/render.png?url=https://www.jd.com&wait5&width=1000&height=700"
response = requests.get(url)
with open('jd.png', 'wb') as f:
    f.write(response.content)

# render.jpeg

# render.har
import requests

url = "http://localhost:8050/render.har?url=https://www.jd.com&wait5"
response = requests.get(url)
print(response.text)

# render.json
# curl http://localhost:8050/render.json?url=https://httpbin.org
# curl http://localhost:8050/render.json?url=https://httpbin.org&html=1&har=1

# execute
import requests
from urllib.parse import quote

lua = """
function main(splash)
    return 'hello'
end
"""

url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)

import requests
from urllib.parse import quote

lua = """
function main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("http://httpbin.org/get")
        return {
            html=treat.as_string(response.body),
            url=response.url,
            status=response.status
        }
    end    
"""

url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)
