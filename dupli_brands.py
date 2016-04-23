f = open("Jabong_Clothing_Brands.txt","r")
g = open("Jabong_Clothing_Brands_Unique.txt","w")
x = []
for line in f:
	x.append(line)
x = list(set(x))
for line in x:
	g.write(line)
f.close()
g.close()		