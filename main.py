class Node:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.atual = None

    def inserir_no_fim(self, valor):
        novo_no = Node(valor)
        if self.cauda is None:  # Lista vazia
            self.cabeca = self.cauda = self.atual = novo_no
        else:
            novo_no.anterior = self.cauda
            self.cauda.proximo = novo_no
            self.cauda = novo_no
        self.atual = self.cauda  # O ponteiro "atual" sempre começa no fim

    def remover_no_fim(self):
        if self.cauda is None:
            print("⚠ Lista vazia, nada para remover.")
            return

        if self.cauda == self.cabeca:  # Se há apenas um elemento
            self.cabeca = self.cauda = self.atual = None
        else:
            self.cauda = self.cauda.anterior
            self.cauda.proximo = None
            self.atual = self.cauda  # Mover "atual" para a nova cauda

    def desfazer(self):
        if self.atual and self.atual.anterior:
            self.atual = self.atual.anterior
        else:
            print("⚠ Não é possível desfazer (já no primeiro elemento).")

    def refazer(self):
        if self.atual and self.atual.proximo:
            self.atual = self.atual.proximo
        else:
            print("⚠ Não é possível refazer (já no último elemento).")

    def mostrar_lista(self):
        atual = self.cabeca
        print("\n📌 Lista:", end=" ")
        while atual:
            if atual == self.atual:
                print(f"[({atual.valor})]", end=" <-> ")
            else:
                print(f"{atual.valor}", end=" <-> ")
            atual = atual.proximo
        print("None")

        print(f"   🟢 Cabeça: {self.cabeca.valor if self.cabeca else 'None'}")
        print(f"   🔴 Cauda: {self.cauda.valor if self.cauda else 'None'}")
        print(f"   🔄 Atual: {self.atual.valor if self.atual else 'None'}\n")


# 📌 Criando a lista
lista = ListaDuplamenteEncadeada()

# 📌 Menu interativo
while True:
    print("\n🔹 MENU 🔹")
    print("1️⃣ Adicionar um número")
    print("2️⃣ Remover o último número")
    print("3️⃣ Desfazer (mover para trás)")
    print("4️⃣ Refazer (mover para frente)")
    print("5️⃣ Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = input("Digite um número para adicionar: ")
        lista.inserir_no_fim(int(valor))
        lista.mostrar_lista()

    elif opcao == "2":
        lista.remover_no_fim()
        lista.mostrar_lista()

    elif opcao == "3":
        lista.desfazer()
        lista.mostrar_lista()

    elif opcao == "4":
        lista.refazer()
        lista.mostrar_lista()

    elif opcao == "5":
        print("👋 Saindo...")
        break

    else:
        print("⚠ Opção inválida! Escolha entre 1 e 5.")
