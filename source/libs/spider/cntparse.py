#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: magic
"""
import lxml.html
import lxml.cssselect
import lxml
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


if __name__ == '__main__':
    s = parse_content(url)
    for i in s:
        print i['title']
