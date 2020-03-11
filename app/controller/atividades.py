from app import app
from flask import render_template, request
from app.models.tables import Atividades
import os
import uuid

@app.route('/atividades')
def listar_atividades():
    a = Atividades.query.all()
    for i in range(len(a)):
        a[i].data = a[i].data.strftime('%d/%m%Y')
    return render_template("atividades_listar.html", atividades=a)

@app.route('/atividades/novo')
def form_nova_atividade():
    tipo="inserir"
    return render_template("atividades_formulario.html", tipo=tipo)

@app.route('/atividades/novo', method=['POST'])
def inserir_atividade():
    arquivo = request.files['arquivo']
    arquivo.filename = str(uuid.uuid4()) + os.path.sliptex(arquivo.filename)[1]
    return ""
