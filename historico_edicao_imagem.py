def criar_no(descricao, imagem_id):
    return {"descricao": descricao, "imagem_id": imagem_id, "anterior": None, "proximo": None}

historico = {"inicio": None, "atual": None}

def adicionar_acao(historico, descricao, imagem_id):
    novo_no = criar_no(descricao, imagem_id)
    if historico["atual"] is None:
        historico["inicio"] = novo_no
    else:
        novo_no["anterior"] = historico["atual"]
        historico["atual"]["proximo"] = novo_no
    historico["atual"] = novo_no
    print(f"Ação adicionada: {descricao}, Imagem ID: {imagem_id}")

def desfazer(historico):
    if historico["atual"] and historico["atual"]["anterior"]:
        historico["atual"] = historico["atual"]["anterior"]
        print(f"Utilizando desfazer: \n "
              f"Nó anterior -> {historico['atual']['anterior']}"
              f"Nó atual -> {historico['atual']['descricao']}, Imagem ID: {historico['atual']['imagem_id']} \n"
              f"Próximo nó -> {historico['atual']['proximo']}")
    else:
        print("Não há ações para desfazer.")

def refazer(historico):
    if historico["atual"] and historico["atual"]["proximo"]:
        historico["atual"] = historico["atual"]["proximo"]
        print(f"Refeito: {historico['atual']['descricao']}, Imagem ID: {historico['atual']['imagem_id']}")
    else:
        print("Não há ações para refazer.")

def listar_acoes(historico):
    atual = historico["inicio"]
    while atual:
        print(f"Ação: {atual['descricao']}, Imagem ID: {atual['imagem_id']}")
        atual = atual["proximo"]

# Exemplo de uso
adicionar_acao(historico, "Ajuste de brilho", 1)
adicionar_acao(historico, "Filtro preto e branco", 2)
adicionar_acao(historico, "Ajuste de contraste", 3)

listar_acoes(historico)

desfazer(historico)
desfazer(historico)
refazer(historico)
refazer(historico)
refazer(historico)