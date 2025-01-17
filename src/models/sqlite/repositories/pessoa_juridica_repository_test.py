import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from unittest import mock
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from .pessoa_juridica_repository import PessoaJuridicaRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PessoaJuridica)],  # query
                    [
                        PessoaJuridica(nome_fantasia="Empresa XYZ", idade=20),
                        PessoaJuridica(nome_fantasia="Caixa", idade=33),
                    ],  # resultado
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


@pytest.mark.skip(reason="interacao com o banco de dados")
def test_list_pessoa_juridica():
    mock_connection = MockConnection()
    repo = PessoaJuridicaRepository(mock_connection)
    response = repo.listar_usuarios_pj()

    mock_connection.session.query.assert_called_once_with(PessoaJuridica)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].nome_fantasia == "Empresa XYZ"
    assert response[1].nome_fantasia == "Caixa"


class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


@pytest.mark.skip(reason="interacao com o banco de dados")
def test_list_pessoa_juridica_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PessoaJuridicaRepository(mock_connection)
    response = repo.listar_usuarios_pj()

    mock_connection.session.query.assert_called_once_with(PessoaJuridica)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []
