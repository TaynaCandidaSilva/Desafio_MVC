from typing import List
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from sqlalchemy.orm.exc import NoResultFound


class PessoaJuridicaRepository:

    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def criar_pessoa_juridica(
        self,
        faturamento: float,
        idade: int,
        nome_fantasia: str,
        celular: str,
        email_corporativo: str,
        categoria: str,
        saldo: float,
    ) -> None:
        with self.__db_connection as database:
            try:
                person_juridica_data = PessoaJuridica(
                    faturamento=faturamento,
                    idade=idade,
                    nome_fantasia=nome_fantasia,
                    celular=celular,
                    email_corporativo=email_corporativo,
                    categoria=categoria,
                    saldo=saldo,
                )
                database.session.add(person_juridica_data)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception

    def consultar_saldo_PJ(self, nome_fantasia) -> None:
        with self.__db_connection as database:
            try:
                pessoa_juridica = (
                    database.session.query(PessoaJuridica)
                    .filter_by(nome_fantasia=nome_fantasia)
                    .first()
                )
                return pessoa_juridica.saldo
            except Exception:
                database.session.rollback()
                raise Exception

    def sacar_dinheiro_PJ(self, pessoa_juridica, valor):
        saldo = self.consultar_saldo_PJ(pessoa_juridica)
        if valor <= saldo:
            saldo -= valor
            return f"Saque de {valor} realizado com sucesso. Saldo restante R$ {saldo}"
        else:
            return f"Erro: saldo insuficiente"

    def realizar_extrato_PJ(self, pessoa_juridica):
        with self.__db_connection as database:
            try:
                pessoa_juridica = (
                    database.session.query(PessoaJuridica)
                    .filter_by(nome_fantasia=pessoa_juridica)
                    .first()
                )
                return {
                    "Nome": pessoa_juridica.nome_fantasia,
                    "Saldo": pessoa_juridica.saldo,
                    "Categoria": pessoa_juridica.categoria,
                }
            except NoResultFound:
                return []
