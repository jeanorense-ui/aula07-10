# nome = 'jean'
# idade = 16
# cidade = 'maringa'
# estado = 'parana'
# print(f'meu e {nome}. tenho {idade} anos de idade. tenho {altura}m. Moro na cidade de {cidade} do estado do {estado}')


# nome = input('digite seu nome')
# print(nome)

# n1 = int(input('digite o primeiro numero'))
# n2 = int(input('digite o segundo numero'))
# soma = n1 + n2
# print(soma)

# n1 = input('digita o seu nome ')
# n2 = input('digite o seu curso ')
# input(f'o seu nome é {n1} e o seu curso {n2}')
# n3 = int(input('digite o seu numero'))
# n4 = int(input('digite o seu segundo numero'))
# soma = n3 + n4
# mult = n3 * n4
# subtra = n3 - n4
# divis = n3 / n4
# input(f'os seus numeros somados da {soma} e em multiplicação {mult} e a subtração {subtra} e a divisão {divis}')

# n1 = 5 
# chute = int(input('escreva um numero '))

# if n1 == chute:
#     print('voce acertou ')
# else:
#     print('voce errou ')

# n1 = 5 
# tentativa = 5
# while tentativa > 0:
#     chute = int(input('escreva um numero '))
#     print(f'voce digitou {chute}')
#     if chute < n1:
#       print('o numero secreto é maior')
#     elif chute > n1:
#       print('o numero secreto é menor')
#     else:
#       print('acertou')
#       break
#     tentativa -= 1
# else:
#    print(f'seua tentativas acabaram. o numero secreto era {n1}')  

import random
nome = input('qual o seu nome? ')
quem = ['meu cachorro', 'meu primo', 'o wi-fi', 'o professor de matematica, meu gato']
acao =['comeu', 'apagau', 'escondeu', 'hacakeon', 'derrubou café']
alvo =['meu caderno', 'meu notebook', 'minha tarefa', 'meu pen drive']

sorteio_quem = random.choice(quem)
sorteio_acao = random.choice(acao)
sorteio_alvo = random.choice(alvo)

print(f'professor, desculpa {sorteio_quem.capitalize()} {sorteio_acao} {sorteio_alvo}')
print(f'assinado: {nome} ')