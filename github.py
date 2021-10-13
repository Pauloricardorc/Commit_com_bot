import os
import time

from tqdm import tqdm

def InitialRepo():
    print('Iniciando git')
    try:
        os.system('git init')
        print('\n')
        for i in tqdm(range(3)):
            time.sleep(1)
    except:
        print('Um erro ocorreu no init do git')
        return
    print('\n')

def InitialConfig(name, email, repo):
    print('Vamos configurar seu ambiente para que possamos fazer o login do github\n')
    try:
        os.system(f'git config user.name "{name}"')
        os.system(f'git config user.email "{email}"')
        respRepo = bool(os.system(f'git remote add origin {repo}'))
        if respRepo == False:
            for i in tqdm(range(3)):
                time.sleep(1)
            print('Tudo configurado vamos continuar')
        else:
            response = input('Um repositorio já está configurado deseja excluir ? [S]:[N]')
            if response.lower() == 'sim' or response.lower() == 's':
                os.system('git remote rm origin')
    except:
        print('Erro ao configurar seu perfil do github')
        return
    print('\n')

def Commit(message):
    arquivos = input('Você deseja adicionar todos os arquivos: [S]:[N] ? ')
    if arquivos.lower() == 'sim':
        gitIgnore = input('OK, certifique-se de ter uma .gitignore [S]:[N] ? ')
        if gitIgnore == 'sim':
            os.system('git add .')
    elif  arquivos.lower() == 'não' or arquivos.lower() == 'nao' or arquivos.lower() == 'n':
        arquivoCommit = input('Qual o nome do arquvio a ser adicionando no commit ? ')
        try:
            message = message.replace(' ', '-')
            os.system(f'git add {arquivoCommit}')
            os.system(f'git commit -m {message}')
        except:
            print('Erro, parace que esse arquivo nÃ£o foi encontrado')
            return

def Push():
    print('Ok, vamos enviar seu commit para o github')
    os.system('git push origin master')

print('''
Bem vindo, vou lhe ajudar a fazer seu commit de uma forma mais intuitiva.
Algumas informaçãoes que serão úteis para o processo:

1) username (nome usado no github)
2) email (usado no github)
3) repositorio (link fornecido no seu repositorio)

''')
name = input('Digite seu username: ')
email = input('Digite seu email: ')
repo = input('Digite o link do repositorio: ')

print('\nOk, vamos começar 🚀\n')

InitialRepo()
InitialConfig(name, email, repo)
message = input('Digite uma mensagem para o seu commit: ')
Commit(message)
Push()