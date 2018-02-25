from newspaper import Article
url = 'http://www.huffingtonpost.com.mx/2018/02/24/huexca-una-comunidad-arrollada-por-la-electricidad_a_23369863/?utm_hp_ref=mx-homepage'

a = Article(url, language='es') # Chinese

a.download()
a.parse()

texto = a.text
array = texto.split('\n')
print (array[0])
if (len(array[0])>15):
    if(array[0]!=a.title):
        print("es desct")