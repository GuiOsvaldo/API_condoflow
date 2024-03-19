from flask_restx import Resource, Namespace
from api_models import cidade_model, cidade_input_model
from models import Cidade
from extensions import db
#from extensions import db
#from models import
#Cidade, Municipio, Bairro, Endereco, TipoUsuario, Usuario, Status, Bloco,
#Condominio, Pessoa, Sindico, Estacionamento, Unidades
#

ns = Namespace("api/v1")

######## endopoint localhost:5000/api/v1/usuarios -> Lista todos usuários ###########

@ns.route("/cidade")
class Cidades(Resource):
    @ns.marshal_list_with(cidade_model)
    def get(self):
        return Cidade.query.all()
    
    @ns.expect(cidade_input_model)  
    @ns.marshal_list_with(cidade_model)
    def post(self):
        cidade = Cidade(name=ns.payload["nome_cidade"])
        db.session.add(cidade)
        db.session.commit()
        return cidade, 201
    
@ns.route("/cidade/<int:id>")
class Cidade(Resource):
    @ns.marshal_with(cidade_model)
    def get(self, id):
        cidade = Cidade.query.get(id)
        return cidade

@ns.expect(cidade_input_model)
@ns.marshal_with(cidade_model)
def put(self, id):
    cidade = Cidade.query.get(id)
    cidade.nome_cidade = ns.payload["nome_cidade"]
    db.session.commit()
    return cidade
           
def delete(self, id):
    cidade = Cidade.query.get(id)
    db.session.delete(cidade)
    db.session.commit()
    return {}, 204


########## Fim do Endpoint usuários #################



    



  