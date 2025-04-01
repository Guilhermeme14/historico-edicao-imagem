class No:
    def __init__(self, descricao, imagem_id):
        self.descricao = descricao
        self.imagem_id = imagem_id
        self.anterior = None
        self.proximo = None


class HistoricoEdicao:
    def __init__(self):
        self.inicio = None
        self.atual = None
        self.cauda = None

    def adicionar_acao(self, descricao, imagem_id):
        novo_no = No(descricao, imagem_id)
        if self.atual is None:
            self.inicio = novo_no
            self.cauda = novo_no
        else:
            novo_no.anterior = self.atual
            self.atual.proximo = novo_no
            self.cauda = novo_no
        self.atual = novo_no

    def desfazer(self):
        if self.atual and self.atual.anterior:
            self.atual = self.atual.anterior
            print(f"Desfeito: {self.atual.descricao}, Imagem ID: {self.atual.imagem_id}")
        else:
            print("Não há ações para desfazer.")

    def refazer(self):
        if self.atual and self.atual.proximo:
            self.atual = self.atual.proximo
            print(f"Refeito: {self.atual.descricao}, Imagem ID: {self.atual.imagem_id}")
        else:
            print("Não há ações para refazer.")

    def listar_acoes(self):
        atual = self.inicio
        print("\nHistórico de Edição:\n")
        while atual:
            marcador = "->" if atual == self.atual else "  "
            print(f"{marcador} {atual.descricao} (Imagem ID: {atual.imagem_id})")
            atual = atual.proximo
        print(f"\nCabeça: {self.inicio.descricao if self.inicio else 'None'}")
        print(f"Atual: {self.atual.descricao if self.atual else 'None'}")
        print(f"Cauda: {self.cauda.descricao if self.cauda else 'None'}")


# Criando o histórico com uma lista predefinida de ações
historico = HistoricoEdicao()
acoes_predefinidas = [
    ("Ajuste de brilho", 1),
    ("Filtro preto e branco", 2),
    ("Ajuste de contraste", 3),
    ("Saturação aumentada", 4),
    ("Redução de ruído", 5)
]

for descricao, imagem_id in acoes_predefinidas:
    historico.adicionar_acao(descricao, imagem_id)

# Menu interativo
while True:
    print("\nMENU")
    print("1 - Desfazer última ação")
    print("2 - Refazer ação desfeita")
    print("3 - Listar ações")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        historico.desfazer()
    elif opcao == "2":
        historico.refazer()
    elif opcao == "3":
        historico.listar_acoes()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Escolha entre 1 e 4.")
