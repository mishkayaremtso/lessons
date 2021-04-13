from urllib import request
import sys


url = "https://www.shutterstock.com/blog/wp-content/uploads/sites/5/2019/07/Man-Silhouette.jpg"
path = "/home/user/PycharmProjects/lessons/get_post/Man-Silhouette.jpg"

try:
    print("Download file from: " + url)
    request.urlretrieve(url, path)
except Exception:
    print("error")
    print(sys.exc_info()[1])
    exit

print("file downloaded")

