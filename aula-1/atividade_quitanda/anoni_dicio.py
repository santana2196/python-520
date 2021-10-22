operacoes = {
    'soma': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y,
}

while True:
    valor1 = float(input('Digite a operação: '))
    valor2 = float(input('Digite a operação: '))

    print(operacoes.get('soma')(valor1,valor2))
    print(operacoes.get('sub')(valor1,valor2))
    print(operacoes.get('mult')(valor1,valor2))
    print(operacoes.get('div')(valor1,valor2))