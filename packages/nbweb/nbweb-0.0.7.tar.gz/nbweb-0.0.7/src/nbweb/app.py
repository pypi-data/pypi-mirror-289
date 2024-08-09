import json
import xml.etree.ElementTree as ET
from importlib.resources import files
from urllib.parse import urlparse
from datetime import datetime

from nbweb.page import Page
from nbweb.parser import Parser


def get_content(url: str, return_type: str):
    rules = get_rules(url, "rules")
    if rules is None:
        raise TypeError("url not supported")
    html = Page(url).get()
    content = Parser(rules, html).get()
    if return_type == "txt":
        return json2txt(content)
    return content


def get_rss(url: str):
    rules = get_rules(url)
    if rules is None:
        raise TypeError("url not supported")
    html = Page(url).get()
    data = Parser(rules["rss"], html).get_rss()
    rss = json2rss(rules, data)
    return rss

def check_is_supported(url: str) -> str:
    rules = get_rules(url)
    if rules is None:
        return "no"
    return "yes"

def json2txt(content):
    data = ""
    for attr, value in content.items():
        data += f"{value}\n\n"
    return data


def json2rss(rules, content):
    xml_string = """<?xml version="1.0" encoding="utf-8"?>
    <rss version="2.0">
        <channel>
            <title>Sample Feed</title>
            <description>For documentation &lt;em&gt;only&lt;/em&gt;</description>
            <link>http://example.org/</link>
            <pubDate>Sat, 07 Sep 2002 00:00:01 GMT</pubDate>
        </channel>
    </rss>
    """
    root = ET.fromstring(xml_string)
    channel = root.find("channel")
    title = channel.find("title")
    description = channel.find("description")
    link = channel.find("link")
    pubDate = channel.find("pubDate")
    title.text = rules["url"]
    description.text = rules["name"]
    link.text = rules["url"]
    pubDate = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    for article in content:
        item = ET.SubElement(channel, "item")
        title = ET.SubElement(item, "title")
        title.text = article["title"]
        link = ET.SubElement(item, "link")
        link.text = article["link"]
        description = ET.SubElement(item, "description")
        description.text = article["description"]
        pubDate = ET.SubElement(item, "pubDate")
        pubDate.text = article["published"]
        guid = ET.SubElement(item, "guid")
        guid.text = article["link"]

    xmlstr = ET.tostring(root, encoding="unicode")
    return xmlstr


def get_rules(url: str, data_type=None):
    u = urlparse(url)
    json_data = json.loads(files("nbweb").joinpath("data.json").read_text())
    for entry in json_data:
        e = urlparse(entry["url"])
        if u.hostname in e.hostname:
            if data_type is None:
                return entry
            return entry[data_type]
    return None
