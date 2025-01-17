from typing import List
from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from sqlalchemy.orm.exc import NoResultFound


class PessoaFisicaRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def listar_usuarios(
        self,
    ) -> List:
        with self.__db_connection as database:
            try:
                pessoa_fisica = database.session.query(PessoaFisica).all()
                return pessoa_fisica

            except NoResultFound:
                return []

    def criar_usuario(self):
        pass

    def deletar_usuario(self, id: int):
        with self.__db_connection as database:
            try:
                (
                    database.session.query(PessoaFisica)
                    .filter(PessoaFisica.id == id)
                    .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
