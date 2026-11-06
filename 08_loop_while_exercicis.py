###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
cont = 1
while cont <= 10:
    cont = cont + 1
    print(cont)

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
cont1 = 1
num1 = 1
num2 = 1
while num1 % 2 and num2 % 2 and cont <= 20:
    sum = num1 + num2
    num1 = num1 + 1
    num2 = num2 + 1
    cont = cont +1
    print(sum)
# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
factorial = int(input("introdueix el numero"))
cont3 = 1
while factorial >= cont3:
    fact = cont3*fact
    cont3 = cont3 + 1
print(fact)
# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
contrasenya = input("introdueix la contrasenya")
while len(contrasenya) < 8:
    contrasenya = input("la contrasenya ha de ser almenys 8 caràctecs")
print("contrasenya és valida")
# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
mult = 1
num = int(input("introdueix un valor"))
while mult <= 10:
    resultat = mult * num
    print(f"{resultat}={mult}*{num} \n")
# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
N = int(input("introdueix un valor positiu"))
while num % 1 and num % num
# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
sum = int(input("introdueix un valor enter"))
while num_int != 0:
    num_int = int(input("introdueix un valor enter"))
    sum = sum + num_int
print(sum)
# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.
num_pos = int(input("introdueix un numero positiu"))
while num_pos > 0:
    cont_8 = cont_8 + 1
print(f"ha introduit {cont_8} vegades")
# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.
fibonacci = int(input("quant termesvol veure"))
sum_ans = 0
sum_fib = 1 
while sum_fib <= fibonacci:
    sum_fib = sum_ans + sum_fib
    print(sum_fib)
# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
num_res = int(input("introdueix el numero secret"))
while num_res != 7:
    if num_res > 7:
        print("el numero és més petit")
        num_res = int(input("introdueix el numero secret"))
    else :
        print("el numero és més gran")
        num_res = int(input("introdueix el numero secret"))
print("felicitat, has encertat el numero secret")