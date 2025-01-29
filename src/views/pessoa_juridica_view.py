class PessoaJuridicaView:
    def __init__(self, pessoa_juridica_controller):
        self.pessoa_juridica_controller = pessoa_juridica_controller

    def criar_pessoa_juridica(self, request):
        try:
            faturamento = request.get("faturamento")
            idade = request.get("idade")
            nome_fantasia = request.get("nome_fantasia")
            celular = request.get("celular")
            email_corporativo = request.get("email_corporativo")
            categoria = request.get("categoria")
            saldo = request.get("saldo")

            self.pessoa_juridica_controller.criar_pessoa_juridica(
                faturamento = faturamento,
                idade = idade,
                nome_fantasia = nome_fantasia,
                celular = celular,
                email_corporativo = email_corporativo,
                categoria = categoria,
                saldo = saldo,
            )
            return "Pessoa jurídica cadastrada com sucesso!"

        except Exception as exception:
            raise str(exception)
        
    def consultar_saldo(self, request):

        try:
            nome_pessoa_juridica = request.get("pessoa_juridica")

            saldo = self.pessoa_juridica_controller.consultar_saldo(
                nome_pessoa_juridica
            )

            return f"O saldo da pessoa jurídica {nome_pessoa_juridica} é R$ {saldo}"
        except Exception as exception:
            raise str(exception)
        
    def sacar_dinheiro(self, request):
        try:
            nome_pessoa_juridica = request.get("nome_pessoa_juridica")

            valor = request.get("valor")

            mensagem = self.pessoa_juridica_controller.sacar_dinheiro(
                nome_pessoa_juridica, valor)
            
            return mensagem
        except Exception as exception:
            raise str(exception)
        
    def realizar_extrato(self, request):
        try:
            nome_pessoa_juridica = request.get("nome_pessoa_juridica")

            extrato = self.pessoa_juridica_controller.realizar_extrato(
                nome_pessoa_juridica
            )

            return extrato
        except Exception as exception:
            raise str(exception)