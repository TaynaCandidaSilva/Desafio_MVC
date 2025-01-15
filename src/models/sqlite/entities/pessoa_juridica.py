from sqlalchemy import Column, String, BIGINT, Float
from src.models.sqlite.settings.base import Base

class PessoaJuridica(Base):
    __tablename__ = "pessoa_juridica"

    id = (Column(BIGINT, primary_key=True),)
    faturamento = (Column(Float),)
    idade = (Column(BIGINT),)
    nome_fantasia = (Column(String),)
    celular = (Column(String),)
    email_corporativo = (Column(String),)
    categoria = (Column(String),)
    saldo = Column(Float)

    def __repr__(self):
        return (
            f"Pessoa Juridica [renda_mensal={self.faturamento}, 
                idade={self.idade},
                nome_fantasia={self.nome_fantasia},
                celular={self.celular},
                email_corporativo={self.email_corporativo},
                categoria={self.categoria},
                saldo={self.saldo}]"
        )
