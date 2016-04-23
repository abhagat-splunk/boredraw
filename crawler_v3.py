from multiprocessing import Process,Queue,Lock
import re,urllib,os
global list_of_all,visited

#Find HTML Files in the Source Code.
def crawl_ahead(URL):
	#print "First"
	#print URL
	sites_return = re.findall('''href=["'](.[^"']+)["']''',urllib.urlopen(URL).read(),re.I)
	#print "Last"
	return sites_return


#Printing the exception if any occurs.
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


#Function to Find new URLs and Add them to the list.
def FindAndAddURLS(brand,q):
	tovisit = []
	try:
		info(brand)
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
		#print tovisit
		#print list_of_all
		q.put(list_of_all)
	except MyError as e:
		print e
		print "Haha, lol skip karte hain"

#Display information about the process ID(PID)
def info(title):
    print "Brand: ",title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()


#Main Function.
def main():
	global list_of_all
	list_of_all = []
	visited = []
	#URL = raw_input("Enter the domain:\n>")
	f = open("brand_url_v2.txt","w")
	g = open("Jabong_Clothing_Brands.txt","r")
	readFile = g.readlines()
	for ind in xrange(0,len(readFile),4):
		q = Queue()
		print readFile[ind:ind+4]
		p = []
		p1 = Process(target=FindAndAddURLS, args=(readFile[ind],q,))
		p2 = Process(target=FindAndAddURLS, args=(readFile[ind+1],q,))
		p3 = Process(target=FindAndAddURLS, args=(readFile[ind+2],q,))
		p4 = Process(target=FindAndAddURLS, args=(readFile[ind+3],q,))
		p = [p1,p2,p3,p4]
		list_of_all_URLS = []
		for processes in p:
			processes.start()
			list_of_all_URLS.extend(q.get())
		for processes in p:
			processes.join()	
		print len(list_of_all_URLS)
		print "FINALALALALALALALALALA"
		print list_of_all_URLS
		#list_of_all = FindAndAddURLS(brand)
		for x in list_of_all_URLS:
				f.write(x)
				f.write('\n')
		#list_of_all = []
	g.close()		
	f.close()

if __name__=='__main__':
	main()			