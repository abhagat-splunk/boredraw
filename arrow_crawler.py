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
#URL = raw_input("Enter the domain:\n>")
URL = "http://www.jabong.com/men/clothing/formal-trousers/Arrow/"
sites_crawl = crawl_ahead(URL)
for x in sites_crawl:
	if '.html' in x:
		list_of_all.append(x)
	else:
		print x	
#find_URLS(sites_crawl)
list_of_all = list(set(list_of_all))
f = open("arrow.txt","w")
for x in list_of_all:
	f.write(x)
	f.write('\n')
f.close()		