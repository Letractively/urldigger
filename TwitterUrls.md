# Look spam and suspicious code in twitter publictimeline #

Added SQLITE support


# Details #

urldigger.db: sqlite3 database (1 table)

In order to use the **show-twitter-urls.py** function

```
    $ cat urldigger.db.dump | sqlite3 urldigger.db
```

http://www.sqlite.org/sqlite.html