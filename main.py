##############################################################
# Autoria: Felipe Beskow <felipeBeskow@outlook.com>
# Algoritmo: Naïves-Bayes
# Disciplina: Sistemas Inteligentes Aplicados
# Professor: Arnaldo Candido Junior
# Repositório: https://github.com/felipebeskow/naiveBayes
# Por favor manter os créditos
##############################################################

#importe para permitir a entrada de paramêtros
import sys

#inicialização de variáveis globais
cabecalho = []
dados = []
questoes = []
matriz = []

#função para limpar string
def filterLinha(l):
  li = l.replace("\n", "").split(" ")
  l = []
  for elem in li:
    if elem:
      l.append(elem)
  return l

#cereja do bolo - implementação do algoritmo
def naiveBayes(questao):
  atributoA = []
  atributoB = []

  classeA = dados[0][-1]

  for k in range(len(questao)-1):
    A = 0
    B = 0
    for i in range(len(dados)):
      if(classeA == dados[i][-1]) and (questao[k] == dados[i][k]) :
        A += 1
      elif (classeA != dados[i][-1]) and (questao[k] == dados[i][k]) :
        B += 1
    atributoA.append(A)
    atributoB.append(B)
  
  A=0
  B=0
  for i in range(len(dados)):
    if(classeA == dados[i][-1]) :
      A += 1
    else :
      classeB = dados[i][-1]
      B += 1
  atributoA.append(A)
  atributoB.append(B)

  A=atributoA[-1]/len(dados)
  B=atributoB[-1]/len(dados)
  for i in range(len(questao)-1):
    A *= atributoA[i]/atributoA[-1]
    B *= atributoB[i]/atributoB[-1]

  questao[-1] = classeA
  questao.append(A)
  questao.append(classeB)
  questao.append(B)
  return questao

#chamada do algoritmo para cada questão
def VerificarQuestoes():
  for questao in questoes:
    matriz.append(naiveBayes(questao))

#printar resultado
def FormataSaida():
  for linha in matriz:
    outPut = ""
    for i in range(len(cabecalho)-1):
      outPut += f'{cabecalho[i]}={linha[i]}'
      if i < len(cabecalho)-2:
        outPut += ', '
    outPut += " ==> "
    if(linha[-3]>linha[-1]):
      outPut += cabecalho[-1] + "=" + linha[-4]
    else:
      outPut += cabecalho[-1] + "=" + linha[-2]
    outPut += f"\n\t{linha[-4]}={linha[-3]}; {linha[-2]}={linha[-1]}"
    print(outPut)

#implementação da "main"
##MAIN##

arquivo = open(sys.argv[1], 'r')

cabecalho = filterLinha(arquivo.readline())

linha = arquivo.readline().replace("\n", "")

while(linha != "---"):
  dados.append(filterLinha(linha))
  linha = arquivo.readline().replace("\n", "")

for linha in arquivo:
  questoes.append(filterLinha(linha))

arquivo.close()

VerificarQuestoes()
FormataSaida()
