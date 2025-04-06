#Clase 5 de abril 2025
from collections import deque

#Control total sobre la pila
class Pila:
    def __init__(self):
        self.items = [1,2,3,4,5]
    def esta_vacia(self):       #Lista vacia
        return len(self.items)==0
    def push(self, item):       #Agregar elemento
        self.items.append(item)
    def pop(self):      #Eliminar elemento
        if self.esta_vacia():
            raise Exception("La pila está vacia")
        return self.items.pop()
    def peek(self):     #Verificar que el elemento esta al final de la pila
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return "La pila esá vacia"
    
pila = Pila()

pila.push(6)

print(pila.items[-1])
print(pila.peek())

#______________________________________________

pilaDeque = deque()

pilaDeque.append(10)
pilaDeque.append(12)
pilaDeque.append(14)
pilaDeque.append(16)
pilaDeque.append(18)
pilaDeque.append(20)

elemento = pilaDeque.pop()

print(pilaDeque)
print(elemento)
print(pilaDeque[-1])

#{[()]}
#(2*2)
#2*2+2
#2*2/(2+1)

#__________________________________________________

def balanceada(cadena):
    pila = deque()
    exp = {")":"(","}":"{","]":"["}
    #"{[()])}"
    if len(cadena)%2 == 0:
        for char in cadena:     #Recorre el elemento en la cadena
            if char in exp.values():
                pila.append(char)
                print(pila)
            elif char in exp.keys():
                if pila and pila[-1]== exp[char]:
                    pila.pop()
                else:
                    return False
        return not pila
    else:
        return False

cadena1 = "{[([])]}"
cadena2 = "([[(]})"

print(f"Cadena 1: ¿Esta balanceada? {balanceada(cadena1)}")
print(f"Cadena 2: ¿Esta balanceada? {balanceada(cadena2)}")

#_______________________________________________________

#(2+3-2) (4/2*2)
precedencia = {"+":1, "-":1, "*":2, "/":2,"^":3}

def infijo_a_posfijo(expresion):
    pila = deque()
    r = []

    for simbolo in expresion:   #Recorre simbolo en la expresión
        if simbolo.isdigit():
            r.append(simbolo)
        elif simbolo == "(":
            pila.append(simbolo)
        elif simbolo == ")":
            while pila and pila[-1] != "(":
                r.append(pila.pop())
            pila.pop()
        else:
            while pila and pila[-1] != "(" and precedencia[simbolo] <= precedencia[pila[-1]]:   #<= es igual a in "pertenece"
                r.append(pila.pop())
            pila.append(simbolo)

    while pila:
        r.append(pila.pop())
    return "".join(r)

expresion = "1/2^3*4+5" #"(1+2)^(3*4)"

print(infijo_a_posfijo(expresion))

#Para prefijo cambiar que revise primero los simbolos y luego los digitos

#____________________________________________________________

def stacksort(inputPila):
    pilaTemp = []

    while inputPila:
        current = inputPila.pop()
        while pilaTemp and pilaTemp[-1] > current:  #Si el último elemento es mayor a current entonces se sacan de la pilaTemp y se ingresan a input para después ordenar
            inputPila.append(pilaTemp.pop())
        pilaTemp.append(current)
    return pilaTemp

inputPila = [34,25,18,1,22,9,0]

print(stacksort(inputPila))

#______________________________________________________________

def invertir_secuencia(secuencia): #Invertir secuencia
    pila = []
    r = []

    for item in secuencia:
        pila.append(item)
    while pila:
        r.append(pila.pop())
    return r

secuencia = [1,2,3,4,5]

print(invertir_secuencia(secuencia))

#________________________________________________________

def es_palindromo(cadena):
    pila = []
    r = []
    cadenaOriginal = list(cadena)   #Convertir la cadena a lista

    for item in cadena:
        pila.append(item)
    while pila:
        r.append(pila.pop())

    if cadenaOriginal == r:
        return print("es palindromo")
    else:
        return print("no es palindromo")
        
cadenaPali = "oso"

es_palindromo(cadenaPali)

#________________________________________________________________

lista_fija = [None]*5
#lista_fija[4] = 1   #Indice [5] se desborda la lista y marca error

try:
    lista_fija.append(6)
except Exception as e:
    print("Error al agregar elemento o desbordado de pila")

print(lista_fija)
#___________________________________________________________________________

class ListaFija:
    def __init__(self, tam):
        self.tam = tam
        self.lista = [None]*tam
        self.indice = 0

    def agregar(self, elemento):
        if self.indice < self.tam:
            self.lista[self.indice] = elemento
            self.indice +=1
        else:
            print("Desbordamiento")
    
    def obtenerLista(self):
        return self.lista
    
listaLimite = ListaFija(5)

listaLimite.agregar(1)
listaLimite.agregar(2)
listaLimite.agregar(3)
listaLimite.agregar(4)
listaLimite.agregar(5)

listaLimite.agregar(6)  #Ingresar elemento para desbordar la lista

print(listaLimite.obtenerLista())