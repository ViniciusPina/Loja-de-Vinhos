#1 - crie um programa que ofereça 3 opçoes de vinho ao usuario usando while e pergunte a idade do ussuario, caso o usuario seja menor de idade finalize o programa, caso ele seja de maior inicie um programa que tenha esses 3 requisitos
#2 -ofereça 3 opçoes de vinho ao usuario  e  caso as comprar de mais de 500 reais de uma mensagem de que ele nao ira pagar taxa
#3 - apos isso printe uma mensagem de agradecimento ao cliente e informe o preço total das comparas.

preco = 0 #preco do 1 vinho

taxa = 0
preco1 =0 # preco do 2 vinho
preco2 = 0 #preco do 3 vinho
while True:
    idade =  input('Boas vindas a nossa vinheria, por favor me informe sua idade!')
    while not idade.isnumeric():
        idade = input('Por favor insira sua idade corretamente!')
    if idade.isnumeric():
        idade = int(idade)
        if idade<=17:
            print('nao e permitido a venda de bebidas alcolicas para menores de idade o programa nao ira continuar!')
            break
        init = input('ok vamos continuar com o programa, temos 3 opcoes de vinho dentre elas temos 1- vinho seco, 2- vinho tinto, 3- vinho rose' 
                     ' por favor digite o vinho desejado que corresponda ao numero')
        if init == '1':
            seco = int(input('ok, bela escolha nosso vinho seco sai por R$300,00 quantas unidades o senhor deseja levar?'))
            preco = seco * 300
            if preco > 500:
                print('voce adquiriu taxa gratis por comprar mais de 500 reais com a  gente aproveite!')
                print('\n')
            else:
                taxa = 0.25
            continuar = input('voce quer continuar comprando? caso queira digite (s) caso deseje finalizar as compras digite (n)')
            if continuar == 'n':
                print(f'o total a ser pago sera de {preco} e a taxa sera de {taxa} com isso o total sera de {(preco * taxa) + preco}')
                break
            if continuar =='s':
                init = input(
                    'ok vamos continuar com o programa, temos 3 opcoes de vinho dentre elas temos 1- vinho seco, 2- vinho tinto, 3- vinho rose'
                    'por favor digite o vinho desejado que corresponda ao numero')
        if init =='2':
            tinto = int(input('ok, bela escolha nosso vinho tinto sai por R$200,00 quantas unidades o senhor deseja levar?'))
            preco1 = tinto * 200
            if preco1 > 500:
                print('voce adquiriu taxa gratis por comprar mais de 500 reais com a  gente aproveite!')
                print('\n')
            else:
                taxa = 0.25
            continuar = input('voce quer continuar comprando? caso queira digite (s) caso deseje finalizar as compras digite (n)')
            if continuar == 'n':
                print(f'o total a ser pago sera de {preco1 + preco} e a taxa sera de {taxa} com isso o total sera de {((preco +preco1) * taxa) + (preco + preco1)}')
                break
            if continuar =='s':
                init = input(
                    'ok vamos continuar com o programa, temos 3 opcoes de vinho dentre elas temos 1- vinho seco, 2- vinho tinto, 3- vinho rose'
                    ' por favor digite o vinho desejado que corresponda ao numero')
        if init =='3':
            rose = int(input('ok, bela escolha nosso vinho rose sai por R$100,00 quantas unidades o senhor deseja levar?'))
            preco2 = rose * 100
            if preco2 > 500:
                print('voce adquiriu taxa gratis por comprar mais de 500 reais com a  gente aproveite!')
                print('\n')
            else:
                taxa = 0.25
            continuar = input('voce quer continuar comprando? caso queira digite (s) caso deseje finalizar as compras digite (n)')
            if continuar == 'n':
                print(f'o total a ser pago sera de {preco1 + preco + preco2} e a taxa sera de {taxa} com isso o total sera de {((preco +preco1 + preco2) * taxa) + (preco + preco1 + preco2)}')
                break
