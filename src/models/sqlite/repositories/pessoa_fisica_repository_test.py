from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from unittest import mock
from src.models.sqlite.entities.pessoa_fisica import PessoaFisica
from .pessoa_fisica_repository import PessoaFisicaRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PessoaFisica)],  # query
                    [
                        PessoaFisica(nome_completo="Mario", idade=20),
                        PessoaFisica(nome_completo="Luigi", idade=33),
                    ],  # resultado
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_list_pessoa_fisica():
    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)
    response = repo.listar_usuarios()

    assert response[0].nome_completo == "Mario"
    assert response
