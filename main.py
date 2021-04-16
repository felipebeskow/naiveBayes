import sys

cabecalho = []
dados = []
questoes = []
matriz = []

def filterLinha(l):
  li = l.replace("\n", "").split(" ")
  l = []
  for elem in li:
    if elem:
      l.append(elem)
  return l

def naiveBayes1(questao):
  count = [[0] * (len(dados[0])+1)] * 2;
  classA = dados[0][-1]
  print(classA, count)
  for i in range(len(dados)):
    if (classA == dados[i][-1]):# and (questao[0] == dados[i][0]) :
      print(count[0])
      count[0][1] = count[0][1] + 1
    if (classA != dados[i][-1]):# and (questao[0] == dados[i][0]) :
      print(count[1])
      count[1][-1] = count[1][-1] + 1
  print(count)
  #return

def naiveBayes(questao):
  matriz = []
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
  matriz.append(atributoA)
  matriz.append(atributoB)

  

  print(matriz)

def VerificarQuestoes():
  for questao in questoes:
    naiveBayes(questao)
  #return

arquivo = open(sys.argv[1], 'r')

cabecalho = filterLinha(arquivo.readline())

linha = arquivo.readline().replace("\n", "")

while(linha != "---"):
  dados.append(filterLinha(linha))
  linha = arquivo.readline().replace("\n", "")


for linha in arquivo:
  questoes.append(filterLinha(linha))

print(cabecalho)
print("---")
print(dados)
print("---")
print(questoes)

print("\n====\n")
VerificarQuestoes()