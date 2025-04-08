# import the necessary packages
from flask import Flask
from flask import render_template, jsonify, request

app = Flask(__name__)

# Almacena los datos recibidos aquí
received_data = []

# This is the main route of the application
# The route is defined using the @app.route decorator
@app.route('/')

# Set the function name to be the same as the route
# This function will be called when the route is accessed
@app.route('/index')
def index():
    user = {'username': 'Lucas'}
    return render_template('index.html', title='Checker', user=user)

@app.route('/health', methods=['GET'])
def webHealthCheck():
    return "WEB working properly!", 200

@app.route('/data', methods=['GET'])
def showReceivedData():
    
    if len(received_data) == 10:
        received_data.pop(0)

    return jsonify(received_data)

@app.route('/receiver', methods=['POST'])
def processDataReceived():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se proporcionó JSON"}), 400

    if 'msg' not in data:
        return jsonify({"error": "Faltan datos en el JSON recibido"}), 400

    # Guarda los datos recibidos
    received_data.append(data)

    respuesta = {
        "msg": data['msg']
    }
    return jsonify(respuesta), 200

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=3000)