import urllib, sys,re,os
from lxml.html import parse
import bs4 as bs
import unicodedata

def writing(output):
	file = open(completeName, "w")
	file.write(output + ' \n' )
	file.close()

url_dir= 'http://fing.uach.mx/facultad/2015/09/24/directorio_docente/'
url_main = 'http://fing.uach.mx'
parsed = parse(url_dir)
doc = parsed.getroot()
links = doc.findall('.//div[@id="listalinks"]/p/a')
output_dir = "Professors"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

interests = []
while True:
	interest = raw_input('What are you interested in? (type a number to end) \n')
	if interest.isdigit():
		sys.stdout.write("\033[F")
		break
	for i in interest.split():
		interests.append(i)


i = 1.0
<<<<<<< HEAD
=======
finder =  re.compile(r'\b\s(:?%s)\b\s' % '|'.join(interests), flags = re.I | re.X | re.S)
print '\b(%s)\b' % '|'.join(interests)
>>>>>>> crawling_tests
for link in links:
	prof_name = link.text_content()
	completeName = os.path.join(output_dir, prof_name+".html")
	profurl = url_main+link.get("href")
	html = urllib.urlopen(profurl).read()
	soup_prof = bs.BeautifulSoup(html, 'lxml')
	for info in soup_prof.findAll("div", attrs ={'id' : "secciones", 'align': None, 'class': None}):
		output = unicodedata.normalize('NFD',unicode(info)).encode('ascii','ignore')
		if info is not None and (finder.findall(output) or finder.findall(info.prettify())):
			writing(output)
	a = (i/len(links))*100
	print 'Finding matching professors ' "%.2f" % a, '%'
	sys.stdout.write("\033[F") # Cursor up one line
	i += 1
print '\n Done!'
