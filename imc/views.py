from .models import *
from sqlalchemy.orm import joinedload
from flask import abort, render_template, request, jsonify
from flask_cors import CORS
from datetime import datetime

def init_app(app):

    CORS(app)
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/pacientes', methods=['POST'])
    def pacientes():
        try:
            payload = request.get_json()
            cadastro = Paciente.query.filter_by(nome=payload['nome'].upper()).first()
            
            if cadastro==None:
                cadastro = Paciente(
                    nome=payload['nome'].upper(),
                    endereco=payload['endereco'].upper(),
                )

            registro = HistoricoPaciente(
                peso=payload['peso'],
                altura=payload['altura'],
                imc=payload['imc'],
                idade=payload['idade'],
                data= datetime.now(),
                paciente=cadastro
            )
            db.session.add(registro)
            db.session.commit()
            return jsonify({'status':'Salvo Com Sucesso!'})
        except Exception as e:
            return jsonify({'status':e})
        
    @app.route('/historicos', methods=['GET']) 
    def historico():
        if request.method == 'POST':
            payload = request.get_json()
            cadastro = Paciente.query.filter_by(nome=payload['nome'])
            if cadastro:
                print('cadastro encontrado')
                return 'ok'

        query = Paciente.query.options(joinedload('historico'))
        if query:
            result = []
            for paciente in query.all():
                result.append({
                        'nome':paciente.nome.title(),
                        'historico':[hist.serialize for hist in paciente.historico]
                    }
                )
            response = jsonify(result)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        return []
