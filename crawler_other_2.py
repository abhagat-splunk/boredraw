

import re,urllib
global list_of_all,visited

def crawl_ahead(URL):
	print "First"
	print URL
	sites_return = re.findall('''href=["'](.[^"']+)["']''',urllib.urlopen(URL).read(),re.I)
	print "Last"
	return sites_return





global list_of_all
list_of_all = []
visited = []
tovisit =[]
#URL = raw_input("Enter the domain:\n>")
URL = "http://www.jabong.com/Arrow/"
sites_crawl = crawl_ahead(URL)
find_after_this = 'javascript:window.open('
for x in xrange(len(sites_crawl)):
	if '.html' in sites_crawl[x]:
		list_of_all.append(sites_crawl[x])
	elif sites_crawl[x]==find_after_this:
		tovisit.extend(sites_crawl[x+1:-1])
for x in tovisit:
	lol = crawl_ahead(x)
	for y in lol:
		if '.html' in y:
			list_of_all.append(y)			
print tovisit
#find_URLS(sites_crawl)
list_of_all = list(set(list_of_all))
f = open("arrow.txt","w")
for x in list_of_all:
	f.write(x)
	f.write('\n')
f.close()		
