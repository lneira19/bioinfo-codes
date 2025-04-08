# import the necessary packages
from flask import Flask, render_template, jsonify
import requests 

app = Flask(__name__)

# Configura las URLs del servidor
health_url = "http://192.168.0.100:3000/health"
receiver_url = "http://192.168.0.100:3000/receiver"


# This is the main route of the application
# The route is defined using the @app.route decorator
@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html')

# Mensaje a enviar
msg = "Ivo!"

# Enviar datos JSON a URL especificada
@app.route('/sender')
def sendDataToURL():
    global msg

    datos = {
        "msg": msg
    }

    if msg == "Campeón!":
        msg = "Ivo!"
    else:
        msg = "Campeón!"

    try:
        # Envía los datos JSON al servidor con requests.post
        response = requests.post(receiver_url, json=datos)
        if response.status_code == 200:
            print("Respuesta del servidor:", response.json())
        else:
            print("Error:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error al conectar con el servidor:", e)


    # Define the function you want to send
    function_code = """
        console.log('Function from server executed!');
    """
    return jsonify({'function': function_code})

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=4000)

