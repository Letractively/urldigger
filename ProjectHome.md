## **NEWS!!, RELATED SERVICE AS WEBSITE** ##

Web Security Awareness; watch out your web infrastructure with:
[desenmascara.me](http://desenmascara.me)



---

## **URLDIGGER REFERENCES** ##
[Badware Busters](https://badwarebusters.org/main/resources) /
[Securitytube tools](http://securitytube-tools.net/index.php?title=Information_Gathering) /
[Secuobs](http://www.secuobs.com/revue/news/384407.shtml) /
[Usage demo in Youtube ](http://www.youtube.com/watch?v=reUQiYMD25w)

---



---

Urldigger (cazaurls in spanish) is an experimental script created to extract URL addresses from different sources and optionally check them for looking SPAM or malicious code. Currently working with Google, Twitter, Alexa and some malware sources. If the most popular web pages get compromised by [drive-by download attacks](http://en.wikipedia.org/wiki/Drive-by_download), can potentially infect a large population.
Extract high url lists to posterior analysis or whatever you are looking for in the need of processing high quantity of urls.

**Use case:** Viral trends like "nexus one, "ipad", "Michael Jackson" lead throughout the world with many people searching these words on the search engines. But this is just the kind of opportunity fraudsters like to exploit by poisoning search terms to direct people to compromised legitimate sites that may have nothing to with the subject matter at hand. If someone clicks on the link to a page on that infected site they are then redirected to a malicious site which can implant malware on their machine or tempt them to install a rogue security product.

Urldigger could help you to extract popular URLs and Scanning them with some of the [honeypot clients](http://en.wikipedia.org/wiki/Client_honeypot) availables by specifically searching for potentially malicious web sites.
[Download it.](http://urldigger.googlecode.com/files/urldigger-02c.tar.gz)


<br>
<a href='http://code.google.com/p/urldigger/wiki/WindowsUrldigger'>Howto execute urldigger on Windows</a>

<br>
<br>
<hr><br>
<br>
<br>
<br>
<b>EXAMPLES:</b>

<b>GET URLS FROM A GOOGLE SEARCH TERM</b>
<pre><code>ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -g urldigger
http://urldigger.com/
http://code.google.com/p/urldigger/
http://code.google.com/p/urldigger/updates/list
http://sniptools.com/vault/urldigger
http://www.urldigger.com/articles/81/asshole-of-the-year-nominee-abu-abdullah.html
----OUTPUT CUT-----
</code></pre>


<b>GET URLS FROM TWITTER HOT WORDS</b>
<pre><code>ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -W
http://itunes.apple.com/us/album/now-playing/id193558513
http://sourceforge.net/projects/nnplaying/
http://vivapinkfloyd.blogspot.com/2008/06/how-to-make-simple-amarok-now-playing.html
http://vivapinkfloyd.blogspot.com/2008/05/how-to-make-simple-amarok-now-playing.html
----OUTPUT CUT-----
</code></pre>

<b>GET URLS FROM CRAWLING YOUR SITE</b>
<pre><code>ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -c http://www.nasa.gov
http://www.nasa.gov/about/career/index.html
http://www.nasa.gov/about/highlights/bolden_bio.html
http://www.nasa.gov/about/highlights/garver_bio.html
http://www.nasa.gov/about/highlights/leadership_gallery.html
http://www.nasa.gov/about/org_index.html
http://www.nasa.gov/about/sites/index.html
http://www.nasa.gov/astronauts
----OUTPUT CUT-----
</code></pre>

<b>SHOW HOT URLS FROM ALEXA</b>
<pre><code>ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -H
http://realestate.yahoo.com/promo/most-expensive-us-small-town-sagaponack-ny.html
http://www.realsimple.com/home-organizing/new-uses-for-old-things/new-uses-penny-00000000027632/index.html?xid=yahoobuzz-rs-012210&amp;xid=yahoo
http://movies.yahoo.com/news/usmovies.thehollywoodreporter.com/forbes-lists-biggest-flops-last-five-years
http://health.yahoo.com/experts/drmao/23125/soup-therapy-detoxify-lose-weight-and-boost-immunity/
http://answers.yahoo.com/question/index?qid=20100111162407AATTvcJ
----OUTPUT CUT-----
</code></pre>

<b>BRUTE FORCE MODE</b>
<pre><code>ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -b &gt; allurls.txt
</code></pre>
Be careful, currently the output is about 18917 urls.<br>
<br>
<b>DETECT SPAM OR SPURIOUS CODE IN YOUR SITE</b>
<pre><code>ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -g "site:uclm.es"
Looking for SPAM in........http://publicaciones.uclm.es/
*Suspicious SPAM!!!-----&gt; http://publicaciones.uclm.es/* [(viagra)]
Looking for SPAM in........http://www.uclm.es/to/cdeporte/pdf/PublicacionesProfesorado.pdf
Looking for SPAM in........http://www.uclm.es/cr/caminos/publicaciones/publicaciones.html
Looking for SPAM in........http://www.uclm.es/profesorado/ricardo/Publicaciones.htm
Looking for SPAM in........http://publicaciones.uclm.es/index.php?action=module&amp;path_module=modules_Product_index
*Suspicious SPAM!!!-----&gt; http://publicaciones.uclm.es/index.php?action=module&amp;path_module=modules_Product_index*
Looking for SPAM in........http://www.uclm.es/PROFESORADO/mydiaz/_private/PUBLICACIONES.pdf
</code></pre>
<i><b>NOTE</b>: Functional code only available thorough the source in the repository.</i>


<hr />
For any question check out my blog at <a href='http://blog.emiliocasbas.com'>http://blog.emiliocasbas.com</a>