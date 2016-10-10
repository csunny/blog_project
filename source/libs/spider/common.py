#!usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author magic
"""
import urllib2


def download(url, user_agent='wswp', num_retries=2):
    print 'Downloading:', url
    headers = {'User-Agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError, e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                html = download(url, user_agent, num_retries-1)
    return html


if __name__ == '__main__':
    pass
    # download('http://blog.csdn.net/column/details/datamining.html')









