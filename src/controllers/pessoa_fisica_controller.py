class PessoaFisicaController:
    def __init__(self, pessoa_fisica_repository):
        self.pessoa_fisica_repository = pessoa_fisica_repository

    def criar_pessoa_fisica(
        self, renda_mensal, idade, nome_completo, celular, email, categoria, saldo
    ):
        try:
            self.pessoa_fisica_repository.criar_pessoa_fisica(
                renda_mensal=renda_mensal,
                idade=idade,
                nome_completo=nome_completo,
                celular=celular,
                email=email,
                categoria=categoria,
                saldo=saldo,
            )
        except Exception as exception:
            raise exception

    def consultar_saldo(self, nome_pessoa_fisica):
        try:
            saldo = self.pessoa_fisica_repository.consultar_saldo(nome_pessoa_fisica)
            return saldo
        except Exception:
            raise Exception

    def sacar_dinheiro(self, pessoa_fisica, valor):
        try:
            mensagem = self.pessoa_fisica_repository.sacar_dinheiro(
                pessoa_fisica, valor
            )
            return mensagem
        except Exception as exception:
            raise exception

    def realizar_extrato(self, pessoa_fisica):
        try:
            extrato = self.pessoa_fisica_repository.realizar_extrato(pessoa_fisica)
            return extrato
        except Exception as exception:
            raise exception
