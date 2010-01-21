#!/usr/bin/python

import os
import urllib2
import re
import optparse
#External dependency. Get it from http://www.catonmat.net/download/xgoogle.zip
from xgoogle.search import GoogleSearch, SearchError

################FUNCTIONS####################################
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


def alexa(country, n):
	if country in ('ES', 'EN'):
		if n > 1:
			num = calculateN(n)
			alexa_custom(country, num)
		else:
			alexa_custom(country, 1)
	else:
		print "Invalid country"


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


def alexaHOT():
	url = "http://www.alexa.com/hoturls"
	r = "<a class='offsite' href='(.*?)'>";

	for x, m in enumerate(re.findall(r, urllib2.urlopen(url).read())):
		print '%s' % (m)
	

#http://code.prashanthellina.com/code/get_alexa_rank.py
def get_alexa_rank(url):
	print 'Getting alexa rank for %s' % url
	data = urllib2.urlopen('http://data.alexa.com/data?cli=10&dat=snbamz&url=%s' % (url)).read()

	#regexp modified to accept domains with numbers
	popularity = re.findall("POPULARITY.*TEXT=\"(\d+)\"\/>",data)
	if popularity:
		popularity = popularity[0]
	print "%s esta en el ranking de alexa el: %s" % (url,popularity)


def show_alexa_data(url):
	print 'Getting alexa data for %s' % url	

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
			#print word
			words.append(word)

	print words

def search_twitts_google():
	hot_twitter()

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
				#print trend
	
	print trends
	
	
################END FUNCTIONS################################

	
def main():
    usage = "usage: %prog [options] arg"
    parser = optparse.OptionParser(usage)

    # Commands
    commands = optparse.OptionGroup(parser, "Commands")
    commands.add_option("-G", "--googhot", action="store_true",
			help="get hot searchs from google. [default 20]")
    commands.add_option("-H", "--hot", action="store_true",
			help="get hot urls from alexa. [default 20]")
    commands.add_option("-T", "--twitter", action="store_true",
			help="get hot topics from twitter main page.")
    commands.add_option("-u", "--ulimit", action="store_true",
                      help="no limit in the number of search url gets from google with '-g option'")
    commands.add_option("-b", "--brute", action="store_true",
                      help="show the max url numbers from all options availables")
    commands.add_option("-t", "--test", action="store_true",
                      help="only for internal tests. Do not use")
    parser.add_option_group(commands)


    # Options
    options = optparse.OptionGroup(parser, "Options")
    options.add_option("-a", "--alexa", dest="country", 
			help="get urls from alexa top sites with selected country (EN, ES). [default 20]")
    options.add_option("-g", "--goog", dest="term",
                      help="get urls with search term=term from google [default 50]")
    options.add_option("-n", "--num", dest="number", type="int",
                      help="specify number urls to get with 'option -a' (20,40,60,80,100,120). [default 20]")
    options.add_option("-r", "--rank", dest="url",
                      help="show the alexa rank for these url")
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
	print "by user (mail at user)"
	print
        parser.error("incorrect number of arguments")

    if options.verbose:
        print "reading %s..." % options.filename

    if options.country:
	if options.country == 'ES':
		if options.number:
			alexa("ES", options.number)
		else:
			alexa("ES", 1)
	elif options.country == 'EN':
		if options.number:
			alexa("EN", options.number)
		else: alexa("EN", 1)
	else: print 'country option: \'%s\' not valid' %options.country

    if options.hot:
	alexaHOT()

    if options.term:
	if options.ulimit:
		google(options.term)
	else: googledefault(options.term)

	# ranking
    if options.url:
	url = options.url
	get_alexa_rank(url)

    if options.brute:
	alexa("ES", 200)
	alexa("EN", 200)
	alexaHOT()

    if options.twitter:
	hot_twitter()

    if options.googhot:
	google_trends()

    if options.test:
	google_trends()



if __name__ == "__main__":
    main()

