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

# %% Flask app
app = Flask(__name__)
CORS(app)




@app.route('/TABLA', methods=['GET'])
def getparameters2():
    id = request.args.get("id")
    cantidad = request.args.get("cantidad")
    unidad = request.args.get("unidad")
    bastidor = request.args.get("bastidor")
    tornillos = request.args.get("tornillos")
    clips = request.args.get("clips")
    x = creartabla(id, unidad, cantidad, bastidor, tornillos, clips)
    return x


@app.route('/')
def index():
    return "Innover is alive!"


@app.route('/GETCATEGORY', methods=['GET'])
def getparameters3():
    x = obtenercategorias()
    return x


@app.route('/UPDATE', methods=["GET"])
def update():
    productsFile = "products.pk"
    categoriesFile = "categories.pk"
    productos = wcapi.get("products?order=asc&per_page=100")
    dictProductos = productos.json()
    with open(productsFile, 'wb') as fi:
        pickle.dump(dictProductos, fi)
    categorias = wcapi.get("products/categories")
    dictCategorias = categorias.json()
    with open(categoriesFile, 'wb') as fi:
        pickle.dump(dictCategorias, fi)
    return "hemos actualizado la base de datos"


@app.route('/NUMBER', methods=['GET'])
def getparameters4():
    x = getnumber()
    return str(x).zfill(4)

if __name__ == '__main__':
    app.run()
