import argparse
"""Parser for command-line options, arguments and sub-commands"""
import logging
""" Logging facility for Python"""
import json
"""For output in the JSON-format"""
import os.path
"""This module implements some useful functions on pathnames."""
import re
"""This module provides regular expression matching operations similar to those found in Perl."""
import sqlite3
"""DB-API 2.0 interface for SQLite databases"""
"""This module provides access to some variables used or maintained 
by the interpreter and to functions that interact strongly with the interpreter. 
It is always available."""
from io import StringIO
"""The StringIO module is an in-memory file-like object. 
This object can be used as input or output to 
the most function that would expect a standard file object."""
from urllib.parse import urlsplit, urlunsplit, quote
"""This module defines a standard interface to break Uniform Resource Locator (URL) strings up 
in components (addressing scheme, network location, path etc.), to combine the components back 
into a URL string, and to convert a “relative URL” to an absolute URL given a “base URL.”"""
from urllib.request import Request, urlopen
"""The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP)
in a complex world — basic and digest authentication, redirections, cookies and more."""
import xml.etree.ElementTree as ET
"""The xml.etree.ElementTree module implements a simple and efficient API 
for parsing and creating XML data."""
from utilits import Colors
"""For color output"""
from datetime import datetime
"""The datetime module supplies classes for manipulating dates and times."""
import html
"""For output in the HTML-format"""
from fpdf import FPDF
"""For output in the PDF-format"""

def parse_args():
    """Adding arguments"""
    parser = argparse.ArgumentParser(prog="rss_reader.py", description="Pure Python command-line RSS reader.")
    parser.add_argument("--version", action="version", version="Version 1.5", help="Print version info")
    parser.add_argument("--json", action="store_true", help="Print result as JSON in stdout")
    parser.add_argument("--verbose", action="store_true", help="Outputs verbose status messages")
    parser.add_argument("--limit", type=int, default=None, help="Limit news topics if this parameter provided")
    parser.add_argument("source", nargs="?", default=None, help="Specify correctly URL")
    parser.add_argument("--date", default=None, help="It should take a date in %Y%m%d format")
    parser.add_argument('--colorize', action='store_true', help="Color output")
    parser.add_argument("--to-pdf", dest='pdf', default=False, action='store_true', help="Output in PDF format")
    parser.add_argument("--to-html", dest='html', default=False, action='store_true', help="Output in HTML format")
    x = parser.parse_args()
    if x.limit is not None and x.limit < 1:
        parser.error("--limit LIMIT is specified incorrectly")
    if x.date:
        try:
            datetime.strptime(x.date, "%Y%m%d")
        except ValueError:
            parser.error("It should take a date in %Y%m%d format")
    return x

def i_logging(verbose_flag):
    """Logging facility"""
    if verbose_flag:
        logging.basicConfig(level=logging.DEBUG,
                            format="%(levelname)s: %(asctime)s - %(message)s",
                            datefmt="%d.%m.%Y %H:%M:%S")
    else:
        logging.basicConfig(level=logging.ERROR,
                            format="%(levelname)s: %(message)s")

def xml(url):
    """String input validation"""
    splitted = urlsplit(url)
    if not splitted.scheme:
        logging.error("Link not entered / entered incorrectly")
    elif not splitted.netloc:
        logging.error("Invalid value")
    else:
        if not url.isascii():
            url = urlunsplit(part.encode("idna").decode("utf-8") if i == 1 else quote(part) for i, part in enumerate(splitted))
        try:
            with urlopen(Request(url)) as response:
                root = ET.fromstring(response.read())
                return root
        except ET.ParseError:
            logging.error("Invalid value")

def strip_of_text(text):
    """Removing extra spaces, tags and objects"""
    stripped = re.sub(r"<.+?>", "", text).strip()
    stripped = re.sub(r"\s{2,}|&nbsp;|\n", " ", stripped)
    stripped = html.unescape(stripped)
    return stripped

def get_image_link(text):
    """Get links to images"""
    img_tag = re.findall(r"<img.+?>", text)[0]
    image_link = re.findall(r"""src=["'](.*?)["']""", img_tag)[0]
    return image_link

def get_absolute_url(url, channel):
    """Changing the entered link"""
    try:
        site = channel.find("link").text
        if site.endswith("/"):
            site = site[:-1]
        absolute_url = site + url
    except AttributeError:
        absolute_url = url
    return absolute_url

def get_ending(num):
    """Obtaining an items / item"""
    return "items" if num != 1 else "item"

def finish_of_analysis(url, root, limit):
    """Display title, publication date, image links, description, article links"""
    news = {}
    channel = root.find("channel")
    if channel is None:
        logging.error("RSS channel was not found in XML document")
        return None
    title = channel.find("title")
    title = "" if title is None or title.text is None else strip_of_text(title.text)
    logging.info(f"RSS channel '{title}' found")
    desc = channel.find("description")
    desc = "" if desc is None or desc.text is None else strip_of_text(desc.text)
    news["Channel"] = {"Title": title, "Description": desc, "URL": url}
    if channel.find("item") is None:
        logging.error("No news found in RSS channel")
        return None
    n = 0
    for item in channel.iter("item"):
        if limit is not None and len(news) > limit:
            break
        else:
            n += 1
            title = item.find("title")
            title = "" if title is None or title.text is None else strip_of_text(title.text)
            date = item.find("pubDate")
            date = "" if date is None or date.text is None else strip_of_text(date.text)
            desc = item.find("description")
            desc = "" if desc is None or desc.text is None else desc.text
            link = item.find("link")
            link = "" if link is None or link.text is None else strip_of_text(link.text)
            if link.startswith("/"):
                link = get_absolute_url(link, channel)
            image = None
            enclosures = item.findall("enclosure")
            if enclosures:
                for enclosure in enclosures:
                    enc_type = enclosure.attrib.get("type", "")
                    if "image" in enc_type or not enc_type:
                        image = enclosure.attrib.get("url", None)
            else:
                try:
                    image = get_image_link(desc)
                except IndexError:
                    for elem in list(item.iter()):
                        tag = elem.tag[elem.tag.find("}")+1:]
                        if tag in ["thumbnail", "content", "encoded"]:
                            image = elem.attrib.get("url", None)
                            if image is not None:
                                break
                            else:
                                try:
                                    image = get_image_link(elem.text)
                                    break
                                except (IndexError, AttributeError, TypeError):
                                    continue
            if image is None or not image:
                try:
                    image = channel.find("image").find("url").text
                except AttributeError:
                    try:
                        image = root.find("image").find("url").text
                    except AttributeError:
                        image = ""
            if image.startswith("/"):
                image = get_absolute_url(image, channel)
            desc = strip_of_text(desc)
            news[f"News {n}"] = {"Title": title,
                                      "Date": date,
                                      "Image": image,
                                      "Description": desc,
                                      "Link": link}
    channel_length = len(news) - 1
    ending = get_ending(channel_length)
    if limit is not None and channel_length < limit:
        logging.warning(f"Limit set to {limit} but only {channel_length} news {ending} found")
    logging.info(f"{channel_length} news {ending} processed")
    return news

def dict_to_string(news, json_flag, date, colors: Colors):
    """Conversion from dictionary to string"""
    if json_flag:
        final_string = json.dumps(news, ensure_ascii=False, indent=1)
    else:
        string_obj = StringIO()
        string_obj.write("\n")
        if date is None:
            if news["Channel"]["Title"]:
                string_obj.write(f"{colors.red}Feed: {news['Channel']['Title']}\n")
            if news["Channel"]["Description"]:
                string_obj.write(f"{colors.red}Description: {news['Channel']['Description']}\n")
            if news["Channel"]["URL"]:
                string_obj.write(f"{colors.red}URL: {news['Channel']['URL']}\n")
        else:
            date_as_date = datetime.strptime(date, "%Y%m%d")
            date_formatted = datetime.strftime(date_as_date, "%B %d, %Y")
            string_obj.write(f"Cached news items for date '{date_formatted}'\n")
        string_obj.write("\n")
        for item in news:
            if item.startswith("News"):
                if news[item]["Title"]:
                    string_obj.write(f"{colors.red}Title: {news[item]['Title']}\n")
                if date:
                    if news[item]["Channel"]:
                        string_obj.write(f"{colors.red}Channel: {news[item]['Channel']}\n")
                    if news[item]["Channel URL"]:
                        string_obj.write(f"{colors.red}Channel URL: {news[item]['Channel URL']}\n")
                if news[item]["Date"]:
                    string_obj.write(f"{colors.red}Date: {news[item]['Date']}\n")
                if news[item]["Image"]:
                    string_obj.write(f"{colors.red}Image: {news[item]['Image']}\n")
                if news[item]["Description"]:
                    string_obj.write(f"{colors.red}Detail: {news[item]['Description']}\n")
                if news[item]["Link"]:
                    string_obj.write(f"{colors.red}Read more: {news[item]['Link']}\n")
                string_obj.write("\n")
        final_string = string_obj.getvalue()[:-1]
    return final_string

INFO = os.path.join(os.path.split(__file__)[0], "info.db")
def create_sql_table():
    """Creating a SQL-table"""
    con = sqlite3.connect(INFO)
    cur = con.cursor()
    cur.execute("CREATE TABLE news ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "channel TEXT, "
                "url TEXT, "
                "title TEXT, "
                "date TEXT, "
                "date_as_date DATE, "
                "desc TEXT, "
                "image TEXT, "
                "link TEXT, "
                "UNIQUE(channel, url, title, date, desc, image, link));")
    con.close()

def parse_date(date):
    """Date format conversion p.1"""
    date_as_date = None
    date_formats = ["datetime.strptime(date, '%Y-%m-%d %H:%M:%S')"]
    for date_format in date_formats:
        try:
            date_as_date = eval(date_format)
            break
        except ValueError:
            continue
    if date_as_date is None:
        logging.warning(f"Incorrectly date")
    return date_as_date
def reformat_date(date):
    """Date format conversion p.2"""
    date_as_date = datetime.strptime(date, "%Y%m%d")
    date_reformatted = datetime.strftime(date_as_date, "%B %d, %Y")
    return date_reformatted

def store_to_sql(news):
    """Storing data in a SQL-table"""
    con = sqlite3.connect(INFO)
    cur = con.cursor()
    channel = news["Channel"]["Title"]
    url = news["Channel"]["URL"]
    for item in news:
        if item.startswith("News"):
            title = news[item]["Title"]
            date = news[item]["Date"]
            date_as_date = parse_date(date)
            desc = news[item]["Description"]
            image = news[item]["Image"]
            link = news[item]["Link"]
            try:
                cur.execute("INSERT INTO news(channel, url, title, date, date_as_date, desc, image, link) "
                            "VALUES(?, ?, ?, ?, ?, ?, ?, ?);",
                            (channel, url, title, date, date_as_date, desc, image, link))
            except sqlite3.IntegrityError:
                continue
    con.commit()
    changes = con.total_changes
    con.close()
    existing = len(news) - 1 - changes
    ending = get_ending(changes)
    if existing:
        ending_exist = get_ending(existing)
        logging.info(f"{changes} news {ending} saved to cache. {existing} news {ending_exist} already in cache.")
    else:
        logging.info(f"{changes} news {ending} saved to cache.")

def retrieve_from_sql(date, source, limit):
    """Table Output"""
    source = "%" if source is None else source
    con = sqlite3.connect(INFO)
    cur = con.cursor()
    if limit is not None:
        cur.execute("SELECT * FROM news WHERE url LIKE ? AND STRFTIME('%Y%m%d', date_as_date)=? "
                    "ORDER BY date_as_date DESC LIMIT ?;", (source, date, limit))
    else:
        cur.execute("SELECT * FROM news WHERE url LIKE ? AND STRFTIME('%Y%m%d', date_as_date)=? "
                    "ORDER BY date_as_date DESC;", (source, date))
    news = {}
    n = 0
    for row in cur:
        n += 1
        news[f"News {n}"] = {"Channel": row[1],
                                  "Channel URL": row[2],
                                  "Title": row[3],
                                  "Date": row[4],
                                  "Description": row[5],
                                  "Image": row[6],
                                  "Link": row[7]}
    con.close()
    dict_length = len(news)
    ending = get_ending(dict_length)
    if news:
        if limit is not None and dict_length < limit:
            logging.warning(f"Limit set to {limit} but only {dict_length} news {ending} found in cache")
        logging.info(f"{dict_length} news {ending} retrieved from cache")
    else:
        logging.error(f"No information found in cache for '{date}'")
    return news

def to_html(self):
    limit = self.limit
    if (limit == None or limit > len(self.feed) or limit < 1):
        limit = len(self.feed)
    news = ''
    if self.channel:
        news += f'{self.channel} \n\n'
    if len(self.feed) == 0:
        print('No articles')
    html = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
    """
    for article in self.feed[:limit]:
        title_content = f"\t\t\t<h3>{article['title']}<h3>\n"
        date_content = f"\t\t\t<p>PubDate: {article['pubDate']}</p>\n"
        link_content = f"\t\t\t<a href='{article['link']}'>Source</a>\n"
        descr_content = f"\t\t\t"

        article_content = '\t\t<div>\n'
        article_content += title_content + date_content + link_content + descr_content + '</div>\n'
        html += article_content
    html += '    </body>\n</html>'

    with open('HTML.html', 'w') as doc:
        doc.write(html)

def to_pdf(self, path=None):
    limit = self.limit
    if (limit == None or limit > len(self.feed) or limit < 1):
        limit = len(self.feed)
    news = ''
    if self.channel:
        news += f'{self.channel} \n\n'
    if len(self.feed) == 0:
        print('No articles')

    for article in self.feed[:limit]:
        news += f"Title: {article['title']}\nDate: {article['pubDate']}\nLink: {article['link']}\n"
        if article['description']:
            news += f"Description: {article['description']}"
        news += f'\n'
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 10, txt=news)
    if path:
        pdf.output(path)
    else:
        pdf.output('PDF.pdf')

def main():
    """Final output of the program"""
    x = parse_args()
    i_logging(x.verbose)
    if x.colorize:
        colors = Colors(True)
    else:
        colors = Colors(False)
    if not os.path.exists(INFO):
        create_sql_table()
    if x.date is not None:
        news = retrieve_from_sql(x.date, x.source, x.limit)
        if not news:
            return None
    else:
        root = xml(x.source)
        if root is None:
            return None
        news = finish_of_analysis(x.source, root, x.limit)
        if news is None:
            return None
        store_to_sql(news)
    end_of_rss = dict_to_string(news, x.json, x.date, colors=colors)
    print(end_of_rss)

if __name__ == "__main__":
    main()