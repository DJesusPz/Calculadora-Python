from flask import Flask, render_template, request

app = Flask(__name__)

# Rutas para la página principal y redirecciones a los ejercicios
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET'])
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/ejercicio1', methods=['POST'])
def calcular_ejercicio1():
    x_valor = float(request.form['x'])
    z_valor = float(request.form['z'])
    resultado = x_valor * z_valor + z_valor + x_valor
    return render_template('resultado.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET'])
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/ejercicio2', methods=['POST'])
def calcular_ejercicio2():
    numero_ingresado = int(request.form['numero'])
    tabla = [(numero_ingresado, i, numero_ingresado * i) for i in range(1, 11)]
    return render_template('tabla.html', tabla=tabla)

@app.route('/ejercicio3', methods=['GET'])
def ejercicio3():
    return render_template('ejercicio3.html')

@app.route('/ejercicio3', methods=['POST'])
def calcular_ejercicio3():
    radio_circulo = float(request.form['radio'])
    lado_cuadrado = float(request.form['lado_cuadrado'])
    base_triangulo = float(request.form['base_triangulo'])
    altura_triangulo = float(request.form['altura_triangulo'])

    area_circulo = 3.1415 * radio_circulo**2
    area_cuadrado = lado_cuadrado**2
    area_triangulo = 0.5 * base_triangulo * altura_triangulo

    return render_template('areas.html', area_circulo=area_circulo, area_cuadrado=area_cuadrado, area_triangulo=area_triangulo)

if __name__ == '__main__':
    app.run(debug=True)


