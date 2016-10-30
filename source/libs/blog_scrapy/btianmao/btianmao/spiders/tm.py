#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@ author: magic
"""
import scrapy
from btianmao.items import BtianmaoItem


class TMaoSpider(scrapy.Spider):
    name = "tm_goods"
    allowed_domain = ['http://www.tianmao.com']
    start_urls = (
        "https://list.tmall.com/search_product.htm?spm=a220m.1000858.1000724.4.fZQJG7&q=%C4%D0%D0%AC&sort=d&style=g&search_condition=2&from=sn_1_brand-qp#J_Filter"
    )
    # 记录处理的页数
    count = 0

    def parse(self, response):
        TMaoSpider.count += 1

        divs = response.xpath("//div[@id='J_ItemList']/div[@class='product']/div")

        if not divs:
            self.log("List Page error--%s" % response.url)

        for div in divs:
            item = BtianmaoItem()
            item['GOODS_PRICE'] = div.xpath("p[@class='productProce']/em/@title")[0].extract()
            item['GOODS_NAME'] = div.xpath("p[@class='productTitle]/a/@title")[0].extract()
            pre_goods_url = div.xpath("p[@class='productTitle']/a/@href")[0].extract()
            item['GOODS_URL'] = pre_goods_url if 'http://' in pre_goods_url else ('http://' + pre_goods_url)
            yield scrapy.Request(url=item['GOODS_URL'], meta={'item': item}, callback=self.parse_detail,
                                 dont_filter=True)

    def parse_detail(self, response):
        div = response.xpath("//div[@class='extend'/ul]")
        if not div:
            self.log("Detail Page error --%s" % response.url)

        item = response.meta['item']
        div = div[0]
        item["SHOP_NAME"] = div.xpath("li[1]/div/a/text()")[0].extract()
        item["SHOP_URL"] = div.xpath("li[1]/div/a/@href")[0].extract()
        item['COMPANY_NAME'] = div.xpath("li[3]/div/text()")[0].extract()
        item["COMPANY_ADDRESS"] = div.xpath("li[4]/div/text()")[0].extract()
        yield item

