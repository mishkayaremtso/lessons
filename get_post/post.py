from urllib import request, parse
import sys

url = "http://www.google.com/search?"
val = {'q': 'SoftServe'}

headers = {}
headers['User-Agent'] ='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0'

try:
    data = parse.urlencode(val)
    print(data)
    url = url + data
    req = request.Request(url, headers=headers)
    ans = request.urlopen(req)
    ans = ans.readlines()
    for l in ans:
        print(l)
except Exception:
    print("Error :)")
    print(sys.exc_info()[1])
