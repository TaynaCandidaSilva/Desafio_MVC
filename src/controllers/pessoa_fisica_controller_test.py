from unittest.mock import Mock
from .pessoa_fisica_controller import PessoaFisicaController


class MockPessoaFisica:
    def criar_pessoa_fisica(
        self, renda_mensal, idade, nome_completo, celular, email, categoria, saldo
    ):
        pass


def test_criar_pessoa_fisica():
    pessoa_fisica = {
        "renda_mensal": 1000,
        "idade": 20,
        "nome_completo": "Juninho",
        "celular": "11999999999",
        "email": "juninho@juninho",
        "categoria": "A",
        "saldo": 100,
    }

    controller = PessoaFisicaController(MockPessoaFisica())
    response = controller.criar_pessoa_fisica(**pessoa_fisica)

    assert pessoa_fisica["nome_completo"] == "Juninho"
    assert pessoa_fisica["renda_mensal"] == 1000
    assert response is None


def test_saldo():

    nome_cliente = "Juninho"
    saldo_esperado = 100

    mock_repository = Mock()
    mock_repository.consultar_saldo.return_value = saldo_esperado
    controller = PessoaFisicaController(mock_repository)
    response = controller.consultar_saldo(nome_cliente)

    assert response == saldo_esperado
    mock_repository.consultar_saldo.assert_called_once_with(nome_cliente)


def test_sacar_dinheiro():
    pessoa_fisica = Mock()
    valor = 50
    mock_repository = Mock()
    mock_repository.sacar_dinheiro.return_value = "Saque realizado com sucesso"
    controller = PessoaFisicaController(mock_repository)

    response = controller.sacar_dinheiro(pessoa_fisica, valor)

    assert response == "Saque realizado com sucesso"
    mock_repository.sacar_dinheiro.assert_called_once_with(pessoa_fisica, valor)


def test_realizar_extrato():
    nome_cliente = "Juninho"
    saldo = 100
    categoria = "A"

    mock_repository = Mock()
    mock_repository.realizar_extrato.return_value = {
        "Nome": nome_cliente,
        "Saldo": saldo,
        "Categoria": categoria,
    }
    controller = PessoaFisicaController(mock_repository)
    response = controller.consultar_saldo(nome_cliente)

    assert response[nome_cliente] == "Juninho"
    assert response[saldo] == 100
    assert response[categoria] == "A"
