import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Pega o caminho absoluto da pasta do projeto (uma pasta atrás da pasta 'config')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, '.env')

# 2. Carrega o .env forçando o caminho exato
load_dotenv(ENV_PATH)

# 3. Carrega as variáveis de ambiente
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
NAME = os.getenv("DB_NAME")

# Trava de segurança para avisar se o arquivo .env estiver vazio ou incorreto
if not HOST:
    print(f"\n[ERRO CRÍTICO] Variável DB_HOST não encontrada! Verifique se o arquivo existe em {ENV_PATH} e se as variáveis começam com DB_")

# URL de conexão com sslmode=require (Essencial para o Supabase)
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}?sslmode=require"

# A Engine gerencia o pool de conexões
engine = create_engine(DATABASE_URL, echo=False)

# SessionLocal é a fábrica de sessões (transações) para os notebooks
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para herdar nos modelos (equivalente a uma classe base de entidades)
Base = declarative_base()

# Teste rápido de conexão
try:
    with engine.connect() as connection:
        print("Conexão com o Supabase estabelecida com sucesso! (Versão Atualizada)")
except Exception as e:
    print(f"Falha ao conectar: {e}")