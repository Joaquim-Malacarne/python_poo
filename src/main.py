from frota import *

def operar_carro(carro: Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

    print('Infos atuais do carro')
    print(carro)

if __name__ == "__main__":
    print('Cadastre carro1')
    nm_modelo = input('Digite o modelo do carro1: ')
    nm_marca = input('Digite a marca do carro1: ')
    nm_cor = input('Digite a cor do carro1: ')
    kms = 0.0

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, kms, motor = False)

    print('Cadastre carro2')
    nm_modelo = input('Digite o modelo do carro2: ')
    nm_marca = input('Digite a marca do carro2: ')
    nm_cor = input('Digite a cor do carro2: ')

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, kms, motor = False)


    '''
    Controlando o carro até ele atingir 600 Km
    '''
    while carro1.odometro < 600 and carro2.odometro < 600:
        try:
            print('1- Controlar carro1')
            print('2- Controlar carro2')

            op = 0
            while op not in (1, 2):
                op = int(input("Digite as opcoes[1 ou 2]: "))

            if op == 1:
                operar_carro(carro1)
            elif op == 2:
                operar_carro(carro2)
        except Exception as e:
            print("Erro!")
            print(e)

    carro1.desligar()
    carro2.desligar()
    if (carro1.odometro > 600):
        print(carro1)
    if (carro2.odometro > 600):
        print(carro2)
    print('Parar para trocar óleo!!!')

