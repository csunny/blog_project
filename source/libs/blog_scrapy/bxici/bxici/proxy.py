#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@ author = magic
"""
import csv
import requests
import json


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
        for line in self.result:
            proxy_type = line[4].lower()
            url = http_url if proxy_type == 'http' else https_url
            proxies = {'http': 'http://'+"{0}:{1}".format(line[0], line[5])}
            try:
                req = requests.get(url=url, proxies=proxies, timeout=1)
            except Exception as e:
                print "Request Error {}".format(e)

            else:
                code = req.status_code
                if 200 <= code <= 300:
                    print 'Effective proxy: {}'.format(line)
                    self._write_ip('../new_ips', line)
                else:
                    print 'Invalide proxy: {}'.format(line)

    def _write_ip(self, newname, content):
        with open(newname, 'ab+') as fp:
            csv.writer(fp).writerow(content)

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


class ParseJson(object):
    def __init__(self):
        self.path = '../ips.json'
        self.result = self._get_res()
        self.items = self._write_to_db()

    def _get_res(self):
        with open(self.path, 'r+') as fp:
            lines = fp.readlines()
            return lines

    def _write_to_db(self):
        try:
            for i, line in enumerate(self.result):
                item = eval(line)[0]
                yield item
        except Exception as e:
            pass


# Test read data from csv file.
def test(name):
    g = GetIp(name)
    g.judge_ip()
    r = g.get_ip('../new_ips')
    for ip in r:
        print r


if __name__ == '__main__':
    pj = ParseJson()
    for i, line in enumerate(pj.result):
        try:
            s = eval(line)[0]
            s.update({'POSITION': s['POSITION'].decode('unicode-escape')})
            if s.has_key('SPEED'):
                print s['POSITION']
        except Exception as e:
            pass

















