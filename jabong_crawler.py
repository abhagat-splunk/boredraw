import re,urllib

def crawl_ahead(URL):
	return re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(URL).read(),re.I)


URL = raw_input("Enter the domain:\n>")
sites_crawl = crawl_ahead(URL)
print sites_crawl
f = open("Jabong_Clothing_Brands.txt","a")
for x in sites_crawl:
	if x[0]=='/':
		x = x.split("/")
		if x[1]=='clothing':
			f.write(x[2])
			f.write("\n")
f.close()			

f = open("Jabong_Shoes_Brands","a")
for x in sites_crawl:
	if x[0]=='/':
		x = x.split("/")
		if x[1]=='shoes':
			f.write(x[2])
			f.write("\n")
f.close()			


f = open("Jabong_Beauty_Brands","a")
for x in sites_crawl:
	if x[0]=='/':
		x = x.split("/")
		if x[1]=='beauty':
			f.write(x[2])
			f.write("\n")
f.close()


f = open("Jabong_Jewellery_Brands","a")
for x in sites_crawl:
	if x[0]=='/':
		x = x.split("/")
		if x[1]=='jewellery':
			f.write(x[2])
			f.write("\n")
f.close()


f = open("Jabong_Bags_Brands","a")
for x in sites_crawl:
	if x[0]=='/':
		x = x.split("/")
		if x[1]=='bags':
			f.write(x[2])
			f.write("\n")
f.close()

f = open("Jabong_Home-Furniture_Brands","a")
for x in sites_crawl:
	if x[0]=='/':
		x = x.split("/")
		if x[1]=='home-furniture':
			f.write(x[2])
			f.write("\n")
f.close()

f = open("Jabong_Sports_Brands","a")
for x in sites_crawl:
	if x[0]=='/':
		x = x.split("/")
		if x[1]=='sports':
			f.write(x[2])
			f.write("\n")
f.close()

f = open("Jabong_Toys_Brands","a")
for x in sites_crawl:
	if x[0]=='/':
		x = x.split("/")
		if x[1]=='toys':
			f.write(x[2])
			f.write("\n")
f.close()

print "Done, Check please."