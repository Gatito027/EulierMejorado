from flask import Flask, render_template, request, jsonify
from controllers.euler_controller import metodo_euler_mejorado, euler_mejorado, datos_grafica

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.json
    ecuacion = data["ecuacion"]
    x0 = float(data["x0"])
    y0 = float(data["y0"])
    h = float(data["h"])
    n = int(data["n"])

    resultados = metodo_euler_mejorado(ecuacion, x0, y0, h, n)
    x_vals, y_aprox, y_exact, errores = euler_mejorado(x0, y0, h, n)
    datos = datos_grafica(x_vals, y_aprox, y_exact)

    return jsonify({
        "tabla": resultados,
        "grafica": datos
    })

if __name__ == "__main__":
    app.run(debug=True)

