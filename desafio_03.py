#Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas

nome_valido = False
salario_valido = False
bonus_valido = False

#1. Solicite o nome do usuario
while not nome_valido:
    try:
        nome = input("Digite o seu nome: ")

        if len(nome) == 0:
            raise ValueError('O nome não pode estar vazio')
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print(f'Nome válido: {nome}')
            nome_valido = True
    except ValueError as e:
        print(e)

#2. Digite o seu salario
while not salario_valido:
    try:
        salario = float(input("Digite o seu salário: "))
        if salario < 0:
            print('Por favor, digite um valor positivo para o salario')
        else: 
            salario_valido = True
    except ValueError:
        print('Entrada inválida')
    
#3. Digite o valor do bonus recebido 
while not bonus_valido: 
    try: 
        bonus = float(input("Digite o valor do seu bônus: "))
        if bonus < 0: 
            print('Por favor, digite um valor positivo para o bonus recebido: ')
        else: 
             bonus_valido = True
    except ValueError:
        print('Entrada inválida para bônus recebido')


#4. Calcule o valor do bonus final 
valor_bonus = 1000 + salario * bonus 

#6. mensagem personalizada
print(f' Olá! {nome} muito bom te ter por aqui! \n você possui o bonus de R${valor_bonus}')
