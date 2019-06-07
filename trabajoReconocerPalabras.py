class ultima_instancia(object):
    
    def __init__(self, patron, alfabeto):
        self.occurrences = dict()
        for letras in alfabeto:
            self.occurrences[letras] = patron.rfind(letras)

    def __call__(self, letras):
        return self.occurrences[letras]

def boyer_moore_match(text, patron):

    alfabeto = set(text)
    last = ultima_instancia(patron, alfabeto)
    m = len(patron)
    n = len(text)
    i = m - 1  # indice texto
    j = m - 1  # indice patron
    while i < n:
        if text[i] == patron[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = last(text[i])
            i = i + m - min(j, 1+l)
            j = m - 1 
    return -1



def menu():
    

     print ("Selecciona una opción")
     print ("\t1 - Encontrar palabra en el texto")
     print ("\t2 - Determinar si es palindroma")
     print ("\t3 - Ver texto palabra invertida")
     print ("\t4 - Ver texto completo invertido")
     print ("\t5 - Ver texto completo sin modificaciones")
     print ("\t9 - salir")
    
def coincidencia(text, patron):
     print ('Texto:  %s' % text)
     p = boyer_moore_match(text, patron)
     print ('Match: %s%s' % ('.'*p, patron))
        
 
def palindromos(texto):
    
    rever = texto[::-1]
    if texto == rever:
        print("La palabra ingresada si es palindromo!!")
    else:
        print("La palabra ingresada no es palindromo!!")  

def invTexto(texto):
    cadenaInvertida = texto[::-1]
    print(cadenaInvertida)
    
while True:
    # Mostramos el menu
    text = 'esta es una prueba de busqueda'
    patron = input("Introduce su palabra: ")
    menu()
 
    # solicituamos una opción al usuario   
    opcionMenu = input("inserta un numero valor >> ")
 
    if opcionMenu=="1":
        print ("")
        coincidencia(text, patron)        
        input("Has pulsado la opción 1...\npulsa una tecla para continuar")
        
             
        
    elif opcionMenu=="2":
        print ("")
        palindromos(patron)
        input("Has pulsado la opción 2...\npulsa una tecla para continuar")
        
        
        
        
    elif opcionMenu=="3":
        print ("")
        input("Has pulsado la opción 3...\npulsa una tecla para continuar")
        
        
        
        
    elif opcionMenu=="4":
        print ("")
        invTexto(text)
        print("\n")
        invTexto(patron)
        input("Has pulsado la opción 4...\npulsa una tecla para continuar")
        
        
        
        
    elif opcionMenu=="5":
        print ("")
        print(text)
        input("Has pulsado la opción 5...\npulsa una tecla para continuar")
        
        
        
    elif opcionMenu=="9":
        break
    
    
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")