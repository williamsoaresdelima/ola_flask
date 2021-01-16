from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route("/number/<numero>", methods=['GET', 'POST'])
def ola(numero):
    return 'oie Flask {}'.format(numero)


@app.route('/<int:id>')
def pessoa(id):
    soma = 1 + id
    return jsonify({'id': id, 'nome': 'willl', 'aa': 'ds', 'soma': soma})


@app.route('/soma/<int:valor1>/<int:valor2>/')
def soma(valor1, valor2):
    return jsonify({'soma': valor1 + valor2})


@app.route('/somajs', methods=['POST', 'GET'])
def somajs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 10
    return jsonify({'somaJS': total})


if __name__ == "__main__":
    app.run(debug=True)
