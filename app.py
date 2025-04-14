from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

personas = []

@app.route("/agregar", methods =["POST"])
def agregar():
    data = request.get_json()
    nombre = data.get("nombre")
    apellido = data.get("apellido")
    dni = data.get("dni")
    telefonos = data.get("telefonos")
    hijos = data.get("hijos")

    personas.append({"Nombre":nombre, "Apellido":apellido,"DNI":dni, "Telefonos":telefonos, "Hijos": hijos })


if __name__ == "__main__":
    app.run(debug=True)


