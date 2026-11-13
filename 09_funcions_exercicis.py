###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
def saludar_a(nom, salutacio = "Hola"):
    print(salutacio + nom)
saludar_a("Bob","bon dia !")
# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.
def es_parell(numero):
    if numero % 2:
        return True
    else :
        return 0
num = int(input("introdueix numero"))
es_parell(num)
#print (f"la paretat es {es_parell} ")
# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.
def mitjana(numeros):
    suma = 0
    i = 0
    for i in numeros:
        suma = suma + i
    mig = suma / len(numeros)
    print(f"la mitjana és {mig}")
    return mitjana
   
print (mitjana([10,20,30,40,50]))

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.
def suma_tot(*args):
    suma = 0 
    for j in args:
        suma = suma + args
    return suma 
print(suma_tot(2,4))
print(suma_tot(2,4,6,3,7))
print(suma_tot(1,2,3,4,5,6,7,8,9,10))
# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().
def taula_multiplicar(numero, limit = 10):
    for k in range(limit + 1):
        multi = numero * k 
        print(f"{numero} x {k} = {multi}")
lim = int(input("introdueix el limit"))
num = int(input("introdueix el numero"))
taula_multiplicar(num,lim)

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).
def mostrar_perfil(**kwargs):
    for clau, valor in kwargs.items():
        print({clau} + {valor})
mostrar_perfil(nom = "Claude", edat = "3", grau = "enginyeria")
# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.
def factorial(n):
  resultat = 1
  comptador = 1
  while comptador <= n:
    resultat *= comptador
    comptador += 1
  return resultat

def maxim(numeros):
  valor_maxim = numeros[0]
  for numero in numeros:
    if numero > valor_maxim:
      valor_maxim = numero
  return valor_maxim

print(f"El factorial de 5 és {factorial(5)}")  # 120
print(f"El màxim és {maxim([15, 5, 25, 10, 20])}")  # 25
# Exercici 8: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.
def comptar_vocals(text) :
   vocal = "aàáèéeíiïóòouúü"
   for lletra in text.lower():
    if lletra in vocal:
       cont_vocal = cont_vocal + 1
    return cont_vocal
cadena = input("introdueix la cadena")
# Exercici 9: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.
def minim_i_maxim(numeros):
   min = numeros[0]
   max = numeros[0]
   
   for num in numeros[1:]:
    if num > max:
       max = num
    elif num < min:
        min = min
   print(f"El màxim és {max} el minim és {min}")
valor = minim_i_maxim([15, 3, 42, 8, 23, 4])     
# Exercici 10: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.
def es_palindrom(text):
   text_min = text.lower()
   if text_min == text[::-1]:
      return True
   else :
      return False

print(es_palindrom("radar"))  # True
print(es_palindrom("Anna"))   # True
print(es_palindrom("Python")) # False