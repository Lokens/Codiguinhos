print("Digite o texto a ser convertido para ASCII (sem acentos):"); x = input(); cont = 0; dat=open('texto','w')
texto= ""; texto+= "v2.0 raw\n"
for a in x:
    b = list(str(hex(ord(a.lower()))[2:])); c = str(int(b.pop(0)) - 2); b.insert(0,c); d = "".join(b); texto+=d;
    cont+=1;
    if cont < 8: texto+=" ";
    else: texto+="\n"; cont=0;
dat.write(texto); dat.close();
print(texto);