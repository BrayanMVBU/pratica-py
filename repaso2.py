"""def sumaarreglo(lista):
    suma=0
    for x in range(len(lista)):
        suma=suma+x
    
    return suma

arreglo = [1,2,6,3,4,5,6,7,8]
sumacompleta= sumaarreglo(arreglo)
print(sumacompleta)
"""
"""def espar(num):
    if num%2==0:
        print("es par")
    else:
        print("no es par")
        
num=6 
espar(num)    """

"""def potencia(a,b):
    result=1
    for x in range(b):
        result=result*a
        
    return result


resultado=potencia(2,4)
print(resultado)"""


"""def ordenar(lista):
    #primer elementode la lista
    menor=lista[0]
    #lista vacia
    ordenado=list()
    #recorre la lista desde 0
    for x in range(len(lista)):
        
        if menor <= lista[x]:
            ordenado=menor
        else:
            ordenado= lista[x] 
    return ordenado

arreglo = [9,2,6,20,4,5,6,7]
sumacompleta= ordenar(arreglo)
print("\n")
print(sumacompleta)"""



def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                unaLista[i], unaLista[i+1] = unaLista[i+1],unaLista[i]
                

unaLista = [54,26,93,17]
ordenamientoBurbuja(unaLista)
print(unaLista)
        

        
        
        
    
    
    
    
    
        
        
        
    
    
    
    
    
    
        
