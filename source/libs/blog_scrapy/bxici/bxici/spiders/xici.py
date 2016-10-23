#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@ author = magic
"""
import scrapy
from bxici.items import BxiciItem


class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ["xicidaili.com"]
    start_urls = (
        'http://xicidaili.com',
    )

    def start_requests(self):
        reqs = []
        for i in range(300, 1085):
            print "Downloading: http://www.xicidaili.com/nn/{}".format(i)
            req = scrapy.Request("http://www.xicidaili.com/nn/{}".format(i))
            reqs.append(req)

        return reqs

    def parse(self, response):
        ip_list = response.xpath('//table[@id="ip_list"]')
        trs = ip_list[0].xpath('tr')

        items = []
        for ip in trs[1:]:
            pre_item = BxiciItem()
            pre_item['IP'] = ip.xpath('td[2]/text()')[0].extract()
            pre_item['PORT'] = ip.xpath('td[3]/text()')[0].extract()
            pre_item['POSITION'] = ip.xpath('string(td[4])')[0].extract().strip()
            pre_item['TYPE'] = ip.xpath('td[6]/text()')[0].extract()
            pre_item['SPEED'] = ip.xpath('td[7]/div[@class="bar"]/@title')[0].re('\d+\.\d+')[0]
            pre_item['LAST_CHECK_TIME'] = ip.xpath('td[10]/text()')[0].extract()
            items.append(pre_item)
        return items


