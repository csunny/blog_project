#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@ author = magic
"""
import logging
from proxy import GetIp

filepath = r'C:\Users\think\Desktop\new_ips.csv'
ips_g = GetIp('../ips.csv').get_ip(filepath)
ips = [ip for ip in ips_g]


class ProxyMiddleware(object):
    http_n = 0
    https_n = 0

    def process_request(self, request, spider):
        # Set the location of the proxy
        if request.url.startswith('http://'):
            n = ProxyMiddleware.http_n
            n = n if n < len(ips) else 0
            request.meta['proxy'] = "http://%s" % (
                ips[n]['http'])
            logging.info('Squence - http: %s - %s' % (n, str(ips[n]['http'])))
            ProxyMiddleware.http_n = n + 1

        if request.url.startswith('https://'):
            n = ProxyMiddleware.https_n
            n = n if n < len(ips) else 0
            request.meta['proxy'] = "https://%s" % (
                ips[n]['https']
            )
            logging.info('Squence - http: %s - %s' % (n, str(ips[n]['https'])))
            ProxyMiddleware.https_n = n + 1



