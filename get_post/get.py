from urllib import request

url = "https://github.com/mishkayaremtso"

req = request.urlopen(url)

text = req.readlines()
text1 = req.read()

print(req)
print(text1)

for l in text:
    print(l)