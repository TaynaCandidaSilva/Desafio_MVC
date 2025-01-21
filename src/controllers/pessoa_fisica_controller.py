class PessoaFisicaController:
    def __init__(self, pessoa_fisica_repository) -> None:
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
        pass
