from flask_restx import fields
from extensions import api

municipio_model = api.model("Municipio", {
     "id_municipio": fields.Integer,
     "nome_municipio": fields.String
      
})

cidade_model = api.model("Cidade", {
    "id_cidade": fields.Integer,
    "nome_cidade": fields.String,
    "municipios":fields.List(fields.Nested(municipio_model))
    
})

cidade_input_model = api.model("CidadeInput", {
       "nome_cidade":fields.String
})

municipio_input_model = api.model("MunicipioInput", {
      "nome_municipio":fields.String,
      "cidade_id":fields.Integer 
})

