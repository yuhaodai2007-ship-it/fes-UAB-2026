###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
RSSI = float(input("Introdueix el nivell de senyal rebut (RSSI) en dBm: "))
if RSSI >= -50:
    print("Cobertura: excel·lent")
elif RSSI >= -67:
    print("Cobertura: bona")
elif RSSI >= -75:
    print("Cobertura: feble")
else:
    print("Cobertura: molt feble")

# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
potencia = float(input("Introdueix la potència òptica rebuda en dBm: "))
if potencia >= -27 and potencia <= -8:
    print("Nivell acceptable")
elif potencia < -27:
    print("Nivell massa baix")
else:
    print("Nivell massa alt")

# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
consum = float(input("Introdueix el consum de dades en GB:"))
if consum <= 20:
    print("Consum dins del límit")
else:
    addicional = consum -20
    print(f"Consum superat en {addicional} GB addicionals")
# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
terminal = bool(input("L'indicador LOS del terminal òptic està encès? (True/False): "))
router = bool(input("L'indicador d'Internet del router està encès? (True/False): "))
if terminal and not router:
    print("Cal revisar el cable de fibra")
elif not terminal and router:
    print("Cal comprovar el servei del proveïdor")
elif not terminal and not router:
    print("La connexió sembla funcionar correctament")
else:
    print("Error en les dades introduïdes")
# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
bateria = float(input("Introdueix el percentatge de bateria disponible al SAI: "))
if bateria <20 and bateria >=0:
    print("Nivell crític")
elif bateria < 50 and bateria >= 20:
    print("Nivell baix")
elif bateria >= 50 and bateria <= 100:
    print("Nivell suficient")
else:
    print("Error en les dades introduïdes")
# Exercici 6: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
potencia_optica = int("introdueix la potència en dBm ")
if potencia_optica > -27 and potencia_optica < -8:
    print("nivell acceptable")
elif potencia_optica > -8:
    print("nivell massa alt")
else :
    print("nivell massa baix")
# Exercici 7: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
consum = float(input("Introdueix el consum de dades en GB: "))
if consum <= 20:
    print("Consum dins del límit")
else:
    addicional = consum - 20
    print(f"Consum superat en {addicional} GB addicionals")
# Exercici 8: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
LOs = bool(input("L'indicador LOS del terminal òptic està encès? (True/False): "))
Internet = bool(input("L'indicador d'Internet del router està encès? (True/False): "))
if LOs and not Internet:
    print("Cal revisar el cable de fibra")
elif not LOs and Internet:
    print("Cal comprovar el servei del proveïdor")
elif not LOs and not Internet:
    print("La connexió sembla funcionar correctament")
# Exercici 9: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
# es repeteix l'exercici 5, així que no cal tornar-lo a escriure.
# Exercici 10: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.
lantencia = float(input("Introdueix la latència en mil·lisegons: "))
perduda = float(input("Introdueix el percentatge de paquets perduts: "))
if lantencia < 0 or perduda < 0 or perduda > 100:
    print("Error en les dades introduïdes")
elif lantencia <= 30 and perduda <= 1:
    print("Connexió excel·lent")
elif lantencia <= 80 and perduda <= 3:
    print("Connexió bona")
elif lantencia <= 150 and perduda <= 5:
    print("Connexió acceptable")
else:
    print("Connexió deficient")
# Exercici 11: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.
tipus_pla = input("Introdueix el tipus de pla (bàsic o plus): ")
consum_mensual = float(input("Introdueix el consum mensual en GB: "))
if consum_mensual < 0:
    print("Consum negatiu no permès")
elif tipus_pla == "bàsic": 
    
    cost_base = 10
    limit = 10
    cost_excess = 1.50
    if consum_mensual > limit:
        cost_total = cost_base + (consum_mensual - limit) * cost_excess
    else:
        cost_total = cost_base
    print(f"Cost total: {cost_total} €")
elif tipus_pla == "plus":
    cost_base = 20
    limit = 30
    cost_excess = 0.75
    if consum_mensual > limit:
        cost_total = cost_base + (consum_mensual - limit) * cost_excess
    else:
        cost_total = cost_base
    print(f"Cost total: {cost_total} €")
# Exercici 12: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.
compte_actiu = bool(input("El compte està actiu? (True/False): "))
contrasenya_correcta = bool(input("La contrasenya és correcta? (True/False): "))
if compte_actiu and contrasenya_correcta:
    codi_correcte = bool(input("El codi de doble verificació és correcte? (True/False): "))
    if codi_correcte:
        print("Accés permès")
    else:
        print("Accés denegat: codi incorrecte") 
# Exercici 13: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.
router_encès = bool(input("El router està encès? (True/False): "))
if not router_encès:
    print("Cal encendre el router")
else:
    LOs = bool(input("L'indicador LOS del terminal òptic està encès? (True/False): "))
    Internet = bool(input("L'indicador d'Internet del router està encès? (True/False): "))
    if LOs:
        print("Cal revisar el cable de fibra")
    elif not Internet:
        print("Cal contactar amb el proveïdor")
    else:
        print("La connexió funciona correctament")
# Exercici 14: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.
afecta_critic = bool(input("La incidència afecta un servei crític? (True/False): "))
usuaris_afectats = int(input("Nombre d'usuaris afectats: "))
if usuaris_afectats < 0:
    print("Nombre d'usuaris negatiu no permès")
else:
    alternativa = bool(input("Hi ha una alternativa de connexió disponible? (True/False): "))
    if (afecta_critic and not alternativa) or (usuaris_afectats >= 50 and not alternativa):
        print("Prioritat crítica")
    elif afecta_critic or usuaris_afectats >= 10:
        print("Prioritat alta")
    else:
        print("Prioritat baixa")