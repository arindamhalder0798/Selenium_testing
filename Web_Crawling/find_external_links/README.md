
Basic Web crawler using Python - Scrapy 
It starts off by crawling the page : https://dmoz-odp.org/Sports/Events/
Finds any external (which are not dmoz-odp) website URLs.
Among the external websites' URL, it stores first 10 website url into local DB Stroage (here i used sqlite DB).



Environment Requires-
Scrapy


Run by the command:
scrapy crawl dmoz_spider
