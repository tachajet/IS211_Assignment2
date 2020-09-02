def downloadData(url):
	import urllib2
	with urllib.request.urlopen(url) as response:
		webdata=response.read()
