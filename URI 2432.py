# Matheus Slama Ribas
# 1811100039

import math

def Procura(num):
	Init = 1
	End = len(raio)-1
	if num > raio[End]:
		return 0
	if num <= raio[0]:
		return len(raio)
	meio = (Init + End) // 2
	if raio[meio] == num:
		return len(raio)-meio
	while Init < End:
		meio = (Init + End) // 2
		if raio[meio] >= num:
			End = meio
		else:
			Init = meio + 1
	return len(raio)-End


### MAIN ###


raio = []
C,T = map(int, input().split(' '))
for i in range(C):
	tmp = int(input())
	resultado = math.sqrt(tmp**2)
	raio.insert(i,resultado)
TotalPontos = 0

for v in range(T):
	Pt1,Pt2 = map(int, input().split(' '))
	result = math.sqrt((Pt1**2)+(Pt2**2))
	TotalPontos += Procura(result)
print(TotalPontos)
