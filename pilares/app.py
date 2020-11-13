
from flask import Flask , request, Response , json ,redirect, url_for , render_template
from PIL import Image
import random
import io

# crear una aplicacion 
app = Flask(__name__)

def db_naruto ():
    "JSON es un tipo de documento que define datos"
  
    naruto = {
        "nombre":"Naruto Uzumaki",
        "ruta":"static\img\septimo.gif"
        }
    sasuke = {
       "nombre":"Sasuke Uchiha",
       "ruta":"static\img\sasuke.gif"
        }
    sakura = {
       "nombre":"Sakura Haruno",
       "ruta":"static\img\sakura.gif"
        }
    konan = {
       "nombre":"Konan Akatsuki",
       "ruta":"static\img\konan.gif"
        }
    itachi = {
       "nombre":"Itachi Uchiha",
       "ruta":"static\img\itachi.gif"
        }
    obito = {
       "nombre":"Obito Uchiha",
       "ruta":"static\img\obito.gif"
        }
    li = {"naruto":naruto, "sasuke":sasuke, "sakura":sakura, "konan":konan, "itachi":itachi,
          "obito":obito}
    return li
def db_bobesponja ():
    "JSON es un tipo de documento que define datos"
   
    bob = {
        "nombre":"Bob Esponja",
        "ruta": "static\img\esponjin.jpg"
        }
    pat = {
       "nombre":"Patricio",
       "ruta":"static\img\patricio.jpg"
        }
    arenita = {
       "nombre":"Arenita",
       "ruta":"static\img\mejillas.jpg",
        }
    ca = {
       "nombre":"Calamardo",
       "ruta":"static\img\calamardo.jpg",
        }
    ga = {
       "nombre":"Gary",
       "ruta":"static\img\gary.jpg",
        }
    don = {
       "nombre":"Don Cangrejo",
       "ruta":"static\img\doncangrejo.jpg",
        }
    li = {"Bob Esponja":bob, "Patricio":pat, "Arenita":arenita, "Calamardo":ca, 
          "Gary":ga, "Don Cangrejo":don }
    return li

@app.route('/naruto')
def render_naruto():
    base_datos = db_naruto()
    llaves = list(base_datos.keys())
    aleatorio = random.randint(0, len(llaves)-1 ) 

    
    llave_ale = llaves[aleatorio]

    key = llave_ale
    diccionario_al = base_datos[key]
    ruta = diccionario_al["ruta"]
    nombre_d = diccionario_al["nombre"]
    
    
    return render_template('naruto-render.html', imagen_render=ruta, nombre = nombre_d)

@app.route('/bobesponja')
def render_bobesponja():
    base_datos = db_bobesponja()
    llaves = list(base_datos.keys())
    aleatorio = random.randint(0, len(llaves)-1 ) 

    
    llave_ale = llaves[aleatorio]

    key = llave_ale
    diccionario_al = base_datos[key]
    ruta = diccionario_al["ruta"]
    
    nombre_d = diccionario_al["nombre"]
    
    return render_template('bobesponja-render.html', imagen_render=ruta, nombre = nombre_d)

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')