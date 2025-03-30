from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("views/index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    # Obtener datos enviados en el cuerpo de la solicitud
    datos = request.get_json()
    ecuacion = datos.get("Ecuacion")
    y = datos.get("valorY")
    x = datos.get("valorX")
    h = datos.get("valorH")
    jsonres= {"n":"0","xn":"1","yn":"1","yreal":"1","error":"0"},{"n":"1","xn":"1","yn":"1","yreal":"1","error":"0"},{"n":"2","xn":"1","yn":"1","yreal":"1","error":"0"}
    # Validar que los datos existan
    if not datos:
        return jsonify({"error": "No se enviaron parámetros"}), 400
    return jsonify(jsonres)




if __name__ == "__main__":
    app.run(debug=True)
