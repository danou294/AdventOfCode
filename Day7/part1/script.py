def evaluer_main(main):
    frequences = {}
    for carte in main:
        if carte in frequences:
            frequences[carte] += 1
        else:
            frequences[carte] = 1

    tri_frequences = sorted(frequences.values(), reverse=True)

    if tri_frequences[0] == 5:
        return "Cinq d'une sorte", tri_frequences
    elif tri_frequences[0] == 4:
        return "Carré", tri_frequences
    elif tri_frequences[0] == 3:
        if tri_frequences[1] == 2:
            return "Full House", tri_frequences
        else:
            return "Brelan", tri_frequences
    elif tri_frequences[0] == 2:
        if tri_frequences[1] == 2:
            return "Deux Paires", tri_frequences
        else:
            return "Une Paire", tri_frequences
    else:
        return "Carte Haute", tri_frequences

def trier_par_type(mains):
    mains_par_type = {
        "Cinq d'une sorte": [],
        "Carré": [],
        "Full House": [],
        "Brelan": [],
        "Deux Paires": [],
        "Une Paire": [],
        "Carte Haute": []
    }

    for main in mains:
        type_main, _ = evaluer_main(main)
        mains_par_type[type_main].append(main)

    return mains_par_type

def comparer_cartes(main1, main2, valeur_cartes):
    for i in range(5):
        if valeur_cartes[main1[i]] > valeur_cartes[main2[i]]:
            return True
        elif valeur_cartes[main1[i]] < valeur_cartes[main2[i]]:
            return False
    return False  # Égalité

def classer_mains(mains):
    valeur_cartes = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    mains_par_type = trier_par_type(mains)
    mains_classees = []

    for type_main in ["Cinq d'une sorte", "Carré", "Full House", "Brelan", "Deux Paires", "Une Paire", "Carte Haute"]:
        mains_type = mains_par_type[type_main]
        mains_type.sort(key=lambda main: [valeur_cartes[carte] for carte in main], reverse=True)
        mains_classees.extend(mains_type)

    return mains_classees

# Adapter l'algorithme pour lire les mains et les enchères à partir du nouvel input

def lire_input_et_extraire_mains_avec_encheres(filepath):
    """
    Lit le fichier d'input et extrait les mains et les enchères.

    :param filepath: Chemin du fichier contenant les mains et les enchères.
    :return: Liste de tuples contenant les mains et les enchères associées.
    """
    mains_et_encheres = []
    with open(filepath, 'r') as file:
        for ligne in file:
            # Séparer la main et l'enchère
            partie_main, enchere = ligne.strip().split()
            mains_et_encheres.append((partie_main, int(enchere)))
    return mains_et_encheres

def classer_mains_avec_encheres(mains_et_encheres):
    # Extraire uniquement les mains pour le classement
    mains_seules = [main for main, enchere in mains_et_encheres]
    # Classer les mains
    mains_classees = classer_mains(mains_seules)

    # Calculer le nombre total de mains
    nombre_mains = len(mains_classees)

    # Associer chaque main classée à son enchère et calculer le gain
    resultats = []
    for i, main_classee in enumerate(mains_classees):
        rang = nombre_mains - i  # Le rang 1 est attribué à la main la plus faible
        enchere = next(enchere for main, enchere in mains_et_encheres if main == main_classee)
        gain = enchere * rang
        resultats.append((main_classee, rang, gain))

    return resultats

# Lire les mains et les enchères à partir du fichier input
mains_et_encheres = lire_input_et_extraire_mains_avec_encheres('input.txt')

# Exécution du classement avec les enchères
resultats = classer_mains_avec_encheres(mains_et_encheres)

# Calculer le gain total
gain_total = sum(gain for _, _, gain in resultats)



# Affichage des mains classées avec rang et gain
for main, rang, gain in resultats:
    print(f"Main: {main}, Rang: {rang}, Gain: {gain}")
print(f"Gain total: {gain_total}")

