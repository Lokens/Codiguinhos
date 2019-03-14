from math import *
num=input().split()
a=float(num[0])
b=float(num[1])
c=float(num[2])
x1=(-b+sqrt(b**2-4*a*c))/2*a
x2=(-b-sqrt(b**2-4*a*c))/2*a
if x1==0 and x2==0:
    print('Impossivel calcular')
else:
    print('''R1 = {:.5f}
R2 = {:.5f}'''.format(x1,x2))