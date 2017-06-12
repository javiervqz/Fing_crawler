import urllib
import HTMLParser
from BeautifulSoup import *
from lxml.html import parse
from pandas.io.parsers import TextParser


class parseText(HTMLParser.HTMLParser):
	def handle_data(self, data):
		if data != '\n':
			urlText.append(data)

def _unpack (row, kind = 'td'):
	elts = row.findall('.//%s' % kind)
	return [val.text for val in elts]

def parse_options_data (table):
	rows = table.findall('.//tr')
	header = _unpack(rows[0], kind = 'th')
	data = [_unpack(r) for r in rows[1:]]
	return TextParser(data, names=header).get_chunk()

url_dir= 'http://fing.uach.mx/facultad/2015/09/24/directorio_docente/'
url_main = 'http://fing.uach.mx'
parsed = parse(url_dir)
doc = parsed.getroot()
links = doc.findall('.//a')

for link in links:
	print link.text_content()
