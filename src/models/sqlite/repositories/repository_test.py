import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pessoa_fisica_repository import PessoaFisicaRepository


db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="interacao com o banco de dados")
def test_list_pessoa_fisica():
    repo = PessoaFisicaRepository(db_connection_handler)
    response = repo.listar_usuarios_pf()
    print()
    print(response)
