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
<pre><code>ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -g urldigger<br>
http://urldigger.com/<br>
http://code.google.com/p/urldigger/<br>
http://code.google.com/p/urldigger/updates/list<br>
http://sniptools.com/vault/urldigger<br>
http://www.urldigger.com/articles/81/asshole-of-the-year-nominee-abu-abdullah.html<br>
----OUTPUT CUT-----<br>
</code></pre>


<b>GET URLS FROM TWITTER HOT WORDS</b>
<pre><code>ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -W<br>
http://itunes.apple.com/us/album/now-playing/id193558513<br>
http://sourceforge.net/projects/nnplaying/<br>
http://vivapinkfloyd.blogspot.com/2008/06/how-to-make-simple-amarok-now-playing.html<br>
http://vivapinkfloyd.blogspot.com/2008/05/how-to-make-simple-amarok-now-playing.html<br>
----OUTPUT CUT-----<br>
</code></pre>

<b>GET URLS FROM CRAWLING YOUR SITE</b>
<pre><code>ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -c http://www.nasa.gov<br>
http://www.nasa.gov/about/career/index.html<br>
http://www.nasa.gov/about/highlights/bolden_bio.html<br>
http://www.nasa.gov/about/highlights/garver_bio.html<br>
http://www.nasa.gov/about/highlights/leadership_gallery.html<br>
http://www.nasa.gov/about/org_index.html<br>
http://www.nasa.gov/about/sites/index.html<br>
http://www.nasa.gov/astronauts<br>
----OUTPUT CUT-----<br>
</code></pre>

<b>SHOW HOT URLS FROM ALEXA</b>
<pre><code>ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -H<br>
http://realestate.yahoo.com/promo/most-expensive-us-small-town-sagaponack-ny.html<br>
http://www.realsimple.com/home-organizing/new-uses-for-old-things/new-uses-penny-00000000027632/index.html?xid=yahoobuzz-rs-012210&amp;xid=yahoo<br>
http://movies.yahoo.com/news/usmovies.thehollywoodreporter.com/forbes-lists-biggest-flops-last-five-years<br>
http://health.yahoo.com/experts/drmao/23125/soup-therapy-detoxify-lose-weight-and-boost-immunity/<br>
http://answers.yahoo.com/question/index?qid=20100111162407AATTvcJ<br>
----OUTPUT CUT-----<br>
</code></pre>

<b>BRUTE FORCE MODE</b>
<pre><code>ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -b &gt; allurls.txt<br>
</code></pre>
Be careful, currently the output is about 18917 urls.<br>
<br>
<b>DETECT SPAM OR SPURIOUS CODE IN YOUR SITE</b>
<pre><code>ecasbas@cipher:~/proyectos/urldigger$ python urldigger.py -g "site:uclm.es"<br>
Looking for SPAM in........http://publicaciones.uclm.es/<br>
*Suspicious SPAM!!!-----&gt; http://publicaciones.uclm.es/* [(viagra)]<br>
Looking for SPAM in........http://www.uclm.es/to/cdeporte/pdf/PublicacionesProfesorado.pdf<br>
Looking for SPAM in........http://www.uclm.es/cr/caminos/publicaciones/publicaciones.html<br>
Looking for SPAM in........http://www.uclm.es/profesorado/ricardo/Publicaciones.htm<br>
Looking for SPAM in........http://publicaciones.uclm.es/index.php?action=module&amp;path_module=modules_Product_index<br>
*Suspicious SPAM!!!-----&gt; http://publicaciones.uclm.es/index.php?action=module&amp;path_module=modules_Product_index*<br>
Looking for SPAM in........http://www.uclm.es/PROFESORADO/mydiaz/_private/PUBLICACIONES.pdf<br>
</code></pre>
<i><b>NOTE</b>: Functional code only available thorough the source in the repository.</i>


<hr />
For any question check out my blog at <a href='http://blog.emiliocasbas.com'>http://blog.emiliocasbas.com</a>