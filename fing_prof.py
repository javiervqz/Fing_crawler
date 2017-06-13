import urllib, re
from lxml.html import parse, etree



url_dir= 'http://fing.uach.mx/facultad/2015/09/24/directorio_docente/'
url_main = 'http://fing.uach.mx'
parsed = parse(url_dir)
doc = parsed.getroot()
links = doc.findall('.//div[@id="listalinks"]/p/a')
for link in links:
	prof_name = link.text_content()
	profurl = url_main+link.get("href")
	parsed = parse(profurl)
	doc = parsed.getroot()

	raw = doc.findall('.//div/h4')
	finder = re.compile(r'\bCursos\b | \bImpartidos\b', flags = re.I | re.X)
	for tag in raw:
		aver = finder.findall(tag.text_content())
		if aver:
			print prof_name, tag
		# if aver:
		# 	header = tag.getprevious()
		# 	print header, prof_name
