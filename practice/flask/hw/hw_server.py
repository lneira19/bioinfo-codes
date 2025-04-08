# import the necessary packages
from flask import Flask

app = Flask(__name__)

# This is the main route of the application
# The route is defined using the @app.route decorator
@app.route('/')

# Set the function name to be the same as the route
# This function will be called when the route is accessed
@app.route('/index')
def index():

    return "¡Hola, Mundo!",200

if __name__ == '__main__':
    app.run(debug=True)