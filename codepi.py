resposta=[]
teste = int(input())
for a in range(teste) :
    nada=False
    matriz=[]
    for i in range(9) :
        matriz.append(list(map(int,input().split(" "))))
    for lineas in matriz :
        for colun in lineas :
            if lineas.count(colun)>1 : nada=True
    for i in range(9) :
        nums=[]
        for lineas in matriz :
            if not(lineas[i] in nums) : nums.append(lineas[i])
        if len(nums)!=9 :
            nada=True
    for lineasm in range(0,9,3) :
        nums1=[]
        nums2=[]
        nums3=[]
        for lineas in range(lineasm,lineasm+3) :
            for colunm in range(0,9,3) :
                for colun in range(colunm,colunm+3) :
                    if colunm==0 :
                        if not(matriz[lineas][colun] in nums1) : nums1.append(matriz[lineas][colun])
                    if colunm==3 :
                        if not(matriz[lineas][colun] in nums2) : nums2.append(matriz[lineas][colun])
                    if colunm==6 :
                        if not(matriz[lineas][colun] in nums3) : nums3.append(matriz[lineas][colun])
        if len(nums2)!=9 : nada=True
        if len(nums3)!=9 : nada=True
        if len(nums1)!=9 : nada=True
    resposta.append([])
    resposta[-1].append("Instancia " + str(a+1))
    if nada : resposta[-1].append("NAO")
    else : resposta[-1].append("SIM")
for i in resposta :
    print(i[0])
    print(i[1])
    print()