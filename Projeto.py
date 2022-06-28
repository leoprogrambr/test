from time import sleep


# PRIMEIRA PERGUNTA PARA O CLIENTE: QUAL O PERIODO QUE DESEJA VER O CARDAPIO?
while True:
    print()
    try:
        card = str(input('Qual o periodo que deseja ver o cardapio ? \n'
                         '[Manhã/Noite]: ')).strip().upper()[0]

        # FORMATAÇÃO DO CARDAPIO DO PERIODO DA MANHA (CASO QUEIRA ADCIONAR OU REMOVER É SÓ ECLUIR OU TROCA-LO.
        manha = dict()
        cardapio_manha = list()
        manha['Entrada'] = 'Ovos'
        cardapio_manha.append(manha.copy())
        manha.clear()
        manha['Prato Principal'] = 'Torradas'
        cardapio_manha.append(manha.copy())
        manha.clear()
        manha['Bebida'] = 'Café'
        cardapio_manha.append(manha.copy())
        manha.clear()
        manha['Sobremesa'] = 'Não se aplica'
        cardapio_manha.append(manha.copy())
        manha.clear()

        # FORMATAÇÃO DO CARDAPIO DO PERIODO DA NOITE (CASO QUEIRA ADCIONAR OU REMOVER É SÓ ECLUIR OU TROCA-LO.
        noite = dict()
        cardapio = list()
        noite['Entrada'] = 'Bife'
        cardapio.append(noite.copy())
        noite.clear()
        noite['Prato Principal'] = 'Batatas'
        cardapio.append(noite.copy())
        noite.clear()
        noite['Bebida'] = 'Vinho'
        cardapio.append(noite.copy())
        noite.clear()
        noite['Sobremesa'] = 'Bolo'
        cardapio.append(noite.copy())
        noite.clear()

        # FORMATAÇÃO PARA UMA MELHOR EXPERIENCIA DO CLIENTE (MANHA)
        if card == 'M':
            print('=' * 40)
            print(f'{"Tipo de Prato":<5}\t\t\t{"Opções de manhã":>15}')
            print('=' * 40)
            for i, f in enumerate(cardapio_manha):
                print(f'{i:<3}', end='')
                for e in f.keys():
                    print(f'{str(e):<15}', end='')
                for d in f.values():
                    print(f'\t\t{str(d):<15}', end='')
                print()
            print('\nObservações: Você pode repetir quantas vezes quiser as xícaras de café.')
            print('=' * 40)
            break

        # FORMATAÇÃO PARA UMA MELHOR EXPERIENCIA DO CLIENTE (NOITE)
        if card == 'N':

            print('=' * 40)
            print(f'{"Tipo de Prato":<15}\t\t\t{"Opções de noite":>15}')
            print('=' * 40)
            for i, f in enumerate(cardapio):
                print(f'{i:<3}', end='')
                for e in f.keys():
                    print(f'{str(e):<15}', end='')
                for d in f.values():
                    print(f'\t\t{str(d):<15}', end='')
                print()
            print('\nObservações: Você pode repetir quantas vezes quiser as Batatas')
            print('=' * 40)
            break

        # TRATAMENTO DE ERRO
        if card.isnumeric() or card not in 'MN':
            print('\033[1;91mPor favor, digite uma opção valida\033[0;0m')
            print('='*40)

    #TRATAMENTO DE ERRO
    except:
        print('\033[1;91mPor favor, digite uma opção valida\033[0;0m')

# FORMATAÇÃO PARA PEDIDO DO CLIENTE
while True:
    try:
        pedido = str(input('Deseja efetuar um pedido ?\n'
                           '[ Sim / Não ]:  ')).strip().upper()[0]
        print('=' * 40)
        if pedido not in 'SN':
            print('\033[1;91mPor favor, escreva uma opção valida.\033[0;0m')
            print()
        if pedido == 'N':
            sleep(1)
            print('Finalizando ...')
            sleep(1)
            print('Muito obrigado pela sua presença e volte sempre ...')
            break
        if pedido == 'S':
            periodo = str(input('Qual o periodo que deseja fazer o pedido ? \n'
                                '[Manhã/Noite]: ')).strip().upper()[0]
            if periodo not in 'MN':
                print('\033[1;91mPor favor, escreva uma opção valida.\033[0;0m')
            print('='*40)
            print()

            # FORMATAÇÃO PARA PROJETO DE CLIENTES MANHA ( CONFORME ESTAVA ESCRITO NAO PODERA REPETIR A NAO SER A XICARA DE CAFE).
            if periodo == "M":
                print(f'{"OPÇÕES NO CARDAPIO":^40}')
                print()
                for i, f in enumerate(cardapio_manha):
                    print(f'{i:<3}', end='')
                    for e in f.keys():
                        print(f'{str(e):<15}', end='')
                    for d in f.values():
                        print(f'\t\t{str(d):<15}', end='')
                    print()
                print('\nObservações: Você pode repetir quantas vezes quiser as xícaras de café.')
                print()
                print('='*40)
                e = r = t = y = v = 0
                m = cardapio_manha[0]['Entrada']
                n = cardapio_manha[1]['Prato Principal']
                b = cardapio_manha[2]['Bebida']
                c = cardapio_manha[3]['Sobremesa']

                while True:
                    try:
                        a = int(input('Escolha pelo codigo qual é o seu pedido \n'
                                      'Digite 999 para poder fechar o pedido: '))
                        print()
                        if a == 0:
                            e += 1
                            if e == 1:
                                print(f'Você adicionol {cardapio_manha[0]["Entrada"]} ao seu pedido')
                                print('=' * 40)
                                v += 1
                                print()
                            if e >= 2:
                                print(
                                    f'\033[1;91mVoce não pode adicionar mais de um item de {cardapio_manha[0]["Entrada"]} por pedido.\033[0;0m')
                                print('=' * 40)
                                v += 1
                                print()

                        elif a == 1:
                            r += 1
                            if r == 1:
                                print(f'Você adicionol {cardapio_manha[1]["Prato Principal"]} ao seu pedido')
                                v += 1
                                print('=' * 40)
                                print()
                            if r >= 2:
                                print(f'\033[1;91mVocê não pode adicionar mais de um item de {cardapio_manha[1]["Prato Principal"]} ao seu pedido.\033[0;0m')
                                v += 1
                                print('=' * 40)
                                print()

                        elif a == 2:
                            t += 1
                            if t == 1:
                                print(f'Você adicionol {cardapio_manha[2]["Bebida"]} ao seu pedido')
                                v += 1
                                print('=' * 40)
                                print()
                            if t >= 2:
                                print(f'\033[1;92mVocê adicionol mais um {cardapio_manha[2]["Bebida"]} ao seu pedido.\033[0;0m')
                                v += 1
                                print('=' * 40)
                                print()

                        elif a == 3:
                            y += 1
                            if y == 1:
                                print(f'\033[1;91mInfelizmente não temos sobremesa hoje para o periodo da manhã.\033[0;0m')
                                v += 1
                                print('=' * 40)
                                print()
                            if y >= 2:
                                print(f'\033[1;91mInfelizmente não temos sobremesa hoje para o periodo da manhã.\033[0;0m')
                                v += 1
                                print('=' * 40)
                                print()

                        elif a == 999:
                            if v == 0:
                                print('\033[1;93mVoce nao fez nenhuma seleção de item.\033[0;0m')
                                sleep(1)
                                print('Finalizando ...')
                                print('='*40)
                                break

                            # Finalização do pedido
                            else:
                                print('Seu pedido foi \033[1;32m', end='')
                                if e > 0:
                                    print(f'{m} ', end="")
                                if r > 0:
                                    print(f'{n} ', end="")
                                if t == 1:
                                    print(f'{b} ', end='')
                                if t > 1:
                                    print(f'{b}({t}x) ', end='')
                                if y > 0:
                                    print(f'erro')
                            print('.\033[0;0m')
                            print('=' * 40)
                            print()
                            sleep(1)
                            print('Finalizando ...')
                            sleep(1)
                            print('Muito obrigado pela preferencia ...')
                            print('=' * 40)
                            break

                        # TRATAMENTO DE ERRO
                        else:
                            print('\033[1;91mNosso sistema não conseguiu encontrar a informação pedida.\033[0;0m')
                            print('='*40)

                    # TRATAMENTO DE ERRO
                    except:
                        print()
                        print('\033[1;91mNosso sistema não conseguiu encontrar a informação pedida.\033[0;0m')
                        print('=' * 40)

            # FORMATAÇÃO PARA PROJETO DE CLIENTES NOITE ( CONFORME ESTAVA ESCRITO NAO PODERA REPETIR A NAO SER A BATATAS).
            if periodo == "N":
                print(f'{"OPÇÕES NO CARDAPIO":^40}')
                print()
                for i, f in enumerate(cardapio):
                    print(f'{i:<3}', end='')
                    for e in f.keys():
                        print(f'{str(e):<15}', end='')
                    for d in f.values():
                        print(f'\t\t{str(d):<15}', end='')
                    print()
                print('\nObservações: Você pode repetir quantas vezes quiser as Batatas')
                print()
                print('='*40)
                e = r = t = y = v = 0
                m = cardapio[0]['Entrada']
                n = cardapio[1]['Prato Principal']
                b = cardapio[2]['Bebida']
                c = cardapio[3]['Sobremesa']

                while True:
                    try:
                        a = int(input('Escolha pelo codigo qual é o seu pedido: \n'
                                      'Digite 999 para poder fechar o pedido: '))
                        v += 1
                        print()
                        if a == 0:
                            e += 1
                            if e == 1:
                                print(f'Você adicionol {cardapio[0]["Entrada"]} ao seu pedido')
                                print('='*40)
                                print()
                            if e >= 2:
                                print(f'\033[1;91mVoce não pode adicionar mais de um item de {cardapio[0]["Entrada"]} por pedido.\033[0;0m')
                                print('=' * 40)
                                print()

                        elif a == 1:
                            r += 1
                            if r == 1:
                                print(f'Você adicionol {cardapio[1]["Prato Principal"]} ao seu pedido.')
                                print('=' * 40)
                                print()
                            if r >= 2:
                                print(f'\033[1;92mVocê adicionol mais um {cardapio[1]["Prato Principal"]} ao seu pedido.\033[0;0m')
                                print('=' * 40)
                                print()

                        elif a == 2:
                            t += 1
                            if t == 1:
                                print(f'Você adicionol {cardapio[2]["Bebida"]} ao seu pedido')
                                print('=' * 40)
                                print()
                            if t >= 2:
                                print(f'\033[1;91mVocê não pode adicionar mais de um item de {cardapio[2]["Bebida"]} ao seu pedido.\033[0;0m')
                                print('=' * 40)
                                print()

                        elif a == 3:
                            y += 1
                            if y == 1:
                                print(f'Você adicionol {cardapio[3]["Sobremesa"]} ao seu pedido')
                                print('=' * 40)
                                print()
                            if y >= 2:
                                print(f'\033[1;91mVocê não pode adicionar mais {cardapio[3]["Sobremesa"]} ao seu pedido.\033[0;0m')
                                print('=' * 40)
                                print()
                        elif a == 999:
                            if v == 1:
                                print('\033[1;93mVocê nao fez nenhuma seleção de item.\033[0;0m')
                                sleep(1)
                                print('Finalizando ...')
                                print('='*40)
                                break

                            # Finalização do pedido
                            else:
                                print('Seu pedido foi \033[1;32m', end='')
                                if e > 0:
                                    print(f'{m} ', end="")
                                if r == 1:
                                    print(f'{n} ', end='')
                                if r > 1:
                                    print(f'{n}({r}x) ', end="")
                                if t > 1:
                                    print(f'{b} ', end='')
                                if y > 0:
                                    print(f'{c}\033[0;0m')
                            print('.\033[0;0m')
                            print('=' * 40)
                            print()
                            sleep(1)
                            print('Finalizando ...')
                            sleep(1)
                            print('Muito obrigado pela preferencia ...')
                            print('='*40)
                            break
                        else:
                            print('\033[1;91mNosso sistema não conseguiu encontrar a informação pedida.\033[0;0m')
                            print('='*40)

                    # TRATAMENTO DE ERRO
                    except:
                        print()
                        print('\033[1;91mNosso sistema não conseguiu encontrar a informação pedida.\033[0;0m')
                        print('=' * 40)

    # TRATAMENTO DE ERRO
    except:
        print('\033[1;91mPor favor, digite uma opção valida\033[0;0m')
        print('='*40)