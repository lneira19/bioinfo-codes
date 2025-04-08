# import the necessary packages
from flask import Flask
from flask import render_template

app = Flask(__name__)

# This is the main route of the application
# The route is defined using the @app.route decorator
@app.route('/')

# Set the function name to be the same as the route
# This function will be called when the route is accessed
@app.route('/index')
def index():
    user = {'username': 'Lucas'}
    return render_template('index.html', title='Casita', user=user)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=3000)