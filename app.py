from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("views/index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    # Obtener datos enviados en el cuerpo de la solicitud
    datos = request.get_json()
    _ecuacion = datos.get("Ecuacion")
    _y = datos.get("valorY")
    _x = datos.get("valorX")
    _n = datos.get("valorN")
    # Validar que los datos existan
    if not datos:
        return jsonify({"error": "No se enviaron parámetros"}), 400
    # Ejemplo: Retornar los mismos datos en formato JSON
    convertido= obtenerNumeros(_ecuacion)
    tipo = clasificarEcuacion(_ecuacion)
    return jsonify({
        "Void":tipo
    })

def obtenerNumeros(_ecuacion):
    # Usamos una comprensión de lista para filtrar solo los dígitos
    numeros = ''.join([caracter for caracter in _ecuacion if caracter.isdigit()])
    return numeros

def clasificarEcuacion(ecuacion):
    # Verificar si la ecuación contiene variables 'x' y 'y'
    if "x" in ecuacion and "y" in ecuacion:
        # Verificar si la ecuación incluye multiplicaciones simples (linealidad)
        if "*" not in ecuacion and "^" not in ecuacion:
            return "lineal"
        # Si hay multiplicación y otros términos complejos, es no lineal
        elif "*" in ecuacion or "^" in ecuacion:
            return "no lineal"
        else:
            return "desconocida"
    else:
        # Si no contiene las variables necesarias, es desconocida
        return "desconocida"



if __name__ == "__main__":
    app.run(debug=True)
