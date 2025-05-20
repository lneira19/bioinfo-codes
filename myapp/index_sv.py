# Bibliotecas necesarias
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os

# Creación de la app
app = Flask(__name__)
app.secret_key = os.urandom(24)

# *** LOG-IN CONFIGURATION ***
# Configuración del login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Modelo de usuario
class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    # Aquí deberías cargar el usuario desde tu base de datos
    # Por simplicidad, asumimos que el usuario es correcto
    return User(user_id)


# *** APP CONFIGURATION ***
@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    
    if request.method == "POST":
        
        username = request.form['username']
        password = request.form['password']

        # Aquí deberías verificar el usuario y la contraseña con tu base de datos
        # Por simplicidad, asumimos que el usuario y la contraseña son correctos
        if username == 'admin' and password == '123':
            
            user_obj = User(0)
            login_user(user_obj)

            # Redirigir a la página principal después de iniciar sesión
            return redirect(url_for('index'))
        else:
            return 'Usuario o contraseña incorrectos'
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)