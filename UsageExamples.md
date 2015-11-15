# Introduction #

Some basic usage examples


# Details #

## Show help and all options available. (This output will be different between versions) ##
```
ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -h
Usage: urldigger.py [options] arg. -h to show HELP, version=urldigger.py-02b

Options:
  -h, --help            show this help message and exit

  Commands:
    -G, --googhot       show hot searchs from google. [default 20].
    -H, --hot           get hot urls from alexa. [default 20].
    -m, --malwaredomains
                        show malicious urls from malwaredomains.com page.
    -T, --twitter       show hot topics from twitter main page.
    -U, --googhoturls   get urls from google trends. Use with caution due to
                        it return thoushands of urls.
    -W, --twitthoturls  get urls from twitter hot words. Use with caution due
                        to it return thoushands of urls.
    -X, --alexaspam     look for common SPAM words in the alexa top URLs.
    -u, --ulimit        no limit in the number of search url gets from google
                        with '-g option'.
    -b, --brute         show the max url numbers from all options availables.
    -t, --test          only for internal tests. Do not use

  Options:
    -a COUNTRY, --alexa=COUNTRY
                        get urls from alexa top sites with selected country
                        (EN, ES) [default 20].
    -f FILE, --file=FILE
                        search in urls results from terms in file.
    -F FILEURL, --fileurl=FILEURL
                        show urls from search terms of the file.
    -g TERM, --goog=TERM
                        get urls with search term=term from google [default
                        50].
    -p PHISHING, --phishing=PHISHING
                        look if the site checked is a phished site.
    -P PHISHINGSEARCH, --phishingsearch=PHISHINGSEARCH
                        look for phished sites in the result google search
                        urls.
    -s SPAM, --spam=SPAM
                        look for common SPAM words in the URL site.
    -S SPAMGOOGLE, --spamgoogle=SPAMGOOGLE
                        look for common SPAM words in the result google search
                        urls
    -n NUMBER, --num=NUMBER
                        specify number urls to get with 'option -a'
                        (20,40,60,.. 200). [default 20]
    -r URL, --rank=URL  show the alexa rank for these url.

  Output:
    -v, --verbose
```


## Show hot searches from google ##
```
ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -G
['mary kay letourneau', 'super 8', 'bethany benz', 'caviar from for the love of ray j', 'nevada unemployment', 'the temptations', 'frank lucas', 'national ice cream day', 'david ruffin', 'nascar schedule', 'billy joe tolliver', 'nyc triathlon', 'british open winners', 'slammin salmon', 'obama deception', 'louis oosthuizen', 'mark williams', 'hope floats', 'antwone fisher', 'top gear season 15 episode 4']
```

## Get hot urls from alexa ##
```
ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -H
http://news.yahoo.com/s/yblog_upshot/20100718/el_yblog_upshot/tea-party-group-expels-leader-for-clearly-offensive-blog-post
http://movies.yahoo.com/news/movies.ap.org/inception-earns-dreamy-reception-with-604m-ap
http://vitality.yahoo.com/video-second-act-jay-shafer-20910192
http://travel.yahoo.com/p-interests-35009923
http://lifestyle.msn.com/relationships/article.aspx?cp-documentid=24682705&GT1=32023
http://www.cnn.com/2010/POLITICS/07/18/tea.party.imbroglio/index.html?hpt=T1
http://mlb.mlb.com/video/play.jsp?content_id=10015643
http://www.huffingtonpost.com/2010/07/18/crista-flanagan-in-playbo_n_650338.html
http://www.amish-shah.com/life/how-to-be-a-gangster
http://sports.espn.go.com/nba/news/story?id=5390603
http://www.dailymail.co.uk/tvshowbiz/article-1295658/Mel-Gibson-leaves-States-selling-mansion-cut-price.html
http://sports.espn.go.com/nba/news/story?id=5390711
http://www.nydailynews.com/news/politics/2010/07/18/2010-07-18_tea_party_express_leader_mark_williams_expelled_over_colored_people_letter.html
http://contact.ebay.com/ws/eBayISAPI.dll
http://www.imdb.com/title/tt1375666/
http://www.bing.com/search?q=girl+dies+park+ride&form=msnhpm
http://www.breitbart.com/article.php?id=CNG.0cc4a694b9a5e1dfeb575b3343e2bc74.c51&show_article=1
http://www.breitbart.com/article.php?id=D9H1JP9G0&show_article=1
http://www.cnbc.com/id/38253735
http://www.foxnews.com/entertainment/2010/07/18/report-mel-gibson-planning-australia-ex-wife/?test=faces
```

## Show hot topics from twitter main page (twitter trends) ##
```
ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -T
['Felipe+Neto+preso', 'Nelson+Mandela', 'Jared+Leto', 'Alan+Carr', 'Premios+Juventud', 'yeahyousexybut', 'cuandoerani%C3%B1o', 'theyhatemebecause', 'Inception', 'Damned+United']
```

## search in urls results from terms in file ##
For example if you have a file named keys.txt with plenty of terms like [this](http://pandalabs.pandasecurity.com/wp-content/uploads/2010/07/key.txt)
You could look for common SPAM words or suspicious code on the results urls from these terms with:
```
ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -f keys.txt
Term: 'true blood season 3 episode 4 megavideo
'
Looking for SPAM in........http://worldvillage.com/truebloodseason3episode4megavideo
Looking for SPAM in........http://www.makli.com/true-blood-season-3-episode-4-megavideo-0047869/
Looking for SPAM in........http://www.poodlesnatcher.com/true-blood-season-3-episode-4-megavideo-6855/
Looking for SPAM in........http://www.usposttoday.com/true-blood-season-3-episode-4-megavideo-9-crimes/
Looking for SPAM in........http://www.24topnews.com/true-blood-season-3-episode-4-megavideo.html
Looking for SPAM in........http://www.tv.com/true-blood-season-3-episode-4-megavideo/webnews/112503.html
Looking for SPAM in........http://www.freepressindex.com/news-watch-true-blood-season-3-episode-4-megavideo-83182.html
Looking for SPAM in........http://www.nyissues.com/true-blood-season-3-episode-4-megavideo.html
Looking for SPAM in........http://ansamblu.com/true-blood-season-3-episode-4-megavideo-9-crimes.html
Looking for SPAM in........http://yourdigestbook.com/digest/true-blood-season-3-episode-4-megavideo.html
Looking for SPAM in........http://www.channelcut.com/true-blood-season3-episode4-9-crimes/
Looking for SPAM in........http://hubpages.com/hub/Watch-True-blood-season-3-episode-4-online-free-Megavideo-now
*Suspicious SPAM!!!-----> http://hubpages.com/hub/Watch-True-blood-season-3-episode-4-online-free-Megavideo-now ( ['iframe width="1" height="1"'] )*
Looking for SPAM in........http://mashakim.com/watch-true-blood-season-3-episode-4-9-crimes-free-online.htm
Looking for SPAM in........http://international.esan-today.com/watch-true-blood-season-3-episode-4-megavideo.html
Looking for SPAM in........http://watchtvshowmegavideo.com/true-blood-season-3-episode-4-9-crimes-megavideo/
^CLooking for SPAM in........http://vimeo.com/groups/54226
^CLooking for SPAM in........http://www.latestseasonepisode.com/true-blood-season-3-episode-4-9-crimes/
-----output CUT--------
```