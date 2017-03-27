import urllib.request
result = urllib.request.urlopen("http://www.google.com").read()
print(result)