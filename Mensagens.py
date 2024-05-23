import os

mensagens = []
nome = input("Nome: ")

while True: 

    #o código abaixo vai limpar o terminal sempre para não travar!
    os.system('cls')
    #cls = clear

    if len(mensagens) > 0:
        for m in mensagens:
            print (m['nome'], "-", m['texto'])
    
    print ("___________________")

    #OBTENDO TEXTO
    texto = input("mensagem: ")
    if texto == "fim":
        break

    # adionanco mensagem na lista
    mensagens.append({
        "nome": nome, 
        "texto": texto
    })