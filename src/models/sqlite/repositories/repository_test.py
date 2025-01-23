import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pessoa_fisica_repository import PessoaFisicaRepository
from .pessoa_juridica_repository import PessoaJuridicaRepository

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="interacao com o banco de dados")
def test_criar_pessoa_fisica():
    renda_mensal = 1000
    idade = 30
    nome_completo = "Mario"
    celular = "123456789"
    email = "n8p6M@example.com"
    categoria = "pessoa_fisica"
    saldo = 1000

    repo = PessoaFisicaRepository(db_connection_handler)
    repo.criar_pessoa_fisica(
        renda_mensal, idade, nome_completo, celular, email, categoria, saldo
    )


@pytest.mark.skip(reason="interacao com o banco de dados")
def test_list_pessoa_fisica():
    repo = PessoaFisicaRepository(db_connection_handler)
    response = repo.listar_usuarios_pf()
    print()
    print(response)


@pytest.mark.skip(reason="interacao com o banco de dados")
def test_criar_pessoa_juridica():
    faturamento = 5000
    idade = 45
    nome_fantasia = "Empresa Windows S.A"
    celular = "123456789"
    email_corporativo = "n8p6M@example.com"
    categoria = "pessoa_juridica"
    saldo = 300000

    repo = PessoaJuridicaRepository(db_connection_handler)
    repo.criar_pessoa_juridica(
        faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo
    )


@pytest.mark.skip(reason="interacao com o banco de dados")
def test_list_pessoa_juridica():
    repo = PessoaJuridicaRepository(db_connection_handler)
    response = repo.listar_usuarios_pj()
    print()
    print(response)


@pytest.mark.skip(reason="interacao com o banco de dados")
def test_consultar_saldo():
    nome_completo = "Pedro Santos"
    repo = PessoaFisicaRepository(db_connection_handler)
    repo.consultar_saldo_PF(nome_completo)
