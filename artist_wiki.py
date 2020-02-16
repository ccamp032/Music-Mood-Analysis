# -*- coding: utf-8 -*-
import scrapy


class ArtistWikiSpider(scrapy.Spider):
	name = 'artist_wiki'
	start_urls = ['https://en.wikipedia.org/wiki/Kendrick_Lamar_discography',
		'https://en.wikipedia.org/wiki/Eminem_albums_discography',
		'https://en.wikipedia.org/wiki/Sia_discography',
		'https://en.wikipedia.org/wiki/Justin_Bieber_discography',
		'https://en.wikipedia.org/wiki/Justin_Timberlake_discography',
		'https://en.wikipedia.org/wiki/Ariana_Grande_discography',
		'https://en.wikipedia.org/wiki/Beyonc%C3%A9_discography',
		'https://en.wikipedia.org/wiki/Bruno_Mars_discography',
		'https://en.wikipedia.org/wiki/Childish_Gambino_discography',
		'https://en.wikipedia.org/wiki/Drake_discography',
		'https://en.wikipedia.org/wiki/Chris_Brown_discography',
		'https://en.wikipedia.org/wiki/Gorillaz_discography',
		'https://en.wikipedia.org/wiki/Imagine_Dragons_discography',
		'https://en.wikipedia.org/wiki/Jay-Z_albums_discography',
		'https://en.wikipedia.org/wiki/Kanye_West_albums_discography',
		'https://en.wikipedia.org/wiki/Lady_Gaga_discography',
		'https://en.wikipedia.org/wiki/Kelly_Clarkson_discography',
		'https://en.wikipedia.org/wiki/Lil_Wayne_albums_discography',
		'https://en.wikipedia.org/wiki/Linkin_Park_discography',
		'https://en.wikipedia.org/wiki/Metallica_discography',
		'https://en.wikipedia.org/wiki/Post_Malone_discography',
		'https://en.wikipedia.org/wiki/Red_Hot_Chili_Peppers_discography',
		'https://en.wikipedia.org/wiki/Rihanna_discography',
		'https://en.wikipedia.org/wiki/Taylor_Swift_discography',
		'https://en.wikipedia.org/wiki/The_Weeknd_discography',
		'https://en.wikipedia.org/wiki/Travis_Scott_discography',
		'https://en.wikipedia.org/wiki/Wu-Tang_Clan_discography'
	]

	def parse(self, response):
		tables = response.xpath('//*[@id="mw-content-text"]/div/table[2]/tbody').extract()
		yield { 'TABLE_HTML' : tables[0]}
