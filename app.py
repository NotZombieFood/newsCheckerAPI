"""API del cotizador de innover."""
import json
import os
from datetime import timedelta
import sys
import math
import requests
from flask import Flask, request, render_template, send_file, make_response, current_app
import argparse
from functools import update_wrapper
import requests
import time
import string
import pickle
from flask_cors import CORS
import tldextract
from urllib.request import urlopen
import re
import pickle
from newspaper import Article

# %% Flask app
app = Flask(__name__)
CORS(app)

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

def checkArticle(noticia):
    a = Article(noticia, language='es')
    a.download()
    a.parse()
    img = a.top_image
    sitiosConfiables = ["huffingtonpost", "cnn", "bbc", "nytimes", "milenio", "eluniversal", "proceso", "reforma","expansion","animalpolitico"]
    sitiosDesconfiables = ["eldeforma", "procesomx", "spdnoticias", "noticiasallimite"]
    hostname = tldextract.extract(noticia)
    if hostname.domain in sitiosConfiables:
        js = "El sitio es confiable"
    elif hostname.domain in sitiosDesconfiables:
        js = "No es confiable el sitio"
    else:
        js = "No contamos con información suficiente"
    title = a.title
    text = a.text
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    text=text.lower()
    text=re.split(' ',text)
    for i in range(len(text)):
        text[i] = text[i].strip('.,;:')
    Economia = ["economia", "economico", "ahorro" ,  "parquedad",  "reducción",  "finanzas",  "bienes",  "capital",  "caudal",  "hacienda",  "heredad",  "patrimonio",  "peculio",  "pertenencias",  "posesiones",  "riqueza", "compra", "venta"]
    Educativo=["educacion", "educativo", "enseñanza",  "instrucción",  "magisterio",  "aprendizaje",  "enseñanza",  "estudios",  "formación",  "adiestramiento",  "aprendizaje",  "entrenamiento",  "instrucción",  "urbanidad",  "enseñanza",  "pedagogía",  "sep"]
    Internacional=["salud", "estado", "migracion", "inmigrantes", "arancel", "muro", "Trump", "extranjero", "comercio", "paises", "exportación", "importación", "inmigratorias", "politica", "tratado"]
    Salud=["bienestar", "seguro", "imss", "salubridad", "sanidad", "cobertura", "discapacidad", "rehabilitacion", "salud", "subsidio", "prevención"]
    Seguridad=["seguridad", "protección", "policía", "armado", "armadas", "arma", "crimen", "salvaguarda", "droga", "tráfico", "civil", "tiroteo", "defensa", "hacker"]
    Ecologia=["ambiente", "reciclado", "ecosistema", "plantas", "bosque", "deforestación", "ecología", "cultivo", "xcaret"]
    contadores = {"economia": countWord(text,Economia),"educacion": countWord(text,Educativo),"internacional":countWord(text,Internacional), "salud":countWord(text,Salud),"seguridad":countWord(text,Seguridad),"ecologia":countWord(text,Ecologia)}
    mayor = max(contadores, key=contadores.get)
    amlo = ["amlo", "andres", "manuel","lopez","obrador"]
    anaya = ["ricardo","anaya"]
    margarita = ["margarita","zavala"]
    meade = ["meade","antonio"]
    bronco = ["jaime","rodríguez","bronco"]
    rios = ["armando","rios","jaguar"]
    contadorCandidato = {"amlo": countWord(text,amlo),"anaya": countWord(text,anaya),"meade": countWord(text,meade),"margarita": countWord(text,margarita),"bronco": countWord(text,bronco),"rios": countWord(text,rios)}
    candidato = max(contadorCandidato, key=contadorCandidato.get)
    print(contadorCandidato[candidato])
    print(contadores[mayor])
    if ((contadorCandidato[candidato]==0) | (contadores[mayor]==0)):
        return "NoCat/NoPresidencial"
    else:
        data = {
            'titulo': title,
            'categoria': mayor,
            'confiable': js,
            'candidato': candidato,
            'img':img
        }
        array = getArticles()
        array.append(data)
        saveArticles(array)
    return js

def obtenerFeed(candidato,categoria):
    array = getArticles()
    respuesta = []
    count = 0
    for i in range(array):
        if(array[i]['candidato']==candidato):
            if(array[i]['categoria']):
                respuesta.append(array[i])
                count=count+1
        if count == 11:
            break
    js = json.dumps(respuesta)
    return js


@app.route('/ARTICLE', methods=['GET'])
def getparameters2():
    url = request.args.get("url")
    x = checkArticle(url)
    return x


@app.route('/')
def index():
    return "api is alive!"


@app.route('/FEED', methods=['GET'])
def getparameters3():
    candidato = request.args.get("candidato")
    categoria = request.args.get("categoria")
    x = obtenerFeed(candidato,categoria)
    return x

if __name__ == '__main__':
    app.run()
