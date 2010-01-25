#!/usr/bin/python

# Distributed under MIT license:
#
# Copyright (c) 2010 Emilio Casbas

# CONTRIBUTORS
# Clemens Kurtenbach

#
# Permission is hereby granted, free of charge, to any person
# Obtaining a copy of this software and associated documentation
# Files (the "Software"), to deal in the Software without
# Restriction, including without limitation the rights to use,
# Copy, modify, merge, publish, distribute, sublicense, and/or sell
# Copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# Conditions:
#
# The above copyright notice and this permission notice shall be
# Included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
#

import os
import urllib2
import re
import optparse
import thread
from time import sleep, ctime
#External dependency. Get it from http://www.catonmat.net/download/xgoogle.zip
from xgoogle.search import GoogleSearch, SearchError

def googledefault(termtosearch):
	try:
	  gs = GoogleSearch(termtosearch)
	  gs.results_per_page = 50
	  results = gs.get_results()
	  for res in results:
	    print res.url.encode('utf8')
	except SearchError, e:
	  print "Search failed: %s" % e


def google(termtosearch):
	try:
	  gs = GoogleSearch(termtosearch)
	  gs.results_per_page = 100
	  results = []
	  while True:
	    tmp = gs.get_results()
	    if not tmp:
	      break
	    results.extend(tmp)
	  for res in results:
	    print res.url.encode('utf8')
	except SearchError, e:
	  print "Search failed: %s" % e	


def alexa(country, n, lock):
	if country in ('ES', 'EN'):
		if n > 1:
			num = calculateN(n)
			alexa_custom(country, num)
		else:
			alexa_custom(country, 1)
	else:
		print "Invalid country"

	if lock != None:
		lock.release()


def calculateN(n):
	if n == 20:
		return(1)
	elif n == 40:
		return(2)
	elif n == 60:
		return(3)
	elif n == 80:
		return(4)
	elif n == 100:
		return(5)
	elif n == 120:
		return(6)
	elif n == 140:
		return(7)
	elif n == 160:
		return(8)
	elif n == 180:
		return(9)
	elif n == 200:
		return(10)
	
	# Default return 2 -> 20 results
	else: return(2)


def alexa_custom(country, num):

	# Alexa has been trying to obfuscate their HTML pages to prevent scrapping.
	# Maybe this code stops to work in a few time.
	#regex to catch domains in alexa
	r = '<a  href="/siteinfo/(.*?)"  ><strong>(.*?)</strong>';	

	if (country == "EN" and num == 1):
		alexaEN(num)
	else:
		if (country == "EN"):
			for i in range(num):
				url ="http://www.alexa.com/topsites/global;%d" %i
				for x, m in enumerate(re.findall(r, urllib2.urlopen(url).read())):
					print '%s' % (m[0])
		else:
			url = "http://www.alexa.com/topsites/countries/%s" %country
			if num == 1:
				for x, m in enumerate(re.findall(r, urllib2.urlopen(url).read())):
					print '%s'  % (m[0])
			else:
				for i in range(num):
					#TODO: Customize code country
					u = "http://www.alexa.com/topsites/countries;%d/ES" %i
					for x, m in enumerate(re.findall(r, urllib2.urlopen(u).read())):
						print '%s' %(m[0])
			


def alexaEN(num):
	url ="http://www.alexa.com/topsites/global"
	r = '<a  href="/siteinfo/(.*?)"  ><strong>(.*?)</strong>';	

	for x, m in enumerate(re.findall(r, urllib2.urlopen(url).read())):
		print '%s' % (m[0])


def alexaHOT(lock):
	url = "http://www.alexa.com/hoturls"
	r = "<a class='offsite' href='(.*?)'>";

	for x, m in enumerate(re.findall(r, urllib2.urlopen(url).read())):
		print '%s' % (m)

	if lock != None:
		lock.release()
	

def get_alexa_rank(url):
	print 'Getting alexa rank for %s' % url
	data = urllib2.urlopen('http://data.alexa.com/data?cli=10&dat=snbamz&url=%s' % (url)).read()

	#regexp modified from -http://code.prashanthellina.com/code/get_alexa_rank.py- to accept domains with numbers
	popularity = re.findall("POPULARITY.*TEXT=\"(\d+)\"\/>",data)
	if popularity:
		popularity = popularity[0]
	print "%s esta en el ranking de alexa el: %s" % (url,popularity)


def hot_twitter():
	url = "http://search.twitter.com/"
	r = "(\/intra\/trend/(.*?)')";
	words = []

	for x, m in enumerate(re.findall(r, urllib2.urlopen(url).read())):
		word = m[1]
		if word[:3] == "%23":
			word = word.replace("%23", "")
			#print '%s' % (word)
			words.append(word)
		else:
			words.append(word)

	return words


def urls_hot_twitter():
	#manual exclusion
	nowatch = ['nowplaying','Goodnight'] 
	twitt = []
	a = hot_twitter()
	for i, w in enumerate(a):
		if w not in nowatch:
			google(w)


def google_trends():
	trends = []
	user_agent = 'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; en-US)'

	search = "http://www.google.com/trends/hottrends"

	req = urllib2.Request(search)
	req.add_header('User-Agent', user_agent)	

	try:
		response = urllib2.urlopen(req)
	except urllib2.HTTPError, e:
		print "Error ", e.code, search
		sys.exit()

	lines = response.readlines()
	
	for line in lines:
		if line.find("trends/hottrends") != -1:
			#cut line until trends/hottrends
			line = line[line.find("trends/hottrends"):]
			#trend begins after <
			line = line[line.find(">")+1:]
			#trends ends before >
			trend = line[:line.find("<")]
	
			#print trend	
			if len(trend) > 0 and trend[1] != " " and trend != "Site Feed":
				trends.append(trend)
	
	return trends


#Take care using the following function. 
#If running this option you see something similar to "Search failed: Failed getting 
#http://www.google.com/search?hl=en&q=jersey=Google+Search: HTTP Error 503: Service Unavailable
#then: http://www.google.com/support/websearch/bin/answer.py?answer=86640
#http://googleonlinesecurity.blogspot.com/2007/07/reason-behind-were-sorry-message.html
def urls_google_trends():
	a = google_trends()
	for i,w in enumerate(a):
		google(w)
	
	
#############################################################################################
	
def main():
    usage = "usage: %prog [options] arg. -h to show HELP"
    parser = optparse.OptionParser(usage)

    # Commands
    commands = optparse.OptionGroup(parser, "Commands")
    commands.add_option("-G", "--googhot", action="store_true",
			help="show hot searchs from google. [default 20].")
    commands.add_option("-H", "--hot", action="store_true",
			help="get hot urls from alexa. [default 20].")
    commands.add_option("-T", "--twitter", action="store_true",
			help="show hot topics from twitter main page.")
    commands.add_option("-U", "--googhoturls", action="store_true",
                      help="get urls from google trends. Use with caution due to it return thoushands of urls.")
    commands.add_option("-W", "--twitthoturls", action="store_true",
                      help="get urls from twitter hot words. Use with caution due to it return thoushands of urls.")
    commands.add_option("-u", "--ulimit", action="store_true",
                      help="no limit in the number of search url gets from google with '-g option'.")
    commands.add_option("-b", "--brute", action="store_true",
                      help="show the max url numbers from all options availables.")
    commands.add_option("-t", "--test", action="store_true",
                      help="only for internal tests. Do not use")
    parser.add_option_group(commands)

    # Options
    options = optparse.OptionGroup(parser, "Options")
    options.add_option("-a", "--alexa", dest="country", 
			help="get urls from alexa top sites with selected country (EN, ES) [default 20].")
    options.add_option("-g", "--goog", dest="term",
                      help="get urls with search term=term from google [default 50].")
    options.add_option("-n", "--num", dest="number", type="int",
                      help="specify number urls to get with 'option -a' (20,40,60,.. 200). [default 20]")
    options.add_option("-r", "--rank", dest="url",
                      help="show the alexa rank for these url.")
    parser.add_option_group(options)

    # Output
    output = optparse.OptionGroup(parser, "Output")
    output.add_option("-v", "--verbose",
                      action="store_true", dest="verbose")
    output.add_option("-q", "--quiet",
                      action="store_false", dest="verbose")
    parser.add_option_group(output)

    (options, args) = parser.parse_args()

    if len(args) == 1:
	print "URL digger services (extract urls from websites)"
	print "by ecasbas (ecasbas at gmail.com)"
	print
        parser.error("incorrect number of arguments")

	#TODO: implement to show function actions in the output
    if options.verbose:
        print "reading %s..." % options.filename

    if options.country:
	if options.country == 'ES':
		if options.number:
			alexa("ES", options.number, None)
		else:
			alexa("ES", 1)
	elif options.country == 'EN':
		if options.number:
			alexa("EN", options.number)
		else: alexa("EN", 1)
	else: print 'country option: \'%s\' not valid' %options.country

    if options.hot:
	alexaHOT(None)

    if options.term:
	if options.ulimit:
		google(options.term)
	else: googledefault(options.term)

	# ranking
    if options.url:
	url = options.url
	get_alexa_rank(url)

	# Be careful with this option. Took about 9 min in my laptop (without threads!)
	# TODO: Multithread processing with Threading module
    if options.brute:
	locks = []
	loops = 3
	for i in range(loops):
		lock = thread.allocate_lock()
		lock.acquire()
		locks.append(lock)

	for i in range(loops):
		thread.start_new_thread(alexa, ( "ES", 200, locks[i]))
		thread.start_new_thread(alexa, ("EN", 200, locks[i]))
		thread.start_new_thread(alexaHOT, (locks[i],))

	for i in range(loops):
		while locks[i].locked(): pass

	#urls_google_trends()
	#urls_hot_twitter()	

    if options.twitter:
	av = hot_twitter()
	print av

    if options.googhot:
	av = google_trends()
	print av

    if options.googhoturls:
	urls_google_trends()

    if options.twitthoturls:
	av = urls_hot_twitter()
	print av

    if options.test:
	av = urls_hot_twitter()
	print av



if __name__ == "__main__":
    main()
