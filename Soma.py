nume1=input()
nume2=input()
num1=[]
num2=[]
total = []
soma = 0
sobrou = 0
string = ""
for x in nume1:
    num1.append(x)
for x in nume2:
    num2.append(x)
if len(num1) < len(num2):
    num1.reverse()
    while len(num1) < len(num2):
        num1.append(0)
    num1.reverse()

elif len(num2) < len(num1):
    num2.reverse()
    while len(num2) < len(num1):
        num2.append(0)
    num2.reverse()

for x in range(len(num1)-1,-1,-1):
   soma = int(num1[x]) + int(num2[abs(x)]) + sobrou
   if (soma >= 10):
       sobrou = soma // 10
       final= str(soma)
       total.append(final[-1])
       if (x == 0):
           total.append(soma//10)
   else:
       total.append(soma)
       sobrou = 0

total.reverse()
print(string.join(str(x) for x in total))
