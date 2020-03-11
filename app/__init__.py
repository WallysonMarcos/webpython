from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://suporte:$uportE99@localhost/atividades'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + 'static/uploads'

from app.models.tables import Usuario
from app.models.tables import Atividade
from app.controller import atividades

@app.route('/home')
def home():
    title = "Lista de Atividades"
    lista = ['Atividade 1', 'Atividade 2']
    return render_template('index.html', titulo=title, eventos=lista)


