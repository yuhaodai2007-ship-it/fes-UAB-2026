# 📝 Exercicis sobre tuples

# 1️⃣ Crea una tupla amb els noms de 5 ciutats i mostra la segona i la penúltima ciutat.
ciutat = ("Barcelona", "Bequing", "Paris", "Berlin", "Nueva York")
print (ciutat[1])
print(ciutat[-2])
# 2️⃣ Donada una tupla amb números enters, compta quantes vegades apareix el número 3 a la tupla.
numero = (1,2,3,4,5,6,2,3,3,4,6)
num3 = numero.count(3)
print(num3)
# 3️⃣ Crea una funció que rebi una tupla amb números i retorni una tupla nova amb els números ordenats de menor a major.
def ord_tupla(tupla_valor):
    return tuple(sorted(tupla_valor))

numeros = (9,22,3,4,5,6,7,8,10,2,3)
numeros_ordenats = ord_tupla(numeros)
print(numeros_ordenats)