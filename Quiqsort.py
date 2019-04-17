import random

'''class Quick(object):
    def particao(self, a, ini, fim):
        pivo = a[fim-1]
        start = ini
        end = ini
        for i in range(ini,fim):
            if a[i] > pivo:
                end += 1
            else:
                end += 1
                start += 1
                aux = a[start-1]
                a[start-1] = a[i]
                a[i] = aux
        return start-1

    def quickSort(self, a, ini, fim):
        if ini < fim:
            pp = self.randparticao(a, ini, fim)
            self.quickSort(a, ini, pp)
            self.quickSort(a, pp+1,fim)
        print (a)
        return a
'''
    def randparticao(self,a,ini,fim):
        rand = random.randrange(ini,fim)
        aux = a[fim-1]
        a[fim-1] = a[rand]
        a[rand] = aux
        return self.particao(a,ini,fim)


a = [0,8,0,5,1,9,9,8,1,8,1,1,1,0,0,0,3,9]

print (f"{a}\n")
q = Quick()
print (q.quickSort(a,0,len(a)))
