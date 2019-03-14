bits = str(input("Digite um numero em binario cokm 8 bits: "))
if len(bits) < 8:
    print("O número deve conter 8 bits")
else:
    tot = ''
    for x in range (len(bits)):
        if bits[x] == '1':
            tot+='0'
        else:
            tot+='1'
    tot=int(tot,2)
    tot+=1
    totdc = tot
    tot=bin(tot)[2:]

    while (len(bits) > len(tot)):
        tot = "0" + str(tot)

    if (tot[0] == "0"):
        neg=" "
    else:
        neg="-"

    print(f'Numero em complemento de 2: {tot}')
    print(f'Numero em decimal:{neg}{totdc}')


