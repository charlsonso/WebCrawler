#avoid crawling the internet, crawl only pages apart of the domain
#https: the protocol
#thenewboston.com the network location
#/hello.txt files on the location
from urllib.parse import urlparse

# Get domain name(example.com)
def get_domain_name(url):
	try:
		results = get_sub_domain_name(url).split('.')
		return results[-2]+ '.' +results[-1]
	except:
		return ''



# Get subdomain name(name.example.com)

def get_sub_domain_name(url):
	try:
		return urlparse(url).netloc
	except:
		return ''

print(get_domain_name('https://thenewboston.com/index.php')
	