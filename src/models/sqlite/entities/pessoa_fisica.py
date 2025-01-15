from sqlalchemy import Column, String, BIGINT, Float
from src.models.sqlite.settings.base import Base

class PessoaFisica(Base):
    __tablename__ = "pessoa_fisica"

    id = (Column(BIGINT, primary_key=True),)
    renda_mensal = (Column(Float),)
    idade = (Column(BIGINT),)
    nome_completo = (Column(String),)
    celular = (Column(String),)
    email = (Column(String),)
    categoria = (Column(String),)
    saldo = Column(Float)

    def __repr__(self):
        return (
            f"Pessoa fisica [renda_mensal={self.renda_mensal}, 
                idade={self.idade},
                nome_completo={self.nome_completo},
                celular={self.celular},
                email={self.email},
                categoria={self.categoria},
                saldo={self.saldo}]"
        )
