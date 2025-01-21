from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from sqlalchemy.orm.exc import NoResultFound


class PessoaFisicaRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def criar_pessoa_fisica(
        self,
        renda_mensal: float,
        idade: int,
        nome_completo: str,
        celular: str,
        email: str,
        categoria: str,
        saldo: float,
    ) -> None:
        with self.__db_connection as database:
            try:
                person_fisica_data = PessoaFisica(
                    renda_mensal=renda_mensal,
                    idade=idade,
                    nome_completo=nome_completo,
                    celular=celular,
                    email=email,
                    categoria=categoria,
                    saldo=saldo,
                )
                database.session.add(person_fisica_data)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception

    def consultar_saldo(self, nome_completo):
        with self.__db_connection as database:
            try:
                consulta = (
                    database.session.query(PessoaFisica)
                    .filter_by(nome_completo=nome_completo)
                    .first()
                )
                return consulta.saldo
            except Exception as exception:
                database.session.rollback()
                raise exception

    def sacar_dinheiro(self, pessoa_fisica, valor):
        limite_saque = 5000
        saldo = self.consultar_saldo(pessoa_fisica)
        if valor <= limite_saque and valor <= saldo:
            saldo -= valor
            return (
                f"Saque de R$ {valor} realizado com sucesso. Saldo restante R$ {saldo}"
            )
        else:
            return "Erro: Valor de saque excede o limite ou saldo insuficiente."

    def realizar_extrato(self, pessoa_fisica):
        with self.__db_connection as database:
            try:
                pessoa_fisica = (
                    database.session.query(PessoaFisica)
                    .filter_by(nome=pessoa_fisica.nome_completo)
                    .first()
                )
                return {
                    "Nome": pessoa_fisica.nome_completo,
                    "Saldo": pessoa_fisica.saldo,
                    "Categoria": pessoa_fisica.categoria,
                }

            except NoResultFound:
                return []
