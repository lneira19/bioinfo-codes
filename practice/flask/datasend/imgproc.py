from flask import Flask, request, send_file, redirect, url_for
from PIL import Image
import io, os
from datetime import datetime
import requests

app = Flask(__name__)

# Carpeta donde se guardarán las imágenes convertidas
cwd = os.path.dirname(__file__)
SAVE_FOLDER = os.path.join(cwd,'static/converted_sv2')

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

@app.route('/convert', methods=['POST'])
def convert_to_grayscale():
    if 'file' not in request.files:
        return 'No hay archivo para convertir', 400

    file = request.files['file']
    img = Image.open(file)

    # Convertir la imagen a escala de grises
    grayscale_img = img.convert('L')

    # Generar un nuevo nombre de archivo con la fecha actual
    original_filename = file.filename.rsplit('.', 1)[0]
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    new_filename = f"{original_filename}_{timestamp}.jpg"

    # Guardar la imagen en la carpeta "static/converted" con el nuevo nombre
    filepath = os.path.join(SAVE_FOLDER, new_filename)
    grayscale_img.save(filepath)

    with open(filepath, 'rb') as img_file:
        response = requests.post('http://127.0.0.1:5000/receive', files={'file': img_file})

    # Devolver la imagen en escala de grises como archivo
    #return send_file(filepath, mimetype='image/jpeg')
    return 'Imagen enviada',200


if __name__ == '__main__':
    
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)
    
    app.run(debug=True, port=5001)
