from extensions import db

class Cidade(db.Model):
    id_cidade = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_cidade = db.Column(db.String(50), unique=True)
    municipios = db.relationship("Municipio", backref="cidade")

class Municipio(db.Model):
    id_municipio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_municipio = db.Column(db.String(50), unique=True)
    cidade_id = db.Column(db.Integer,db.ForeignKey("cidade.id_cidade"))
    bairros = db.relationship("Bairro", backref="municipio")
 
class Bairro(db.Model):
    id_bairro = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_bairro = db.Column(db.String(50), nullable=False)
    municipio_id = db.Column(db.Integer, db.ForeignKey("municipio.id_municipio"))
    enderecos = db.relationship("Endereco", backref="bairro")

class Endereco(db.Model):
    id_endereco = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_endereco = db.Column(db.String(50), nullable=False)
    bairro_id = db.Column(db.Integer, db.ForeignKey("bairro.id_bairro"))
    pessoas = db.relationship("Pessoa", backref="endereco")
    condominios = db.relationship("Condominio", backref="endereco")

class Status(db.Model):
    id_status = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_status = db.Column(db.Boolean)
    pessoas = db.relationship("Pessoa", backref="status")
    estacionamento = db.relationship("Estacionamento", backref="status")

class Tipousuario(db.Model):
    id_tipo_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_tipo_usuario = db.Column(db.String(50), nullable=False)
    usuarios = db.relationship("Usuario", backref="tipousuario")

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email_usuario = db.Column(db.String(50), nullable=False)
    senha_usuario = db.Column(db.String(50), nullable=False)
    usuario_tipo_id = db.Column(db.Integer, db.ForeignKey("tipousuario.id_tipo_usuario"))
   

class Pessoa(db.Model):
    id_pessoa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_pessoa = db.Column(db.String(50), nullable=False)
    telefone_pessoa = db.Column(db.String(50), nullable=False)
    endereco_id = db.Column(db.Integer, db.ForeignKey("endereco.id_endereco"))
    status_id = db.Column(db.Integer, db.ForeignKey("status.id_status"))
    bi_pessoa = db.Column(db.String(13), unique=True)
    moradors = db.relationship("Morador", backref="pessoa")
    visitantes = db.relationship("Visitante", backref="pessoa")
    sindicos = db.relationship("Sindico", backref="pessoa")

class Morador(db.Model):
    id_morador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    morador_id = db.Column(db.Integer, db.ForeignKey("pessoa.id_pessoa"))

class Visitante(db.Model):
    id_visitante = db.Column(db.Integer, primary_key=True, autoincrement=True)
    visitante_id = db.Column(db.Integer, db.ForeignKey("pessoa.id_pessoa"))

class Sindico(db.Model):
    id_sindico = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sindico_id = db.Column(db.Integer, db.ForeignKey("pessoa.id_pessoa"))
    condominios = db.relationship("Condominio", backref="sindico")
    categorias = db.relationship("Categoria", backref="sindico")
    estacionamentos = db.relationship("Estacionamento", backref="sindico")     
        
class Tipocondominio(db.Model):
    id_tipo_condominio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_tipo_condominio = db.Column(db.String(50), nullable=False)
    condominios = db.relationship("Condominio", backref="tipocondominio")
    
class Condominio(db.Model):
    id_condominio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_condominio = db.Column(db.String(50), nullable=False)
    tipo_condominio_id = db.Column(db.Integer, db.ForeignKey("tipocondominio.id_tipo_condominio"))
    sindico_id = db.Column(db.Integer, db.ForeignKey("sindico.id_sindico"))
    endereco_id = db.Column(db.Integer, db.ForeignKey("endereco.id_endereco"))
    blocos = db.relationship("Bloco", backref="condominio")

class Bloco(db.Model):
    id_bloco = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_bloco = db.Column(db.String(50), nullable=False)
    condominio_id = db.Column(db.Integer, db.ForeignKey("condominio.id_condominio"))
    unidades = db.relationship("Unidade", backref="bloco")
    estacionamentos = db.relationship("Estacionamento", backref="bloco")

class Tipounidade(db.Model):
    id_tipo_unidade = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_tipo_unidade = db.Column(db.String(50), nullable=False)
    unidades = db.relationship("Unidade", backref="tipounidade")

class Unidade(db.Model):
    id_unidade = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_unidade = db.Column(db.Integer)
    numero_quarto_unidade = db.Column(db.Integer)
    metragem_unidade = db.Column(db.String(50), nullable=False)
    unidade_id = db.Column(db.Integer, db.ForeignKey("tipounidade.id_tipo_unidade"))
    bloco_id = db.Column(db.Integer, db.ForeignKey("bloco.id_bloco"))
    salaos = db.relationship("Salao", backref="unidade")


class Salao(db.Model):
    id_salao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_salao = db.Column(db.String(50), nullable=False)
    unidade_id = db.Column(db.Integer, db.ForeignKey("unidade.id_unidade"))


class Categoria(db.Model):
    id_categoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_categoria = db.Column(db.String(50), nullable=False)
    sindico_id = db.Column(db.Integer, db.ForeignKey("sindico.id_sindico"))

class Tipoestacionamento(db.Model):
    id_tipo_estacionamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_tipo_estacionamento = db.Column(db.String(50), nullable=False)
    estacionamentos = db.relationship("Estacionamento", backref="tipoestacionamento")    

class Estacionamento(db.Model):
    id_estacionamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    serie_estacionamento = db.Column(db.String(50), nullable=False)
    sindico_id = db.Column(db.Integer, db.ForeignKey("sindico.id_sindico"))
    bloco_id = db.Column(db.Integer, db.ForeignKey("bloco.id_bloco"))
    tipo_estacionamento_id = db.Column(db.Integer, db.ForeignKey("tipoestacionamento.id_tipo_estacionamento"))
    status_id = db.Column(db.Integer, db.ForeignKey("status.id_status"))

