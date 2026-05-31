import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Carrega as variáveis do .env
load_dotenv()

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
NAME = os.getenv("DB_NAME")

# URL de conexão no padrão PostgreSQL
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"

# A Engine gerencia o pool de conexões
engine = create_engine(DATABASE_URL, echo=False) # echo=True para ver o log do SQL

# SessionLocal é a fábrica de sessões (transações)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para herdar nos modelos (equivalente a uma classe base de entidades)
Base = declarative_base()

def get_db_session():
    """Gera uma nova sessão com o banco de dados."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()