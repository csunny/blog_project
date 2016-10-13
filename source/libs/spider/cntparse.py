#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: magic
"""
import lxml.html
import lxml.cssselect
import lxml
import re
from common import download
url = 'http://blog.csdn.net/column/details/datamining.html'


def parse_content(url):
    html = download(url)
    tree = lxml.html.fromstring(html)
    td = tree.cssselect('ul.detail_list > li')
    for lis in td:
        item = {}
        item['title'] = lis.cssselect('h4 > a')[0].text_content()
        item['time'] = lis.cssselect('div.detail_b > span')[0].text_content()
        item['views'] = lis.cssselect('div.detail_b > em')[0].text_content()
        item['abstract'] = lis.cssselect('p.detail_p')[0].text_content()
        item['link'] = lis.cssselect('h4 > a')[0].attrib['href']
        yield item


def get_dateil():
    content = parse_content(url)
    links = [article['link'] for article in content]
    for link in links:
        article_tree = lxml.html.fromstring(download(link))
        article_content = article_tree.cssselect('div#article_content > p')[0]
        print article_content


if __name__ == '__main__':
    # s = parse_content(url)
    # for i in s:
    #     print i['link']
    get_dateil()
