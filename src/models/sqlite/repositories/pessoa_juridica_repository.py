from typing import List
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from sqlalchemy.orm.exc import NoResultFound


class PessoaJuridicaRepository:

    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def listar_usuarios_pj(self) -> List[PessoaJuridica]:
        with self.__db_connection as database:
            try:
                pessoa_juridica = database.session.query(PessoaJuridica).all()
                return pessoa_juridica

            except NoResultFound:
                return []
