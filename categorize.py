import os,re
f = open("Jabong_Clothing_Brands_Unique.txt","r")
li = f.readlines()
tempfile = "broadcategorize.txt"
for line in li:
	try:
		g = open(tempfile,"a")
		line  = line.strip()
		final_url = "www.jabong.com/"+line
		print final_url
		q = 'wget '+final_url
		os.system(q)
		h = open(line.strip(),"r")
		li_h = h.readlines()
		x = li_h[6]
		indexes = [m.start() for m in re.finditer('<a href="/', x)]
		index = []
		for y in xrange(len(indexes)-1):
			if indexes[y+1]-indexes[y]<500:
				index.append(indexes[y])
		cat = []
		for q in xrange(len(index)-1):
			check = x[index[q]+9:index[q+1]]
			ind = check.find('"')
			final_check = x[index[q]+9:index[q]+9+ind]
			cat.append(final_check)
		print cat
		g.write(line)
		g.write(":")
		for l in cat:
			g.write(l)
			g.write(',')
		g.write('\n')
		g.close()
		os.system("rm "+line)
	except Exception,e:
		print str(e)
		os.system("rm "+line)
		continue	
