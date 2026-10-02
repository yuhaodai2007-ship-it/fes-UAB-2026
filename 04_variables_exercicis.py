###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom_encaminador = "TP-Link Archer C7"
ubicacio = "Sala d'estar"
nombre_port = 4
estat = True
print(f"L'encaminador {nom_encaminador} està en ubicació : {ubicacio}, té {nombre_port} ports i el seu estat : {estat}")
# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
GB_inclosos = 10
GB_consumits = 3
GB_restants = GB_inclosos - GB_consumits
print(f"Queden {GB_restants} GB")
GB_consumits = 5
GB_restants = GB_inclosos - GB_consumits
print(f"Queden {GB_restants} GB")