#Post-Crawler Work.
import re,urllib,os
from lxml import etree, html
f = open("brands_lol.txt","r")
urls = f.readlines()

for URL in urls:
	URL = "http://www.jabong.com"+URL
	#line_return = re.findall('''<meta property="og:image" content="''',urllib.urlopen(URL).read(),re.I)
	#os.system("wget "+URL+" >trial.txt")
	response = urllib.urlopen(URL)
	htmlresp = response.read()
	document_root = html.fromstring(htmlresp)
	pretty_html = etree.tostring(document_root, encoding='unicode', pretty_print=True)
	total_len = len(pretty_html)
	toFindInsideData = '''<script type="text/javascript">var globalConfig = {'''
	if toFindInsideData in pretty_html:
		start_index = pretty_html.index(toFindInsideData)
		for x in xrange(start_index,total_len):
			if pretty_html[x]=="}" and pretty_html[x+1]==";":
				end_index = x+1
				break
	data = pretty_html[start_index:end_index]
	keyValues = data.split(',')
	for x in keyValues:
		print x
	