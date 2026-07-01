from sqlalchemy import Column, String, Integer, Date, Numeric, DateTime, ForeignKey, Table
from sqlalchemy.sql import func
from config.database import Base

responsavel_paciente = Table(
    'responsavel_paciente',
    Base.metadata,
    Column('cpf_paciente', String, ForeignKey('paciente.cpf_paciente'), primary_key=True),
    Column('cpf_responsavel', String, ForeignKey('responsavel.cpf_responsavel'), primary_key=True)
)

class Paciente(Base):
    __tablename__ = 'paciente'
    cpf_paciente = Column(String, primary_key=True)
    nome_completo = Column(String, nullable=False)
    email = Column(String)
    telefone = Column(String)
    logradouro = Column(String)
    numero = Column(String)
    bairro = Column(String)
    cidade = Column(String)
    cep = Column(String)
    data_nascimento = Column(Date)

class Responsavel(Base):
    __tablename__ = 'responsavel'
    cpf_responsavel = Column(String, primary_key=True)
    nome_completo = Column(String, nullable=False)
    email = Column(String)
    telefone = Column(String)
    logradouro = Column(String)
    numero = Column(String)
    bairro = Column(String)
    cidade = Column(String)
    cep = Column(String)

class Cuidador(Base):
    __tablename__ = 'cuidador'
    cpf_cuidador = Column(String, primary_key=True)
    nome_completo = Column(String, nullable=False)
    email = Column(String)
    telefone = Column(String)
    logradouro = Column(String)
    numero = Column(String)
    bairro = Column(String)
    cidade = Column(String)
    cep = Column(String)
    dias_disponiveis = Column(String)
    horario_disponivel = Column(String)

class Pagamento(Base):
    __tablename__ = 'pagamento'
    id_pagamento = Column(Integer, primary_key=True, autoincrement=True)
    data_pagamento = Column(Date)
    cpf_responsavel = Column(String, ForeignKey('responsavel.cpf_responsavel'))
    cpf_cuidador = Column(String, ForeignKey('cuidador.cpf_cuidador'))
    valor = Column(Numeric)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Avaliacao(Base):
    __tablename__ = 'avaliacao'
    id_avaliacao = Column(Integer, primary_key=True, autoincrement=True)
    cpf_responsavel = Column(String, ForeignKey('responsavel.cpf_responsavel'))
    cpf_cuidador = Column(String, ForeignKey('cuidador.cpf_cuidador'))
    nota = Column(Integer)
    comentario = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Medicamento(Base):
    __tablename__ = 'medicamento'
    id_medicamento = Column(Integer, primary_key=True, autoincrement=True)
    nome_generico = Column(String(100))
    nome_comercial = Column(String(100))

class PacienteMedicamento(Base):
    __tablename__ = 'paciente_medicamento'
    cpf_paciente = Column(String, ForeignKey('paciente.cpf_paciente'), primary_key=True)
    id_medicamento = Column(Integer, ForeignKey('medicamento.id_medicamento'), primary_key=True)
    data_inicio = Column(Date, primary_key=True)
    data_fim = Column(Date)
    frequencia = Column(String(50))
    dosagem = Column(String(50))