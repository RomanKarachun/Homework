# The final task of Roman Karachun (WITH EXAMPLES)

## Introduction to Python. Final task.
You are proposed to implement Python RSS-reader using python 3.9.

The task consists of few iterations. Do not start new iteration if the previous one is not implemented yet.
## Common requirements.
+ It is mandatory to use argparse module.

+ Codebase must be covered with unit tests with at least 50% coverage.

+ Yor script should not require installation of other services such as mysql server, postgresql and etc. (except Iteration 6). If it does require such programs, they should be installed automatically by your script, without user doing anything.

+ In case of any mistakes utility should print human-readable. error explanation. Exception tracebacks in stdout are prohibited in final version of application.

+ Docstrings are mandatory for all methods, classes, functions and modules.

+ Code must correspond to pep8 (use pycodestyle utility for self-check).

+ You can set line length up to 120 symbols.

+ Commit messages should provide correct and helpful information about changes in commit. Messages like Fix bug, Tried to make workable, Temp commit and Finally works are prohibited.
## [Iteration 1] One-shot command-line RSS reader.
```shell
C:\Users\user\rss>rss_reader.py "https://news.yahoo.com/rss/" --limit 1
Feed: Yahoo News - Latest News & Headlines
Description: The latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.
URL: https://news.yahoo.com/rss/

Title: Colombia's most wanted drug lord captured in jungle raid
Date: 2021-10-23T23:32:33Z
Image: https://s.yimg.com/uu/api/res/1.2/sbSt9k2i59Ne3T5Dahi7dg--~B/aD0xNTAwO3c9MjAwMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/1fc569ce977352662b4cf3039acae975
Read more: https://news.yahoo.com/colombia-announces-capture-one-most-233233294.html


```
Utility should provide the following interface:
```shell
usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT]
                     source

Pure Python command-line RSS reader.

positional arguments:
  source         RSS URL

optional arguments:
  -h, --help     show this help message and exit
  --version      Print version info
  --json         Print result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limit news topics if this parameter provided

```

In case of using `--json` argument your utility should convert the news into [JSON](https://en.wikipedia.org/wiki/JSON) format.
You should come up with the JSON structure on you own and describe it in the README.md file for your repository or in a separate documentation file.
```
C:\Users\user\rss>python rss_reader.py "https://news.yahoo.com/rss/" --json  --limit 2
{
 "Channel": {
  "Title": "Yahoo News - Latest News & Headlines",
  "Description": "The latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.",
  "URL": "https://news.yahoo.com/rss/"
 },
 "News 1": {
  "Title": "Colombia's most wanted drug lord captured in jungle raid",
  "Date": "2021-10-23T23:32:33Z",
  "Image": "https://s.yimg.com/uu/api/res/1.2/sbSt9k2i59Ne3T5Dahi7dg--~B/aD0xNTAwO3c9MjAwMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/1fc569ce977352662b4cf3039acae975",
  "Description": "",
  "Link": "https://news.yahoo.com/colombia-announces-capture-one-most-233233294.html"
 },
 "News 2": {
  "Title": "Ex-soldiers offered mercenaries $10,000 a week to join a private army that would fight in Yemen's civil war, prosecutors says",
  "Date": "2021-10-24T08:42:47Z",
  "Image": "https://s.yimg.com/uu/api/res/1.2/kQBZ_Uosy0S_VK_YxOmh_Q--~B/aD0xODQ3O3c9MjQ2MzthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/business_insider_articles_888/9f640b033bb7d3be557ddc77f9f3c04a",
  "Description": "",
  "Link": "https://news.yahoo.com/ex-soldiers-offered-mercenaries-10-084247990.html"
 }
}


```
With the argument `--verbose` your program should print all logs in stdout.
```
C:\Users\user\rss>rss_reader.py "https://news.yahoo.com/rss/" --verbose  --limit 2
INFO: 24.10.2021 15:05:09 - RSS channel 'Yahoo News - Latest News & Headlines' found
INFO: 24.10.2021 15:05:09 - 2 news items processed
WARNING: 24.10.2021 15:05:09 - No date provided or wrong date format in news 'Colombia's most wanted drug lord captured in jungle raid'. Date set to '19000101'.
WARNING: 24.10.2021 15:05:09 - No date provided or wrong date format in news 'Ex-soldiers offered mercenaries $10,000 a week to join a private army that would fight in Yemen's civil war, prosecutors says'. Date set to '19000101'.
INFO: 24.10.2021 15:05:09 - 0 news items saved to cache. 2 news items already in cache.
INFO: 24.10.2021 15:05:09 - Data converted to text string

Feed: Yahoo News - Latest News & Headlines
Description: The latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.
URL: https://news.yahoo.com/rss/

Title: Colombia's most wanted drug lord captured in jungle raid
Date: 2021-10-23T23:32:33Z
Image: https://s.yimg.com/uu/api/res/1.2/sbSt9k2i59Ne3T5Dahi7dg--~B/aD0xNTAwO3c9MjAwMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/1fc569ce977352662b4cf3039acae975
Read more: https://news.yahoo.com/colombia-announces-capture-one-most-233233294.html

Title: Ex-soldiers offered mercenaries $10,000 a week to join a private army that would fight in Yemen's civil war, prosecutors says
Date: 2021-10-24T08:42:47Z
Image: https://s.yimg.com/uu/api/res/1.2/kQBZ_Uosy0S_VK_YxOmh_Q--~B/aD0xODQ3O3c9MjQ2MzthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/business_insider_articles_888/9f640b033bb7d3be557ddc77f9f3c04a
Read more: https://news.yahoo.com/ex-soldiers-offered-mercenaries-10-084247990.html

```

### Task clarification (I)

1) If `--version` option is specified app should _just print its version_ and stop.
2) User should be able to use `--version` option without specifying RSS URL. For example:
```
> C:\Users\user\rss>rss_reader.py --version
"Version 1.5"

```
3) The version is supposed to change with every iteration.
4) If `--limit` is not specified, then user should get _all_ available feed.
5) If `--limit` is larger than feed size then user should get _all_ available news.
6) `--verbose` should print logs _in the process_ of application running, _not after everything is done_.
7) Make sure that your app **has no encoding issues** (meaning symbols like `&#39` and etc) when printing news to _stdout_.
8) Make sure that your app **has no encoding issues** (meaning symbols like `&#39` and etc) when printing news to _stdout in JSON format_.
9) It is preferrable to have different custom exceptions for different situations(If needed).
10) The `--limit` argument should also affect JSON generation.

## [Iteration 2] Distribution.

* Utility should be wrapped into distribution package with `setuptools`.
* This package should export CLI utility named `rss-reader`.


### Task clarification (II)
 
1) User should be able to run your application _both_ with and without installation of CLI utility,
meaning that this should work:

```
> C:\Users\user\rss>python rss_reader.py "https://news.yahoo.com/rss/" --limit 1

Feed: Yahoo News - Latest News & Headlines
Description: The latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.
URL: https://news.yahoo.com/rss/

Title: Colombia's most wanted drug lord captured in jungle raid
Date: 2021-10-23T23:32:33Z
Image: https://s.yimg.com/uu/api/res/1.2/sbSt9k2i59Ne3T5Dahi7dg--~B/aD0xNTAwO3c9MjAwMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/1fc569ce977352662b4cf3039acae975
Read more: https://news.yahoo.com/colombia-announces-capture-one-most-233233294.html


```

as well as this:  

```
> C:\Users\user\rss>rss_reader.py "https://news.yahoo.com/rss/" --limit 1

Feed: Yahoo News - Latest News & Headlines
Description: The latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.
URL: https://news.yahoo.com/rss/

Title: Colombia's most wanted drug lord captured in jungle raid
Date: 2021-10-23T23:32:33Z
Image: https://s.yimg.com/uu/api/res/1.2/sbSt9k2i59Ne3T5Dahi7dg--~B/aD0xNTAwO3c9MjAwMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/1fc569ce977352662b4cf3039acae975
Read more: https://news.yahoo.com/colombia-announces-capture-one-most-233233294.html


```
2) Make sure your second iteration works on a clean machie with python 3.9. (!)
3) Keep in mind that installed CLI utility should have the same functionality, so do not forget to update dependencies and packages.


## [Iteration 3] News caching.
The RSS news should be stored in a local storage while reading. The way and format of this storage you can choose yourself.
Please describe it in a separate section of README.md or in the documentation.

New optional argument `--date` must be added to your utility. It should take a date in `%Y%m%d` format.
For example: `--date 20191020`
Here date means actual *publishing date* not the date when you fetched the news.

The cashed news can be read with it. The new from the specified day will be printed out.
If the news are not found return an error.

If the `--date` argument is not provided, the utility should work like in the previous iterations.

### Task clarification (III)
1) Try to make your application crossplatform, meaning that it should work on both Linux and Windows.
For example when working with filesystem, try to use `os.path` lib instead of manually concatenating file paths.
2) `--date` should **not** require internet connection to fetch news from local cache.
3) User should be able to use `--date` without specifying RSS source. For example:
```
> C:\Users\user\rss>python rss_reader.py "https://news.yahoo.com/rss/" --date 20211023

Cached news items for date 'October 23, 2021'

Title: The story of Carol and Karen: Two experimental Facebook accounts show how the company helped divide America
Channel: Yahoo News - Latest News & Headlines
Channel URL: https://news.yahoo.com/rss/
Date: 2021-10-23T08:00:10Z
Detail: 2021-10-23 08:00:10
Read more: https://s.yimg.com/uu/api/res/1.2/4SS3v7Hgt9GDo.0tfbndHQ--~B/aD0zNzcxO3c9NDM0ODthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/usa_today_tech_153/6f11e68ab704af3b5cc338fa9cc52aa7

Title: Rep. Eric Swalwell Shares Chilling Voicemail Sent To Him By Tucker Carlson Fan
Channel: Yahoo News - Latest News & Headlines
Channel URL: https://news.yahoo.com/rss/
Date: 2021-10-23T07:08:33Z
Detail: 2021-10-23 07:08:33
Read more: https://s.yimg.com/uu/api/res/1.2/MhcXwchBo0tsDS4ZXYpxoA--~B/aD02MDA7dz05NTg7YXBwaWQ9eXRhY2h5b24-/https://media.zenfs.com/en/the_huffington_post_584/b6435d8564a57bf5392dabe3b8e44df6

Title: Email shows Loudoun superintendent knew of bathroom sexual assault on same day
Channel: Yahoo News - Latest News & Headlines
Channel URL: https://news.yahoo.com/rss/
Date: 2021-10-23T03:11:00Z
Detail: 2021-10-23 03:11:00
Read more: https://s.yimg.com/uu/api/res/1.2/V8W1bGMQJFADxHiXa_C.Nw--~B/aD05NDA7dz0xNTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/washington_examiner_articles_265/934f042c03f4154c4c135a36b1f24a34

Title: Jake Tapper Says Rep. Marjorie Taylor Greene Has 'Issues' After Her Rant On Bannon Vote
Channel: Yahoo News - Latest News & Headlines
Channel URL: https://news.yahoo.com/rss/
Date: 2021-10-23T01:46:34Z
Detail: 2021-10-23 01:46:34
Read more: https://s.yimg.com/uu/api/res/1.2/sGocJDN_dI8s949Pp.0Tkw--~B/aD01OTk7dz0xMjAwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/the_huffington_post_584/e9407c0ff7ea369c92c149d0fa6c0106


```
Or for second iteration (when installed using setuptools):
```
> C:\Users\user\rss>rss_reader.py "https://news.yahoo.com/rss/" --date 20211023

Cached news items for date 'October 23, 2021'

Title: The story of Carol and Karen: Two experimental Facebook accounts show how the company helped divide America
Channel: Yahoo News - Latest News & Headlines
Channel URL: https://news.yahoo.com/rss/
Date: 2021-10-23T08:00:10Z
Detail: 2021-10-23 08:00:10
Read more: https://s.yimg.com/uu/api/res/1.2/4SS3v7Hgt9GDo.0tfbndHQ--~B/aD0zNzcxO3c9NDM0ODthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/usa_today_tech_153/6f11e68ab704af3b5cc338fa9cc52aa7

Title: Rep. Eric Swalwell Shares Chilling Voicemail Sent To Him By Tucker Carlson Fan
Channel: Yahoo News - Latest News & Headlines
Channel URL: https://news.yahoo.com/rss/
Date: 2021-10-23T07:08:33Z
Detail: 2021-10-23 07:08:33
Read more: https://s.yimg.com/uu/api/res/1.2/MhcXwchBo0tsDS4ZXYpxoA--~B/aD02MDA7dz05NTg7YXBwaWQ9eXRhY2h5b24-/https://media.zenfs.com/en/the_huffington_post_584/b6435d8564a57bf5392dabe3b8e44df6

Title: Email shows Loudoun superintendent knew of bathroom sexual assault on same day
Channel: Yahoo News - Latest News & Headlines
Channel URL: https://news.yahoo.com/rss/
Date: 2021-10-23T03:11:00Z
Detail: 2021-10-23 03:11:00
Read more: https://s.yimg.com/uu/api/res/1.2/V8W1bGMQJFADxHiXa_C.Nw--~B/aD05NDA7dz0xNTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/washington_examiner_articles_265/934f042c03f4154c4c135a36b1f24a34

Title: Jake Tapper Says Rep. Marjorie Taylor Greene Has 'Issues' After Her Rant On Bannon Vote
Channel: Yahoo News - Latest News & Headlines
Channel URL: https://news.yahoo.com/rss/
Date: 2021-10-23T01:46:34Z
Detail: 2021-10-23 01:46:34
Read more: https://s.yimg.com/uu/api/res/1.2/sGocJDN_dI8s949Pp.0Tkw--~B/aD01OTk7dz0xMjAwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/the_huffington_post_584/e9407c0ff7ea369c92c149d0fa6c0106


```
4) If `--date` specified _together with RSS source_, then app should get news _for this date_ from local cache that _were fetched from specified source_.
5) `--date` should work correctly with both `--json`, `--limit`, `--verbose` and their different combinations.
``` 
C:\Users\user\rss>python rss_reader.py "https://news.yahoo.com/rss/" --date 20211023  --limit 2

Cached news items for date 'October 23, 2021'

Title: The story of Carol and Karen: Two experimental Facebook accounts show how the company helped divide America
Channel: Yahoo News - Latest News & Headlines
Channel URL: https://news.yahoo.com/rss/
Date: 2021-10-23T08:00:10Z
Detail: 2021-10-23 08:00:10
Read more: https://s.yimg.com/uu/api/res/1.2/4SS3v7Hgt9GDo.0tfbndHQ--~B/aD0zNzcxO3c9NDM0ODthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/usa_today_tech_153/6f11e68ab704af3b5cc338fa9cc52aa7

Title: Rep. Eric Swalwell Shares Chilling Voicemail Sent To Him By Tucker Carlson Fan
Channel: Yahoo News - Latest News & Headlines
Channel URL: https://news.yahoo.com/rss/
Date: 2021-10-23T07:08:33Z
Detail: 2021-10-23 07:08:33
Read more: https://s.yimg.com/uu/api/res/1.2/MhcXwchBo0tsDS4ZXYpxoA--~B/aD02MDA7dz05NTg7YXBwaWQ9eXRhY2h5b24-/https://media.zenfs.com/en/the_huffington_post_584/b6435d8564a57bf5392dabe3b8e44df6


```
```
C:\Users\user\rss>rss_reader.py "https://news.yahoo.com/rss/" --date 20211023  --limit 2 --verbose
INFO: 24.10.2021 15:10:20 - 2 news items retrieved from cache
INFO: 24.10.2021 15:10:20 - Data converted to text string

Cached news items for date 'October 23, 2021'

Title: The story of Carol and Karen: Two experimental Facebook accounts show how the company helped divide America
Channel: Yahoo News - Latest News & Headlines
Channel URL: https://news.yahoo.com/rss/
Date: 2021-10-23T08:00:10Z
Detail: 2021-10-23 08:00:10
Read more: https://s.yimg.com/uu/api/res/1.2/4SS3v7Hgt9GDo.0tfbndHQ--~B/aD0zNzcxO3c9NDM0ODthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/usa_today_tech_153/6f11e68ab704af3b5cc338fa9cc52aa7

Title: Rep. Eric Swalwell Shares Chilling Voicemail Sent To Him By Tucker Carlson Fan
Channel: Yahoo News - Latest News & Headlines
Channel URL: https://news.yahoo.com/rss/
Date: 2021-10-23T07:08:33Z
Detail: 2021-10-23 07:08:33
Read more: https://s.yimg.com/uu/api/res/1.2/MhcXwchBo0tsDS4ZXYpxoA--~B/aD02MDA7dz05NTg7YXBwaWQ9eXRhY2h5b24-/https://media.zenfs.com/en/the_huffington_post_584/b6435d8564a57bf5392dabe3b8e44df6

```
## [Iteration 4] Format converter.

You should implement the conversion of news in at least two of the suggested format: `.mobi`, `.epub`, `.fb2`, `.html`, `.pdf`

New optional argument must be added to your utility. This argument receives the path where new file will be saved. The arguments should represents which format will be generated.

For example:  `--to-mobi` or `--to-fb2` or `--to-epub`

You can choose yourself the way in which the news will be displayed, but the final text result should contain pictures and links, if they exist in the original article and if the  format permits to store this type of data.

### Task clarification (IV)

Convertation options should work correctly together with all arguments that were implemented in Iterations 1-3. For example: 
* Format convertation process should be influenced by `--limit`.
* If `--json` is specified together with convertation options, then JSON news should 
be printed to stdout, and converted file should contain news in normal format.
* Logs from `--verbose` should be printed in stdout and not added to the resulting file.
* `--date` should also work correctly with format converter and to not require internet access.

## * [Iteration 5] Output colorization.
> Note: An optional iteration, it is not necessary to implement it. You can move on with it only if all the previous iterations (from 1 to 4) are completely implemented.

You should add new optional argument `--colorize`, that will print the result of the utility in colorized mode.

*If the argument is not provided, the utility should work like in the previous iterations.*

### This function in my program only works in the Python console!!!

![image](https://user-images.githubusercontent.com/87867142/138593891-d3751de7-9c6e-47d0-b3cf-a6bdaba21b51.png)


> Note: Take a look at the [colorize](https://pypi.org/project/colorize/) library


---
Implementations will be checked with the latest cPython interpreter of 3.9 branch.
---

> Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. Code for readability. **John F. Woods**
