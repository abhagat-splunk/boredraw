import re,urllib
global list_of_all,visited

def crawl_ahead(URL):
	print "First"
	print URL
	sites_return = re.findall('''href=["'](.[^"']+)["']''',urllib.urlopen(URL).read(),re.I)
	print "Last"
	return sites_return

def find_URLS(sites_crawl):
	global list_of_all
	for x in sites_crawl:
		print x
		if 'Adidas' in x and '.html' in x:
			list_of_all.append(x)
		elif x[:12]=='/Adidas/color':
			print x
			returned_sites = crawl_ahead('http://www.jabong.com'+x)
			print "I am here in "+x+"\n"
			print returned_sites
			find_URLS(returned_sites)
		elif '?promotion' in x or 'voucherCode' in x or 'sports-jerseys' in x:
			continue
		elif x[:16]=='/Adidas/?gender=':
			print x
			if x not in visited:
				visited.append(x)
				returned_sites = crawl_ahead('http://www.jabong.com'+x)
				print "I am here in "+x+"\n"
				print returned_sites
				find_URLS(returned_sites)

global list_of_all
list_of_all = []
visited = []
#URL = raw_input("Enter the domain:\n>")
URL = "https://www.jabong.com/Adidas"
sites_crawl = crawl_ahead(URL)
find_URLS(sites_crawl)
list_of_all = list(set(list_of_all))
f = open("adidas.txt","w")
for x in list_of_all:
	f.write(x)
	f.write('\n')
f.close()	


'''/Adidas/?gender=Men
/Adidas/?gender=Women
/Adidas/?gender=Boys
/Adidas/?gender=Girls'''
