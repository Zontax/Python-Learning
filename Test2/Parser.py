from bs4 import BeautifulSoup
import requests, lxml.html
from lxml import etree

url = 'https://hpk.edu.ua/replacements'


def get_titles(html_text):
    tree = lxml.html.document_fromstring(html_text)
    text_titles = tree.xpath("//*[@class='news-body']/p/strong/text()")
    return text_titles


html_text = requests.get("https://hpk.edu.ua/replacements")
if html_text.status_code == 200:
    text_title(get_titles(html_text.text))
