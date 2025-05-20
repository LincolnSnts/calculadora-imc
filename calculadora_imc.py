# IMC = peso / (altura * altura)

def calculcar_imc():
    nome = input('Digite seu nome: ')
    peso = float(input('Digite seu peso(kg): '))
    altura = float(input('Digite sua altura(m): '))
    imc = peso / (altura * altura)
    
    if imc < 18.5:
        grau = 'Abaixo do Peso'
    elif 18.5 < imc <= 24.9:
        grau = 'Peso Normal'
    elif 25 < imc <= 29.9:
        grau = 'Sobrepeso'
    elif 30 < imc <= 34.9:
        grau = 'Obesidade Grau 1'
    elif 35 < imc <= 39.9:
        grau = 'Obesidade Grau 2'
    else:
        grau = 'Obesidade Grau 3'
    
    print(f'{nome}, seu IMC é {imc:.2f}, o que indica {grau}')

#Início da Main

while True:
    calculcar_imc()
    sair = input('Deseja calcular outro IMC? (S/N): ')
    
    if sair == 'N':
        break
