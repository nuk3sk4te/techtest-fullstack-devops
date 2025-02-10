from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'imagenes.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    return db

@app.route('/imagenes', methods=['GET'])
def get_imagenes():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM imagenes')
    imagenes = cursor.fetchall()
    db.close()
    return jsonify(imagenes)

@app.route('/imagenes', methods=['POST'])
def add_imagen():
    # ... (código para añadir una imagen a la base de datos)

@app.route('/imagenes/<int:id>', methods=['DELETE'])
def delete_imagen():
    # ... (código para eliminar una imagen de la base de datos)

@app.route('/imagenes/<int:id>', methods=['PUT'])
def edit_imagen():
    # ... (código para editar una imagen en la base de datos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')