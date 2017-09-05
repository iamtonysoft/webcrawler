import scrapy
from urllib.parse import urljoin
from erc_files.items import ErcFilesItem


class ErcSpider(scrapy.Spider):
	name = "erc_search"
	allowed_domains = ["erc.gov.ph"]
	start_urls = [
					"http://erc.gov.ph/Search/2010-143",
					"http://erc.gov.ph/Search/2011-032",
					"http://erc.gov.ph/Search/2011-043",
					"http://erc.gov.ph/Search/2011-081",
					"http://erc.gov.ph/Search/2011-096",
					"http://erc.gov.ph/Search/2011-097",
					"http://erc.gov.ph/Search/2011-113",
					"http://erc.gov.ph/Search/2011-129",
					"http://erc.gov.ph/Search/2011-130",
					"http://erc.gov.ph/Search/2011-141",
					"http://erc.gov.ph/Search/2011-142",
					"http://erc.gov.ph/Search/2011-167",
					"http://erc.gov.ph/Search/2011-175",
					"http://erc.gov.ph/Search/2012-011",
					"http://erc.gov.ph/Search/2012-019",
					"http://erc.gov.ph/Search/2012-028",
					"http://erc.gov.ph/Search/2012-034",
					"http://erc.gov.ph/Search/2012-042",
					"http://erc.gov.ph/Search/2012-064",
					"http://erc.gov.ph/Search/2012-079",
					"http://erc.gov.ph/Search/2012-082",
					"http://erc.gov.ph/Search/2012-083",
					"http://erc.gov.ph/Search/2012-087",
					"http://erc.gov.ph/Search/2012-098",
					"http://erc.gov.ph/Search/2012-101",
					"http://erc.gov.ph/Search/2012-125",
					"http://erc.gov.ph/Search/2013-090",
					"http://erc.gov.ph/Search/2013-152",
					"http://erc.gov.ph/Search/2014-048",
					"http://erc.gov.ph/Search/2014-105",
					"http://erc.gov.ph/Search/2015-001",
					"http://erc.gov.ph/Search/2015-029",
					"http://erc.gov.ph/Search/2015-077",
					"http://erc.gov.ph/Search/2015-118",
					"http://erc.gov.ph/Search/2015-141",
					"http://erc.gov.ph/Search/2015-182",
					"http://erc.gov.ph/Search/2016-034",
					"http://erc.gov.ph/Search/2016-100",
					"http://erc.gov.ph/Search/2016-175",
					"http://erc.gov.ph/Search/2016-202",
					"http://erc.gov.ph/Search/2016-207",
					"http://erc.gov.ph/Search/2016-208",
					"http://erc.gov.ph/Search/2017-002"
				 ]
	
	def parse(self, response):
		
		#Arrays & Objects
		ERC_FILES = []
		url_list = []
		x = ErcFilesItem()
		data = response.xpath('//table[@id="MainContent_gvSearchResults"]/tr/td[2]')
		
		#Case Number	
		cleanCase = response.url.replace('http://erc.gov.ph/Search/', '')
		x['case'] = cleanCase
		
		#URL List
		list = data.xpath("a/@href").re(r'..\s*(.*)')
		for link in list:
			request = urljoin('http://erc.gov.ph', str(link))
			url_list.append(request)
			x['pdf'] = url_list
		
		ERC_FILES.append(x)			
		return ERC_FILES