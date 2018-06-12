import requests
from bs4 import BeautifulSoup
import csv
x = 0
i = 0
urls = [
  'https://www.us-proxy.org/',
  'https://free-proxy-list.net/uk-proxy.html',
  'https://free-proxy-list.net/',
  'https://www.socks-proxy.net/',
  'https://www.sslproxies.org/',
  'https://free-proxy-list.net/anonymous-proxy.html',
]

for x in range(len(urls)):
    res = requests.get(urls[x] , headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(res.text,"lxml")
    for items in soup.select("tbody tr")[:-8]:
        proxy_list = ':'.join([item.text for item in items.select("td")[:2]])
        f = open('helloworld.txt', 'a')
        f.write(proxy_list+ '\n')
        print(proxy_list)
        i = i+1

#removing empty lines
with open('helloworld.txt') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output
print (i)
