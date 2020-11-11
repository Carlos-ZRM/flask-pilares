# librerias
from flask import Flask , request, Response , json ,redirect, url_for , render_template
from PIL import Image
import random
import io

# crear una aplicacion 
app = Flask(__name__)

def db ():
    "JSON es un tipo de documento que define datos"
   
    bob = {
        "nombre":"Bob Esponja",
        "ruta": "static/img/esponjin.jpg"
        }
    pat = {
       "nombre":"Patricio",
       "ruta":"static/img/patricio.jpg"
        }
    arenita = {
       "nombre":"Arenita",
       "ruta":"static/img/mejillas.jpg",
        }
    ca = {
       "nombre":"Calamardo",
       "ruta":"static/img/calamardo.jpg",
        }
    ga = {
       "nombre":"Gary",
       "ruta":"static/img/gary.jpg",
        }
    don = {
       "nombre":"Don Cangrejo",
       "ruta":"static/img/doncangrejo.jpg",
        }
    li = {"Bob Esponja":bob, "Patricio":pat, "Arenita":arenita, "Calamardo":ca, 
          "Gary":ga, "Don Cangrejo":don }
    return li


@app.route('/txt')
def hello_world():
    base_datos = db()
    llaves = list(base_datos.keys())
    aleatorio = random.randint(0, len(llaves)-1 ) 
   
    llave_ale = llaves[aleatorio]

    key = llave_ale
    value = base_datos[key]

    return 'Tu eres '+ str(value) + " \n"+key

@app.route('/json')
def hello_json():

    base_datos = db()
    llaves = list(base_datos.keys())
    aleatorio = random.randint(0, len(llaves)-1 ) 

    
    llave_ale = llaves[aleatorio]

    key = llave_ale
    value = base_datos[key]

    
    myjson = json.dumps(value)
   
    respuesta = Response(response=myjson,
                         status=200, 
                         mimetype='application/json'
                         )
    # retornar la respuesta creada 
    return respuesta

@app.route('/img')
def response_imagen():
    base_datos = db()
    llaves = list(base_datos.keys())
    aleatorio = random.randint(0, len(llaves)-1 ) 

    
    llave_ale = llaves[aleatorio]

    key = llave_ale
    diccionario_al = base_datos[key]
    ruta = diccionario_al["ruta"]
    output = io.BytesIO()   
    image = Image.open( ruta)
    image.save(output, 'JPG')
    
    
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/')
def index():
    return render_template("imagen.html")

@app.route('/variable/<int:entero>')
def variable_url(entero):

    variable = str(entero)
    respuesta = Response(response=variable,
                         status=200, 
                         mimetype='text/txt'
                         )
    # retornar la respuesta creada 
    return respuesta

@app.route('/variable/render/<int:entero>')

def variable_render(entero):
    print(entero)
    return render_template('variable.html', variable_html=str(entero))

@app.route('/img-render')
def render_imagen():
    base_datos = db()
    llaves = list(base_datos.keys())
    aleatorio = random.randint(0, len(llaves)-1 ) 

    
    llave_ale = llaves[aleatorio]

    key = llave_ale
    diccionario_al = base_datos[key]
    ruta = diccionario_al["ruta"]
    
    nombre_d = diccionario_al["nombre"]
    
    return render_template('imagen-render.html', imagen_render=ruta, nombre = nombre_d)

@app.route("/formulario/", methods=["GET", "POST"])
def show_signup_form():
    if request.method == 'POST':
        nombre = request.form['Nombre']
        mensaje = request.form['Mensaje']
        print("nombre"+nombre+"mensaje"+mensaje)
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return "nombre"+nombre+"mensaje"+mensaje
        #return redirect(url_for('hello_world'))
    return render_template('formulario.html')
    #return "nombre"+nombre+"mensaje"+mensaje

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
