import tldextract
from urllib.request import urlopen
import re
import pickle
from newspaper import Article

name = 'articles.pk'

articles = []

with open(name, 'wb') as fi:
	pickle.dump(articles, fi)

def countWord(articulo, keyword):
	count = 0
	for i in range(len(articulo)):
		for j in range(len(keyword)):
			if(articulo[i]==keyword[j]):
				count+=1
	return count


def getArticles():
    name = "articles.pk"
    with open(name, 'rb') as fi:
        dictionary = pickle.load(fi)
    return dictionary

def saveArticles(dictionary):
	name = 'articles.pk'
	with open(name, 'wb') as fi:
		pickle.dump(dictionary, fi)

data = {
	        'titulo': title,
	        'categoria': mayor,
	        'confiable': js,
	        'candidato': candidato,
	        'img':img, 
	        'url':noticia
	    }

def obtenerFeed(candidato,categoria):
	array = getArticles()
	respuesta = []
	count = 0
	for i in range (array):
		if(array[i]['candidato']==candidato):
			if(array[i]['categoria']):
				respuesta.append(array[i])
				count++
		if count == 11:
			break
	return respuesta

print(checkArticle("http://www.eluniversal.com.mx/columna/periodistas-el-universal/nacion/el-bronco-cabalga-en-redes-sociales"))