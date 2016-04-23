from multiprocessing import Pool
import re,urllib
global list_of_all,visited

def crawl_ahead(URL):
	print "First"
	print URL
	sites_return = re.findall('''href=["'](.[^"']+)["']''',urllib.urlopen(URL).read(),re.I)
	print "Last"
	return sites_return


class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)




global list_of_all
list_of_all = []
visited = []
tovisit =[]
#URL = raw_input("Enter the domain:\n>")
f = open("brand_url_v2.txt","w")
g = open("Jabong_Clothing_Brands.txt","r")
for brand in g:
	try:
		print "Brand: ",brand
		URL = "http://www.jabong.com/"+brand.strip()+"/"
		print "URL: ",URL
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
	except MyError as e:
		print e
		print "Haha, lol skip karte hain"
		continue		#continue	
#find_URLS(sites_crawl)
	list_of_all = list(set(list_of_all))
	for x in list_of_all:
		f.write(x)
		f.write('\n')
	list_of_all = []
g.close()		
f.close()		