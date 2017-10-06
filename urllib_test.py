from urllib.request import urlopen

response = urlopen('http://www.debian.org')
print(response.readline())
print(response.status)



