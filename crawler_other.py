import re,urllib
global list_of_all
global visited
def crawl_ahead(URL):
	print URL
	find_URLS(re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(URL).read(),re.I))

def find_URLS(brand_name,sites_crawl):
	global list_of_all
	global visited
	for x in sites_crawl:
		try:
		#print x
			if brand_name in x and '.html' in x:
				list_of_all.append(x)
			elif 'm.jabong.com' in x:
				continue
			elif x=='http://www.jabong.com/'+brand_name+'/':
				continue
			elif '?promotion' in x or 'voucherCode' in x or 'sports-jerseys' in x or 'price' in x:
				continue								
			elif '/'+brand_name+'/?' in x:
				print x
				if x not in visited:
					visited.append(x)
					crawl_ahead('http://www.jabong.com'+x)
		except:
			print "Andar wala error"
			continue

global list_of_all
list_of_all = []
visited = []
string = '/?gender=Men,/?gender=Women,/?gender=Boys,/?gender=Girls,/color-Black/,/color-Grey/,/color-Navy Blue/,/color-Blue/,/color-White/,/color-Green/,/color-Red/,/color-Orange/,/color-Pink/,/color-Black/,/color-Grey/,/color-Navy Blue/,/color-Blue/,/color-White/,/color-Green/,/color-Red/,/color-Orange/,/color-Pink/,/color-Yellow/,/color-Multi/,/color-Purple/,/color-Maroon/,/color-Olive/,/color-Silver/,/color-Brown/,/color-Peach/,/color-Tan/,/color-Off White/,/color-Khaki/,/color-Assorted/,'
add_url = string.split(',')
g = open("Jabong_Clothing_Brands.txt","r")
'''for brand in g:
	for x in add_url:
		try:
			crawl_ahead('https://www.jabong.com/'+brand.strip()+x)
		except:
			print "Bahar error!"'''
for x in add_url:
	crawl_ahead('https://www.jabong.com/shoes'+x)				
list_of_all = list(set(list_of_all))	
f = open("shoes.txt","w")
for x in list_of_all:
	f.write(x)
	f.write('\n')
f.close()			