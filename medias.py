from flask import render_template, Flask, request
import firebase_admin
from firebase_admin import credentials, firestore
import os
app = Flask(__name__)

cred = credentials.Certificate("chave-firebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def principal():
    return render_template("principal.html")


@app.route('/media', methods=['POST'])
def calcularmedia():
    nome = request.form['nome']
    a = float(request.form['num1'])
    b = float(request.form['num2'])
    resultado = (a + b) / 2

    db.collection('alunos').add({
        'nome': nome,
        'nota1': a,
        'nota2': b,
        'media': resultado
    })

    return render_template('resultado.html', media=round(resultado, 2))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
