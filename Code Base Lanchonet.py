###LanchoNET###
from time import sleep

print("\n -- SISTEMA lanchoNET --")

# Bases da Manipulação de Dados
#[quantidade, nome do produto, valor individual, valor pela quantidade, código]
baseVenda = []
vendasTotais = []
novoProd = {}

##Código: [{Nome: Valor em Reais}]
codigos = [{'Bolo de Fubá com Goibada': 15},
           {'Bolo de Chocolate (Fatia)': 3},
           {'Bolo de Macaxeira (Fatia)': 2},
           {'Bolo de Milho (Fatia)': 5},
           {'Bolo de Trigo (Fatia)': 2},
           {'Bolo de Limão (Fatia)': 3},
           {'Bolo de Puba (Fatia2)': 2},
           {'Bolo de Tapioca': 2},
           {'Coxinha': 2.5},
           {'Pão Caseiro': 5},
           {'Pão de Queijo': 0.5},
           {'Mão de Vaca': 0}
           ]

# FUNÇÕES
## Cancelar Item de Venda
def cancelItem(itemCancel):
    

    for x in baseVenda: #procura pelo item

        if x[-1] == itemCancel:
            print("\n{0}x - {1}({2}) = R${3}".format(x[0], x[1], x[2],x[3]))
            apagar = input("\n (a)Retirar Item por Completo\n (b)Retirar Parte do Item\nEscolha: ").capitalize()

            if apagar == 'A':
                indicIt = baseVenda.index(x)
                baseVenda.pop(indicIt)
                sleep(0.2)
                print("Item Retirado\n")
                sleep(0.5)

            elif apagar == 'B':
                retQtt = int(input("Digite a quantidade a ser retirada: "))
                x[0] = x[0] - retQtt
                sleep(0.2)
                print("Quantidade Retirada\n")
                sleep(0.5)
                
            else:
                sleep(0.5)
                print("##Resposta Inválida##")
    

## Venda
def venda():
    print('\nTABELA DE PRODUTOS\n')
    # Escrever itens adicionados
    for x in codigos:

        for nome,valor in x.items():
            print("({2}) - {0} R${1}".format(nome,valor,(codigos.index(x)+1)))

    while True:

        while True: ##outra dica que estava na documentação

            # garantindo que o input será um número
            try:
                prod = int(input("\nDigite o código do produto ou 0 para encerrar: "))
                break

            except ValueError:
                sleep(0.5)
                print("\n##O código digitado deve ser um número##")
                continue
            
        #se o código existir na tabela 
        if 0 < prod <= len(codigos): 
            print(codigos[prod-1])

            # garantindo que o input será um número
            while True:
                try:
                    qtt = int(input("Digite a quantidade: "))
                    break
                except ValueError:
                    sleep(0.5)
                    print("##O código digitado deve ser um número##")
                    continue

            # se for o primeiro produto adicionado
            if len(baseVenda) == 0:

                for nome,valor in codigos[prod-1].items(): #vi esse estilo na documentação
                    baseVenda.append([qtt, nome, valor, qtt*valor, prod])

            # se já existirem produtos dentro da venda
            else:
                
                # procura pelo produto
                for item in baseVenda:
                    ach = ''
                    if item[-1] == prod:
                        ach = baseVenda.index(item)

                # se o produto NÃO for achado, add
                if ach == '':
                    for nome,valor in codigos[prod-1].items():
                        baseVenda.append([qtt, nome, valor, qtt*valor, prod])

                # se o produto FOR achado, aumenta a quantidade
                else:
                    baseVenda[ach][0] = baseVenda[ach][0] + qtt
  
        #Para finalizar comprar
        elif prod == 0:

            # caso nenhum item tenha sido selecionado
            if len(baseVenda) == 0: 
                print("##Nenhum Item Selecionado, Compra Cancelada##")
                break

            else:
                total = 0
                print("Compra Finalizada\n")
                sleep(0.5)

                #Lista Final de Produtos Comprados
                print("Itens escolhidos:")

                for x in baseVenda:
                    sleep(0.2)
                    # Imprimir cada produto
                    print("{0}x - {1}(R${2}) = R${3}".format(x[0], x[1], x[2],x[3]))
                    total = total + x[3]
                print("Total da Compra: R$",total)

                fecha = input("\nFechar compra? (s/n): ").capitalize() #caso precise adicionar mais itens
            
            if fecha == 'S':
                vendaInd = baseVenda[:] #clona base de vendas de forma independente para que não suma quando a base for limpa
                vendasTotais.append(vendaInd) #inclui venda atual no registro geral de vendas
                baseVenda.clear() #limpa a base de vendas
                break 

            elif fecha == 'N':

                #Cancelamento de Item
                while True:
                    cancelamento = input("Deseja retirar algo (s/n)?: ").capitalize() 

                    # para cancelar
                    if cancelamento == 'S':

                        # garantindo que o input será um número
                        while True:
                            try:
                                itemCancel = int(input("\nDigite o código do item a ser alterado: "))
                                break
                            except ValueError:
                                sleep(0.5)
                                print("##O código deve ser um número##")
                                continue

                        cancelItem(itemCancel)

                    # para NÃO cancelar
                    elif cancelamento == 'N':
                        print("Se desejar, adicione um item à venda.")
                        break 

                    else:
                        sleep(0.5)
                        print("\n##Resposta Inválida##")

            else:
                sleep(0.5)
                print("\n##Resposta Inválida, a compra será aberta novamente##")
                continue
                
        else:
            sleep(0.5)
            print('\n##Código Inválido##')
## Add produto na tabela
def addProdTabel(nomeProdN, valorProdN):
    novoProd[nomeProdN] = valorProdN 
    prodNovo = novoProd.copy()
    codigos.append(prodNovo)
    novoProd.clear()

## Del produto da tabela
def delProdTabel(itemRet):

    for x in codigos:
                    indcItRet = codigos.index(x)

                    if indcItRet == itemRet-1:
                        print(x)
                        retirar = input("Deseja retirar este item (s/n)?").capitalize()

                        if retirar == 'S':
                            codigos.pop(itemRet - 1)

                        elif retirar == 'N':
                            break

                        else:
                            sleep(0.5)
                            print("##Código Inválido, Item não retirado##")
## TABELA DE PRODUTOS
def produtos():
    print('\nTABELA DE PRODUTOS\n')
    # Escrever itens adicionados

    for x in codigos:

        for nome,valor in x.items():
            print("({2}) - {0} R${1}".format(nome,valor,(codigos.index(x)+1)))
    sleep(0.5)
    addOuRetProd = input("Adicionar ou Retirar Item da tabela (s/n)? ").capitalize()
    if addOuRetProd == 'S':

        while True:
            # Adicionar Produto            
            AoR = input("\n(a) - Adicionar Produto \n(b) - Retirar Produto \n(c) - Finalizar Ação \nAção: ").capitalize()

            if AoR == 'A':
                nomeProdN = input("\nDigite o nome do Produto a ser adicionado: ").capitalize()
                valorProdN = float(input("Digite o valor do Produto a ser adicionado: "))
                # add o produto e seu valor à tabela
                addProdTabel(nomeProdN, valorProdN)

            # Retirar Produto
            elif AoR == 'B':
                itemRet = int(input("Digite o Código do Produto a ser retirado: "))
                delProdTabel(itemRet)
                  
            # Finalizar
            elif AoR == 'C':
                break

            else:
                sleep(0.5)
                print("##Ação Inválida##")
                continue

    elif addOuRetProd == 'N':
        "tudo bem"

    else:
        print("##Resposta Inválida##")

## REGISTRO DE VENDAS
def registro():
    x = 0
    total = 0
    totalGeral = 0
    print("\nREGISTRO GERAL DE VENDAS")

    if len(vendasTotais) == 0:
        print("\n##Nenhuma Venda Realizada##")

    else:

        for cadaVenda in vendasTotais:
            print("\nVenda", x + 1)

            for cadaProd in cadaVenda:
                print("{0}x - {1}(R${2}) = R${3}".format(cadaProd[0], cadaProd[1], cadaProd[2],cadaProd[3]))
                total = total + cadaProd[3]
            print("Total da Venda: R$", total)
            x += 1
            totalGeral = totalGeral + total
            total = 0

    print("\nTotal Geral de Vendas: R$", totalGeral)
    
# INÍCIO
while True:
    print("\nDigite o código da ação:")
    acao = input(" 1 - Venda \n 2 - Tabela de Produtos \n 3 - Registro de Vendas \n 4 - Encerrar Sessão \n \nCódigo: ")
    sleep(0.5)

    if acao == '1':
        venda()

    elif acao == '2':
        produtos()

    elif acao == '3':
        registro()

    elif acao == '4':
        break

    else:
        sleep(0.5)
        print("### Código inválido ###")
print("Fim de Sessão.\nAgradecemos por utilizar o sistema LanchoNet!")

#### Área de Visualização (para manutenção e demonstração) ###
#print('base venda:',baseVenda)
#print('vendas totais:',vendasTotais)
#print('codigos:', codigos)        
