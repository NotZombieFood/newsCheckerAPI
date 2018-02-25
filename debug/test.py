from newspaper import Article
url = 'http://www.eluniversal.com.mx/columna/periodistas-el-universal/nacion/el-bronco-cabalga-en-redes-sociales'

a = Article(url, language='es') # Chinese

a.download()
a.parse()

print(a.text)

print(a.title)

print(a.top_image)

