from extensions import db

class Cidade(db.Model):
    id_cidade = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_cidade = db.Column(db.String(50), unique=True)
    municipios = db.relationship("Municipio", backref="cidade")

class Municipio(db.Model):
    id_municipio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_municipio = db.Column(db.String(50), unique=True)
    cidade_id = db.Column(db.Integer,db.ForeignKey("cidade.id_cidade"))

    




   
