from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import requests
import os
from PIL import Image
import align
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html'), 200

# Carpeta donde se almacenan las imágenes subidas
cwd = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(cwd,'static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

SAVE_FOLDER = os.path.join(cwd,'static/received')
app.config['SAVE_FOLDER'] = SAVE_FOLDER

DATA_FOLDER = os.path.join(cwd,'static/data')
app.config['DATA_FOLDER'] = DATA_FOLDER

datajson = dict()

# Pasaje de strings entre HTMLs
@app.route('/send', methods=['POST'])
def sendData():

    # Obtener las secuencias
    seq1 = request.form.get('seq1')
    seq2 = request.form.get('seq2')
    file = request.files['file']

    seqA, seqB, score = align.align_sequences(seq1, seq2)

    # Guardamos la secuencia consenso y el score en un archivo CSV
    with open(f'{DATA_FOLDER}/secuencias.csv', mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([seq1,seq2,seqA,seqB, score])

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        filepath_for_html = f"../static/uploads/{filename}"

        with open(filepath, 'rb') as img_file:
            response = requests.post('http://127.0.0.1:5001/convert', files={'file': img_file})

    global datajson
    
    datajson = dict({
        'seq1': seq1,
        'seq2': seq2,
        'seqA': seqA,
        'seqB': seqB,
        'score': score,
        'filepath': filepath_for_html
    })

    return render_template('dataview.html', datajson=datajson), 200

@app.route('/receive', methods=['POST'])
def receiveImg():
    if 'file' not in request.files:
        return 'No hay archivo para convertir', 400
    
    file = request.files['file']

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['SAVE_FOLDER'], filename)
        file.save(filepath)
        filepath_for_html = f"../static/received/{filename}"
    
    # Crear diccionario con datos
    global datajson

    datajson['converted_img'] = filepath_for_html

    return 'Imagen recibida y guardada', 200


if __name__ == '__main__':

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)

    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    app.run(debug=True,port=5000)