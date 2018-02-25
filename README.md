[![Estatus del build](https://travis-ci.com/NotZombieFood/innoverAPI.svg?token=UsGfg3kACvQ8anUCPNyh&branch=master)](https://travis-ci.com/NotZombieFood/innoverAPI)
[![Lenguaje](https://img.shields.io/badge/Lenguaje-Python-blue.svg)](https://travis-ci.com/NotZombieFood/innoverAPI)
[![Slack](https://img.shields.io/badge/Autor-Basiko-yellow.svg?logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAZFJREFUeNp8kruLE1EUxn8TEteEZMzELQR1N8wa2EJMJ7ikt9p%2FQexUEBvBF4iVzXYprASLZUlloyAqgshWKfIyWAQJFqImxjiwaNZXkuPJzcMJSTzwFXPm%2B91z%2Bc61RIRxBQ66ZNI%2F2N1pwm9t%2FOFf9TjMKb4SGvoDvl%2FIL4t0SgnHGAd1UfWWrgIrXPlZs3xmnTgWwSSVXAhpa79EWsraLqreqRrEprz%2Bj8zpI6gJeUNQoZYBK6pvrF8%2F77AQvH8ninS0V%2BT5ZJrHtVLuwJRvBvReBZD33DTQQFVeyCdmoBlQ9jhrpgzBj9KC%2FIOlueBUqnT4THCUJ4R1JSkn0WNu%2BU%2BpPdREW2xoosOpJTwNJnT1nPP%2Fq96%2BFEe%2Bm3BujUCRDzzx8gFi9upicM09Sv%2B19uqqMs8MXDDruPAoG1kMgsvTe2FMv2B22TZTq6p9Nu9ePjTxWv63GrWTJOw%2BL7cbnDjThTonEX12XSLY1PS1buHIbDiuewwsl%2BX4cYqPdekeg7CQL6om5ibZG7bx%2FhVgAFxSe7B%2FyBevAAAAAElFTkSuQmCC)](https://basiko.slack.com)
[![Website](https://img.shields.io/badge/Website-Innover-green.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAQAAAC1QeVaAAAA70lEQVQY013QPUuCYRiG4aclG5qlrVp1K9SIqFWlD0iwralyiFd8p0ptaMoaioRwKoTEJiEcKn/d0ZDax72ey30dIYQQQhAkFAwNFSSE6QlmpJ2riEQqzqXNGKekE5dy1vX0rMtoOJEUgkUDp2YVVcVqIrGUUwOLQVbHjSPLVnV1rdgxcq8jG6w5Vvag61VT04s7D8qOrX3HkrwL1z6NnNmSV/ofW969u1VXsP8Ty9qe9TXV9Tx5dPAdszrujWxbGT9U9KHlSm4yJSUWqYlFYmmH2pYmCA0ZG/pThIoFv/gubNpT/cM39Z0zb9fbb/gvvC7zcIQtJxIAAAAASUVORK5CYII=)](https://beta.innover.mx)
[![Requisitos](https://img.shields.io/badge/Requisitos-Actualizados-green.svg)](https://github.com/NotZombieFood/innoverAPI/blob/master/requirements.txt)


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