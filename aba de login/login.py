# Parte 3 do Código de Login - Opção de criar conta + Correção de Login e senha + Erros de digitação do Usuário + Design melhor.

print('----------Bem vindo ao Site do Pretins----------')
interface = int(input('O que deseja?\nCriar conta = 1\nLogar = 2\n'))

while interface != 1 and interface != 2:
    print('')
    print("----------Não há essa opção nas alternativas [X]----------")
    interface = int(input('O que deseja?\nCriar conta = 1\nLogar = 2\n'))

if interface == 1:
    print('')
    print('----------Aba de Criação de Conta----------')
    nome_do_usuario = input('Digite qual será o seu nome: ')
    senha_do_usuario = input('Digite qual será sua senha: ')

    print('')
    print('----------Conta criada com sucesso!----------')
    print('')

    etapa2 = int(input('Digite 3 para Abrir a Aba de Login: '))

    while etapa2 != 3:
        print('')
        print("----------O Número Digitado Está Incorreto [X]----------")
        etapa2 = int(input('Digite 3 para Abrir a Aba de Login: '))
        print('')

if interface == 2 or etapa2 == 3:
    print('')
    print('----------Aba de Login do usuário!----------')
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')
    print('')

nome_correto = nome_do_usuario

senha_correta = senha_do_usuario

while senha != senha_correta or nome != nome_correto:
    print('')
    print('----------Login ou/e senha incorretos [X]----------')
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')
    print('')

else:
    print('')
    print("----------Logado com sucesso!----------")


# OBS: Ainda há alguns erros em relação ao login direto. Parece que o login armazenado é o criado anteriormente - Necessito de mais conhecimento na área para correção.
# Possível solução para esse problema: Criar um Banco de Dados.
