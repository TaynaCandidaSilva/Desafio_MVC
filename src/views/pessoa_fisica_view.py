class PessoaFisicaView:
    def __init__(self, pessoa_fisica_controller):
        self.pessoa_fisica_controller = pessoa_fisica_controller

    def cadastrar_pessoa_fisica(self, request):
        try:
            nome_completo = request.get("nome_completo")
            renda_mensal = request.get("renda_mensal")
            idade = request.get("idade")
            celular = request.get("celular")
            email = request.get("email")
            categoria = request.get("categoria")
            saldo = request.get("saldo")

            self.pessoa_fisica_controller.criar_pessoa_fisica(
                nome_completo = nome_completo,
                renda_mensal = renda_mensal,
                idade = idade,
                celular = celular,
                email = email,
                categoria = categoria,
                saldo = saldo,
            )
            return "Pessoa física cadastrada com sucesso!"

        except Exception as exception:
            raise str(exception)

    def consultar_saldo(self, request):

        try: 
            nome_pessoa_fisica = request.get("nome_pessoa_fisica")

            saldo = self.pessoa_fisica_controller.consultar_saldo(
                nome_pessoa_fisica
            )

            return f"O saldo da pessoa física {nome_pessoa_fisica} é R$ {saldo}"
        
        except Exception as exception:
            raise str(exception)
        
    def realizar_extrato(self, request):
        try:
            nome_pessoa_fisica = request.get("nome_pessoa_fisica")

            extrato = self.pessoa_fisica_controller.realizar_extrato(
                nome_pessoa_fisica
            )

            return extrato
        
        except Exception as exception:
            raise str(exception)
        
    def sacar_dinheiro(self, request):
        try:
            nome_pessoa_fisica = request.get("nome_pessoa_fisica")

            valor = request.get("valor")

            mensagem = self.pessoa_fisica_controller.sacar_dinheiro(
                nome_pessoa_fisica, valor)
            
            return mensagem

        except Exception as exception:
            raise str(exception)