from urllib.request import urlopen
from linkFinder import LinkFinder
from general import *



class Spider:

	# Class variables (shared among all instances)
	project_name = ''
	#if the link is rel, then this will help it be the full one
	base_url = ''
	domain_name = ''
	#saved on compuer
	queue_path = ''
	crawled_path = ''
	#saved on memory
	queue_set = set()
	crawled_set = set()
	#any spider can set the value of these

	#base_url: google.com/IMAGES IMAGES is the base url
	#domain_name: google.com is the domain name
	def __init__(self, project_name, base_url, domain_name):
		Spider.project_name = project_name
		Spider.base_url = base_url
		Spider.domain_name = domain_name
		Spider.queue_path = Spider.project_name+'/queue.txt'
		Spider.crawled_file = Spider.project_name +'/crawled.txt'
		self.boot()
		#connect to webpage
		#name of thread, and then page its crawling during prompt
		self.crawl_page('First spider', Spider.base_url)

	@staticmethod
	def boot():
		create_project_dir(Spider.project_name)
		create_data_files(Spider.project_name, Spider.base_url)
		Spider.queue = file_to_set(Spider.queue_path)
		Spider.crawled = file_to_set(Spider.crawled_file)

	@staticmethod
	def crawl_page(thread_name,page_url):
		if page_url not in Spider.crawled_set:
			print(thread_name + ' crawling '+ page_url)
			print('Queue '+str(len(Spider.queue)+' | Crawled '))
			Spider.add_links_to_queue(Spider.gather_link(page_url))
			Spider.queue_set.remove(page_url)
			Spider.crawled_set.add(page_url)
			Spider.update_files()

	@staticmethod
	def gather_links(page_url):
		html_string = ''
			try:
				response=urlopen(page_url)
				if response.getheader('Content-Type')=='text/html'
					html_bytes = response.read()
					html_string = html_bytes.decode("utf-8")
				finder = LinkFinder(Spider.base_url, page_url)
				finder.feed(html_string)
			except:
				print('Error: can not crawl page')
				return set()
			return finder.page_links()

	@staticmethod
	def add_links_to_queue(links):
		for url in links:
			#if already in queue or crawled skip
			if url in Spider.queue:
				continue
			if url in Spider.crawled:
				continue
			if Spider.domain_name not in url:
				continue
			Spider.queue.add(url)

	@staticmethod
	def update_files():
		set_to_file(Spider.queue_set, Spider.queue_path)
		set_to_file(Spider.crawled_set, Spider.crawled_path)

