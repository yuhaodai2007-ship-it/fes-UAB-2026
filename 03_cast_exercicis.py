###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.
###

# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
paquet = input("Introdueix el nombre de paquets: ")
print(f"Total de paquets és: {int(paquet) + 1200}")


# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
velocitat = input("Introdueix la velocitat de connexió ")
print(f"la velocitat equivalent de MB/S és: {float(velocitat)/8}")