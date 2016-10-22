#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@ author = magic
"""
import csv
import requests


class GetIp(object):
    def __init__(self, filename):
        self.filename = filename
        self.result = self._get_res()

    def _get_res(self):
        with open(self.filename, 'rb') as fp:
            for i, line in enumerate(csv.reader(fp)):
                if i >= 1:
                    yield line

    def judge_ip(self):
        " Judge ip's availability "
        http_url = "http://www.baidu.com/"
        https_url = "https://www.alipay.com/"
        data = []
        for line in self.result:
            proxy_type = line[4].lower()
            url = http_url if proxy_type == 'http' else https_url
            proxies = {'http': 'http://'+"{0}:{1}".format(line[0], line[5])}
            try:
                req = requests.get(url=url, proxies=proxies, timeout=5)
            except Exception as e:
                print "Request Error {}".format(e)

            else:
                code = req.status_code
                if 200 <= code <= 300:
                    print 'Effective proxy: {}'.format(line)
                    data.append(tuple(line))
                else:
                    print 'Invalide proxy: {}'.format(line)
        self._write_ip('./new_ips', data)

    def _write_ip(self, newname, content):
        with open(newname, 'wb') as fp:
            csv.writer(fp).writerows(content)

    def get_ip(self, newname):
        with open(newname, 'rb') as fp:
            ips = {}
            for i, line in enumerate(csv.reader(fp)):
                if i > 0:
                    if line[4].lower() == 'http':
                        ips['http'] = line[0] + ":" + line[5]
                    if line[4].lower() == 'https':
                        ips['https'] = line[0] + ":" + line[5]
                    yield ips

if __name__ == '__main__':
    g = GetIp('../ips.csv')
    g.judge_ip()

















