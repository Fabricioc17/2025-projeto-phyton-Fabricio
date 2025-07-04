'''
DESCUBRA A SENHA
Fabricio
02/07/25
'''
#jogo descubra a senha é só uma faze, pode fazer quantas vezes quiser.
# Funções
from modules import limpaTela, mostraCabecalho
# a msg de entrada.
msgsCab = ['DESCRUBRA A SENHA', 'É SÓ UMA RODADA (TODAS AS RODADAS SÃO COMPOSTAS POR 4 NUMEROS', 'A DICA É MICHAEL JACKSON', 'A DICA É A SOMA DOS NUMEROS É 11']

def playgame():
  limpaTela()
  mostraCabecalho(msgsCab)
#Crar uma variável senha
  senha = 0
  sen = 0
  PALMEIRAS = 0
#Repetir até que a senha seja validada
  while (senha != 2009):
#Ler a senha informada pelo usuário
    senha = int(input('ADIVINHE A SENHA: '))
 #Mostrar a msg
    if (senha != 2009):
 #Mostrar senha invalida
      print ('Senha Invalida')
    else:
 # Acesso permitido == 2002
      print ('Acesso Permitido')
 
#msg parte 2
  print('RODADA 2, ACHOU QUE TINHA ACABADO')
  print('A DICA É COMO ESCREVER 2 SEGUIDO DE UM UM UM ')
  while (sen != 2111):
#Ler a senha informada pelo usuário
    sen = int(input('ADIVINHE A SENHA: '))
 #Mostrar a msg
  if (sen != 2111):
 #Mostrar senha invalida
    print ('Senha Invalida')
  else:
 # Acesso permitido == 2111
    print ('Acesso Permitido')

    print('RODADA 3, ÚLTIMA')
  print('A DICA É PALMEIRAS')
  while (PALMEIRAS != 1951):
#Ler a senha informada pelo usuário
    PALMEIRAS = int(input('ADIVINHE A SENHA: '))
 #Mostrar a msg
  if (PALMEIRAS != 1951):
 #Mostrar senha invalida
    print ('Senha Invalida')
  else:
 # Acesso permitido == 1951
    print ('Acesso Permitido, Parabens você ganhou, experiência')
playgame()