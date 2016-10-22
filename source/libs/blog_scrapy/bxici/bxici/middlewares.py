#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@ author = magic
"""
import base64
import logging
from .proxy import GetIp
ips = GetIp('../ips.csv').get_ip('../new_ips.csv')


class ProxyMiddleware(object):
    http_n = 0
    https_n = 0

    def process_request(self, request, spider):
        # Set the location of the proxy
        if request.url.startswith('http://'):
            n = ProxyMiddleware.http_n
            n = n if n < len(ips['http']) else 0
            request.meta['proxy'] = "http://%s:%s" % (
                ips['http'][n][0], int(ips['http'][n][5]))
            logging.info('Squence - http: %s - %s' % (n, str(ips['http'][n])))
            ProxyMiddleware.http_n = n + 1

        if request.url.startswith('https://'):
            n = ProxyMiddleware.https_n
            n = n if n < len(ips['https']) else 0
            request.meta['proxy'] = "https://%s:%s" % (
                ips['https'][n][0], int(ips['https'][n][5])
            )
            logging.info('Squence - http: %s - %s' % (n, str(ips['http'][n])))
            ProxyMiddleware.https_n = n + 1
