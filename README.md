[![Build Status](https://travis-ci.org/NotZombieFood/newsCheckerAPI.svg?branch=master)](https://travis-ci.org/NotZombieFood/newsCheckerAPI)
![Lenguaje](https://img.shields.io/badge/Lenguaje-Python-blue.svg)
[![Sentry](https://img.shields.io/badge/Sentry-FakenewsMX-yellow.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAMCAQAAAATvv9SAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QA/4ePzL8AAAAJcEhZcwAACxIAAAsSAdLdfvwAAAAHdElNRQfiAhoLFCDLqezOAAAAjklEQVQY03XQPQrCYBCE4ScBfyPiT5dYiFaCNt7ARoKd4EG8j53HEU9gZWcjljaCn2WCmqmWfZmdYalUVIzhaxGXQMNcPXyjQCS3t/brklg5WkpDOSsQ28kkrhIH76jkGtsYeurrW5QPJqbOHpq6TnKtAmW2GgY6JmIjaZFVM9N2F+u66blEr6JG9Sf+6QPzuRdFQpQSQgAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxOC0wMi0yNlQxMToyMDozMi0wNTowMNBBAsoAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTgtMDItMjZUMTE6MjA6MzItMDU6MDChHLp2AAAAAElFTkSuQmCC)](https://sentry.io/itesm-rr/fakenews-mx/)
[![Requisitos](https://img.shields.io/badge/Requisitos-Actualizados-green.svg)](https://github.com/NotZombieFood/newsCheckerAPI/blob/master/requirements.txt)



# fakenewsMXAPI

## Funciones / Notas
+ Listo para hacer deploy en Heroku.
+ API sirviendo 2 funciones distintas.
+ Para debuggear hay una subcarpeta llamada debug e igual se podrá hacer uno con el comando pytest.

## Llamadas a la API 
| Llamada        | Función         | URL  |  Params   |
| ------------- |:-------------:| -----:| :-----:|
| Articulo      | Enviar un artículo para su analisis | **/ARTICLE**  (GET)|  url     |
| Feed    |  Se obtiene un listado de 10 noticias del tema y del candidato    |  **/FEED** (GET)|   candidato categoria     |


## ¿Cómo correrlo en local?
1. En caso de tener Python3, pip y virtual env; ir al paso 5.
2. Instalar Python3
3. Instalar pip 
4. Instalar virtualenv mediante "pip install virtualenv". 
5. Crear un virtual env mediante "mkvirtualenv fakenewsmxAPI".
6. Ir al folder donde clonamos el repo y correr el siguiente comando "setprojectdir .", mediante esto cada vez que ingresemos al entorno se´redireccionará al folder. Para salir del entorno tenemos que usar "deactivate" y para regresar "workon fakenewsmxAPI". Si todo funciona debería de salirnos **(fakenewsmxAPI)** antes de nuestro cursor en la consola.
7. Correr "pip install -r requirements.txt"
8. Correr  "gunicorn app:app"
9. En nuestra url local en el puerto 5000 se debería ver un mensaje.