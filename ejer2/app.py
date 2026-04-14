from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/proceso", methods=["POST"])
def proceso():
    # Obtener el nombre del formulario
    nombre = request.form.get("nombre")
    
    # Obtener la lista de lenguajes seleccionados (checkboxes)
    lenguajes = request.form.getlist("lenguajes")
    
    # Enviar los datos a la plantilla de salida
    return render_template("salida.html", nombre=nombre, lenguajes=lenguajes)

if __name__ == "__main__":
    app.run(debug=True)