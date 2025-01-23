class PessoaJuridicaController:
    def __init__(self, pessoa_juridica_repository):
        self.pessoa_juridica_repository = pessoa_juridica_repository

    def criar_pessoa_juridica(
        self,
        faturamento,
        idade,
        nome_fantasia,
        celular,
        email_corporativo,
        categoria,
        saldo,
    ):
        try:
            self.faturamento = (faturamento,)
            self.idade = (idade,)
            self.nome_fantasia = (nome_fantasia,)
            self.celular = (celular,)
            self.email_corporativo = (email_corporativo,)
            self.categoria = (categoria,)
            self.saldo = saldo
        except Exception as exception:
            raise exception

    def consultar_saldo(self, nome_pessoa_juridica):
        try:
            saldo = self.pessoa_juridica_repository.consultar_saldo(
                nome_pessoa_juridica
            )
            return saldo
        except Exception:
            raise Exception

    def sacar_dinheiro(self, pessoa_juridica, valor):
        try:
            mensagem = self.pessoa_juridica_repository.sacar_dinheiro(
                pessoa_juridica, valor
            )
            return mensagem
        except Exception as exception:
            raise exception

    def realizar_extrato(self, pessoa_juridica):
        try:
            extrato = self.pessoa_juridica_repository.realizar_extrato(pessoa_juridica)
            return extrato
        except Exception as exception:
            raise exception
