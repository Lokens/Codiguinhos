cont100=0
cont50=0
cont20=0
cont10=0
cont5=0
cont2=0
cont1=0
cont050=0
cont025=0
cont010=0
cont005=0
cont001=0
num=float(input())
while True :
    if num>=100 :
        cont100+=1
        num-=100
    elif num>=50 :
        cont50+=1
        num-=50
    elif num>=20 :
        cont20+=1
        num-=20
    elif num>=10 :
        cont10+=1
        num-=10
    elif num>=5 :
        cont5+=1
        num-=5
    elif num>=2 :
        cont2+=1
        num-=2
    elif num>=1 :
        cont1+=1
        num-=1
    elif num>=0.50 :
        cont050+=1
        num-=0.50
    elif num>=0.25 :
        cont025+=1
        num-=0.25
    elif num>=0.10 :
        cont010+=1
        num-=0.10
    elif num>=0.05 :
        cont005+=1
        num-=0.05
    elif num>=0.01:
        cont001+= 1
        num-=0.01
    else:
        break
print ('NOTAS:')
print ('{} nota(s) de R$ 100.00'.format(cont100))
print ('{} nota(s) de R$ 50.00'.format(cont50))
print ('{} nota(s) de R$ 20.00'.format(cont20))
print ('{} nota(s) de R$ 10.00'.format(cont10)
print ('{} nota(s) de R$ 5.00'.format(cont5))
print ('{} nota(s) de R$ 2.00'.format(cont2))
print ('MOEDAS:')
print ('{} moeda(s) de R$ 1.00'.format(cont1))
print ('{} moeda(s) de R$ 0.50'.format(cont050))
print ('{} moeda(s) de R$ 0.25'.format(cont025))
print ('{} moeda(s) de R$ 0.10'.format(cont010))
print ('{} moeda(s) de R$ 0.05'.format(cont005))
print( '{} moeda(s) de R$ 0.01'.format(cont001))