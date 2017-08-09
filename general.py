#Web Crawler for pulling urls to a file.

#import os allows us to create directories
import os

# Create a folder for our crawler
def create_project_dir(directory):
	#only create if path doesn't exist
	if not os.path.exists(directory):
		print('Creating Project Folder: ' + directory)
		os.makedirs(directory)

#Multithreading so it allows us to crawl 16 pages at once

#Create queue and crawled files (if not created)

def create_data_files(project_name, base_url):
	#name of file path, add slash to add file into folder
	queue = project_name + '/queue.txt'
	crawled = project_name + '/crawled.txt'
	#if this file does not exist yet, start from the home webpage and crawl
	if not os.path.isfile(queue):
		write_file(queue, base_url)
	#create a empty crawl file because if implement first then the program will think that its crawled already
	if not os.path.isfile(crawled):
		write_file(crawled,'')


# Create a new file
def write_file(path, data):
	#open file and write
	open_file = open(path, 'w')
	open_file.write(data)
	open_file.close()
	#frees up memory resources and saves buffer

#add data onto an existing file
def append_to_file(path, data):
	with open(path, 'a') as file:
		file.write(data+'\n')

# Delete the contents of a file
def delete_file_contents(path):
	with open(path, 'w'):
		#will delete all the contents of the file
		pass

# Read a file and convert each line to set items
def file_to_set(filename):
	results =set()
	#open and write text
	with open(filename, 'rt') as f:
		for line in f:
			for line in f:
				results.add(line.replace('\n',''))
	return results

# Iterate through a set, each item will be anew line in the file
def set_to_file(links, file):
	delete_file_contents(file)
	for link in sorted(links):
		append_to_file(file, link)


create_project_dir('thenewboston')
create_data_files('thenewboston','https://thenewboston.com/')




