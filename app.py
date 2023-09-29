import flask
from flask import Flask, request, jsonify
from pymongo import MongoClient


mongopass = "mongodb://localhost:27017/Database"  # Defina a URI corretamente

app = Flask(__name__)
app.config["DEBUG"] = False

client = MongoClient(mongopass)  # Crie o cliente MongoDB com a URI
db = client.Database
colecao = db.Midiateca

# Resto do seu código Flask...

# requisitar todos
@app.route('/Midiateca', methods=['GET'])
def obter_obras():
    obras = db.mycollection.find()

    return jsonify([obras for obras in obras])  # Corrigido "flask.jsonify" para "jsonify"

# requisitar somente 1
@app.route('/Midiateca/<int:id>', methods=['GET'])  # Corrigido "method" para "methods"
def obter_obra_por_id(id):
    obra = db.mycollection.find_one({"_id": id})  # Corrigido 'id:' para 'id'

    return jsonify(obra)  # Corrigido "flask.jsonify" para "jsonify"

# editar
@app.route('/Midiateca/<int:id>', methods=['POST'])  # Corrigido "method" para "methods"
def editar_obra_id(id):
    obra_alt = request.get_json()
    obra_alterada = db.mycollection.find_one_and_update(
        {"_id": id}, {'$set': {'titulo': obra_alt['titulo']}}
    )
    return jsonify(obra_alterada)  # Corrigido "flask.jsonify" para "jsonify"

# criar
@app.route('/Midiateca', methods=['POST'])  # Corrigido "method" para "methods"
def adicionar_obra():
    nova_obra = request.get_json()
    db.mycollection.insert_one(nova_obra)

    return jsonify(message="adicionado com sucesso")  # Corrigido "flask.jsonify" para "jsonify"

# excluir
@app.route('/Midiateca/<int:id>', methods=['DELETE'])  # Corrigido "method" para "methods"
def excluir_obra(id):
    db.mycollection.delete_one({'_id': id})

    return jsonify(message="obra excluída com sucesso")  # Corrigido "flask.jsonify" para "jsonify"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
