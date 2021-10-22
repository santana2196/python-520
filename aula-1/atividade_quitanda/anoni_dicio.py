operacoes = {
    'soma': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y,
}

while True:
    valor1 = int(input('Digite primeiro valor: '))
    valor2 = int(input('Digite segundo valor: '))

    print(f"A soma do {valor1} + {valor2} = {operacoes.get('soma')(valor1,valor2)}")
    print(f"A subtracao do {valor1} - {valor2} = {operacoes.get('sub')(valor1,valor2)}")
    print(f"A multiplicação do {valor1} * {valor2} = {operacoes.get('mult')(valor1,valor2)}")
    print(f"A divisao do {valor1} / {valor2} = {operacoes.get('div')(valor1,valor2)}", '\n')