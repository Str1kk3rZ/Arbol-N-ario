class Nodo:
        def __init__(self, valor, hijos = []):
            self.valor = valor
            self.hijos = hijos
	
def buscar(arbol, valor):
            if arbol == None:
                    return False
            elif arbol.valor == valor:
                    return True
            else:
                    return buscar_Hijos(arbol.hijos, valor)

def buscar_Hijos(lista, valor):
            if lista == []:
                    return False
            else:
                    return buscar(lista[0], valor) or buscar_Hijos(lista[1:], valor)
                

arbolEneario = Nodo(0,[Nodo(1,[Nodo(11), Nodo(12,[Nodo(121)]), Nodo(13,[Nodo(131),Nodo(132)])]),
                       Nodo(2),
                       Nodo(3,[Nodo(31), Nodo(32)])])
                       
                       

print (buscar(arbolEneario, 31))
print (buscar(arbolEneario, 3))
print (buscar(arbolEneario, 5))
