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

    def listar_usuarios_pj(self) -> List[PessoaJuridica]:
        with self.__db_connection as database:
            try:
                pessoa_juridica = database.session.query(PessoaJuridica).all()
                return pessoa_juridica

            except NoResultFound:
                return []
