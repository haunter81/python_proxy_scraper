import requests
from bs4 import BeautifulSoup
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
#scraping links from urls
for x in range(len(urls)):
    res = requests.get(urls[x] , headers={'User-Agent':'Mozilla/5.0'}) #fetching urls and setting user-agent
    soup = BeautifulSoup(res.text,"lxml")
    for items in soup.select("tbody tr")[:-8]:  #mark -8 removes the broken lines from scrape
        proxy_list = ':'.join([item.text for item in items.select("td")[:2]])  # grabing and joining the first 2 rows
        f = open('helloworld.txt', 'a') #writing to a file , not the final output due to empty lines
        f.write(proxy_list+ '\n')
        print(proxy_list)
        i = i+1 # for debug and statistical reasons
#removing empty lines
with open('helloworld.txt') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output
print (i)
