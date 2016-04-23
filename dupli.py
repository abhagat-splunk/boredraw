f = open("brand_url_v2.txt","r")
g = open("brands_lol.txt","w")
x = []
for line in f:
	x.append(line)
x = sorted(list(set(x)))
for line in x:
	g.write(line)
f.close()
g.close()		