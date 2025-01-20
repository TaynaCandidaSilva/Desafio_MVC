from typing import List
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

    def listar_usuarios_pf(
        self,
    ) -> List[PessoaFisica]:
        with self.__db_connection as database:
            try:
                pessoa_fisica = database.session.query(PessoaFisica).all()
                return pessoa_fisica

            except NoResultFound:
                return []

    def criar_usuario(self):
        pass
