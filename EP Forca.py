##Tábatha Fróes 1º ADS - A
import requests
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
p = requests.get(url)
palavras = p.text.lower()
palavras = palavras.split()
from random import choice
from string import punctuation
from string import ascii_letters



forca = ['''
  +------+
         |
         |
         |
         |
+--------+''','''
  +------+
  |      |
  o      |
         |
         |
+--------+''','''
 +-------+
  |      |
  o      |
 /       |
         |
+--------+''','''
 +-------+
  |      |
  o      |
 /|      |
         |
+--------+''','''
 +-------+
  |      |
  o      |
 /|\     |
         |
+--------+''','''
 +-------+
  |      |
  o      |
 /|\     |
 /       |
+--------+''','''
 +-------+
  |      |
  o      |
 /|\     |
 / \     |
+--------+''']
certas = ''
erradas = ''
def escolhe():
    return choice(palavras)
def desenha():
    print(forca[len(erradas)])
    for c in sorteada: print(c if c in certas else '_', end = ' ')
    print()
def ganhou():
    return ''.join(sorted(set(sorteada))) == ''.join(sorted(set(certas)))
def jogar_novamente():
    x = input('Deseja jogar novamente? (SsNn)')
    return x in 'Ss'
def chute(letras):
    while True:
        x = input('Digite uma letra:').lower()
        if x not in ascii_letters: #caracter especial
            print('Caracter inválido!')
        elif x in letras:
            print('Letra repedita!')
        elif len(x) != 1:
            print('Uma única letra')
        else:
            return x

sorteada = escolhe()

while True:
    escolhe()
    desenha()
    x = chute(certas+erradas)
    if x in sorteada:
        certas = certas + x
    else:
        erradas = erradas + x
    print(f'Letras já chutadas: {certas+erradas}')

    if len(erradas) == len(forca) or ganhou():
        if len(erradas) == len(forca):
            print('Você perdeu! A palavra era:', sorteada)
            if jogar_novamente() == True:
                sorteada = ''
                certas = ''
                erradas = ''
            else:
                exit()
        elif ganhou():
            print('Você ganhou! A palavra é:', sorteada)
            if jogar_novamente() == True:
                sorteada = ''
                certas = ''
                erradas = ''
            else:
                exit()
