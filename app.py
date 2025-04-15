from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

personas = []

# Agrega al array un objeto de la persona
@app.route("/agregar", methods =["POST"])
def agregar():
    data = request.get_json()
    nombre = data.get("nombre")
    apellido = data.get("apellido")
    dni = data.get("dni")
    telefonos = data.get("telefonos")
    hijos = data.get("hijos")

    personas.append([nombre,apellido,dni,telefonos,hijos] )

    return "" , 200

# Envia el array a front
@app.route("/mostrar", methods = ["GET"])
def mostrar():
    return(personas)

# Buscar por dni
@app.route("/buscar/<dni>",methods = ["GET"])
def buscar(dni):
    for persona in personas:
        if persona[2] == dni:
            return jsonify({
                "nombre":persona[0],
                "apellido":[1],
                "dni":persona[2],
                "telefonos":persona[3],
                "hijos":persona[4] 
            })
    return jsonify({"No se encuentra una persona con ese dni"})
        


if __name__ == "__main__":
    app.run(debug=True)


