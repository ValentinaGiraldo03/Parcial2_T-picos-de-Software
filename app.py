from flask import Flask


app = Flask(__name__)

def calcular_factorial(numero):
    if numero < 0:
        return None  
    elif numero in (0, 1):
        return 1
    return numero * calcular_factorial(numero - 1)

@app.route('/factorial/<int:numero>')
def obtener_factorial(numero):
    resultado = calcular_factorial(numero)
    if resultado is None:
        return "El factorial no está definido para números negativos", 400
    return f"El factorial de {numero} es {resultado}"


if __name__ == '__main__':
    app.run(debug=True)
