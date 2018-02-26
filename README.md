[![Build Status](https://travis-ci.org/NotZombieFood/newsCheckerAPI.svg?branch=master)](https://travis-ci.org/NotZombieFood/newsCheckerAPI)
![Lenguaje](https://img.shields.io/badge/Lenguaje-Python-blue.svg)
[![Sentry](https://img.shields.io/badge/Sentry-FakenewsMX-yellow.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAMCAMAAACOacfrAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAqFBMVEUAAAAiHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB0iHB3///9UKRiuAAAAN3RSTlMAAAcsBgFPnEwMkD5+GgJVcXxcZwIioIRybXkuCkRtcXp7Q3YJJpd0hYeeRZUjBjE8Jik4HS4F7M4nvQAAAAFiS0dENzC4uEcAAAAJcEhZcwAACxIAAAsSAdLdfvwAAAAHdElNRQfiAhoLDTqty7ysAAAAWklEQVQI12NgwASMjIxIHCZmFjiXkZWNnQPB4+Ti5uGFchn5+AUEhYRFIFxGUTFxCUkpaQhPRlZOXkFRSVkFzFNVU9fQ1NLW0QXz9PQNDI2MTUzNYFZDALqbAFWGBePDVfAnAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDE4LTAyLTI2VDExOjEzOjU4LTA1OjAwwIuJAQAAACV0RVh0ZGF0ZTptb2RpZnkAMjAxOC0wMi0yNlQxMToxMzo1OC0wNTowMLHWMb0AAAAASUVORK5CYII=)](https://sentry.io/itesm-rr/fakenews-mx/)
[![Website](https://img.shields.io/badge/Website-Innover-green.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAQAAAC1QeVaAAAA70lEQVQY013QPUuCYRiG4aclG5qlrVp1K9SIqFWlD0iwralyiFd8p0ptaMoaioRwKoTEJiEcKn/d0ZDax72ey30dIYQQQhAkFAwNFSSE6QlmpJ2riEQqzqXNGKekE5dy1vX0rMtoOJEUgkUDp2YVVcVqIrGUUwOLQVbHjSPLVnV1rdgxcq8jG6w5Vvag61VT04s7D8qOrX3HkrwL1z6NnNmSV/ofW969u1VXsP8Ty9qe9TXV9Tx5dPAdszrujWxbGT9U9KHlSm4yJSUWqYlFYmmH2pYmCA0ZG/pThIoFv/gubNpT/cM39Z0zb9fbb/gvvC7zcIQtJxIAAAAASUVORK5CYII=)](https://beta.innover.mx)
[![Requisitos](https://img.shields.io/badge/Requisitos-Actualizados-green.svg)](https://github.com/NotZombieFood/newsCheckerAPI/blob/master/requirements.txt)


https://img.shields.io/badge/style-flat-green.svg?longCache=true&style=flat


# innoverAPI

## Funciones / Notas
+ Listo para hacer deploy en Heroku.
+ API sirviendo 5 funciones distintas.
+ API key de woocomerce de beta.innover.mx
+ Para debuggear hay una subcarpeta llamada debug con un archivo html e igual se podrá hacer uno con el comando pytest.

## Llamadas a la API 
| Llamada        | Función         | URL  |  Params   |
| ------------- |:-------------:| -----:| :-----:|
| Categorías      | Obtener todas las categorías que se encuentran en woocommerce | **/GETCATEGORY**  (GET)|  Sin parámetros     |
| Categoría    | Obtener los productos de una sola categoría-      |  **/CATEGORIA** (GET)|   categoria     |
| Cotizar | Recible un producto y parámetros para calcular el costo total      |  **/TABLA**(GET) | id, unidad, bastidor, tornillos, clips        |
| Número único      | Obtener número unico para poder sacar cotización | **/NUMBER**(GET) |  Sin parámetros     |
| Test      | Poder observar cuando la api funciona | **/**  |  Sin parámetros     |


## ¿Cómo correrlo en local?
1. En caso de tener Python3, pip y virtual env; ir al paso 5.
2. Instalar Python3
3. Instalar pip 
4. Instalar virtualenv mediante "pip install virtualenv". 
5. Crear un virtual env mediante "mkvirtualenv InnoverAPI".
6. Ir al folder donde clonamos el repo y correr el siguiente comando "setprojectdir .", mediante esto cada vez que ingresemos al entorno se´redireccionará al folder. Para salir del entorno tenemos que usar "deactivate" y para regresar "workon InnoverAPI". Si todo funciona debería de salirnos **(InnoverAPI)** antes de nuestro cursor en la consola.
7. Correr "pip install -r requirements.txt"
8. Correr  "gunicorn innover:app"
9. En nuestra url local en el puerto 5000 se debería ver un mensaje.