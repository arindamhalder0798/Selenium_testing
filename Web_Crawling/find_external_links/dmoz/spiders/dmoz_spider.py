import scrapy
from ..items import DmozItem

class dmozSpider(scrapy.Spider):
    name = "dmoz_spider"
    # start_urls = ['http://brickset.com/sets/year-2016']
    start_urls = ['https://dmoz-odp.org/Sports/Events/']

    def parse(self, response):
        items = DmozItem()
        
        all_links  = response.xpath('//a[contains(@href, "https://") or contains(@href, "http://") and not(contains(@href, "dmoz-odp.org"))] //@href').extract()
        all_name  = response.xpath('//a[contains(@href, "https://") or contains(@href, "http://") and not(contains(@href, "dmoz-odp.org"))] //text()').extract()

        # excluding links with no name
        count = 0
        final_name = []
        final_link = []
        for name in all_name:
            #get rid of spaces
            stripped_name = name.strip()
            stripped_name = stripped_name.replace("\n", "")
            stripped_name = stripped_name.replace("\r", "")
            if  stripped_name:
                final_name.append(stripped_name)
                final_link.append(all_links[count].strip())

                count = count + 1

        items['name']  = final_name[:10]
        # starting from 1 beacause of wrong naming
        items['link']  = final_link[1:11]
        
        # print("count --- ", count)
        yield items