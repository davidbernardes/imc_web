from .database import db

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    endereco = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return self.nome.title()

class HistoricoPaciente(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    paciente = db.relationship('Paciente', backref=db.backref('historico', lazy=True))
    idade = db.Column(db.Integer)
    peso = db.Column(db.Float)
    altura = db.Column(db.Integer)
    imc = db.Column(db.Float)
    data = db.Column(db.DateTime)

    @property
    def serialize(self):
        hist = {
                'data':self.data,
                'idade':self.idade,
                'peso': self.peso,
                'altura': self.altura,
                'imc':self.imc
            }

        return hist

