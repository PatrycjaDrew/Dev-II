ensemble_eleves = {}
fichier = "aucun fichier n'a été ouvert\n"
def ouverture_fichier(nom_fichier):
    global fichier
    try:
        with open(nom_fichier) as file:
            for line in file:
                if line != "":
                    line = line.split()
                    prenom = line[0]
                    nom = line[1]
                    points = line[2]
                    ajout_dictionnaire(nom, prenom, points)
        fichier = nom_fichier
        print("Le fichier a été ouvert\n")

    except FileNotFoundError:
        print('Fichier introuvable\n')


def moyenne(liste_points):
    if len(liste_points) == 1:
        return liste_points[0]
    else:
        total = 0
        for point in liste_points:
            total += point
        return total/len(liste_points)


def ajout_dictionnaire(nom, prenom, points):
    eleve = f"{nom} {prenom}"
    if eleve in ensemble_eleves:
        ensemble_eleves[eleve].append(int(points))
    else:
        ensemble_eleves[eleve] = [int(points)]


def ajout_points(nom_fichier):
    prenom = input("Quel est le prénom de l'élève : ").strip()
    nom = input("Quel est le nom de l'élève : ").strip()
    points = input("Quel est la note sur 20 de l'élève : ").strip()
    with open(nom_fichier, 'a') as file:
        file.write(f"\n{prenom} {nom} {points}")

    ajout_dictionnaire(nom, prenom, points)
    print("Les points ont été écrits dans le fichier\n")


def affiche(point_ou_moyenne, ordre, qui):
    with open("eleves.txt", "w") as file:
        ensemble_eleves_triee = sorted(ensemble_eleves.items(), key=lambda x: moyenne(x[1]))
        if ordre == 'D':
            ensemble_eleves_triee.reverse()

        for key, value in ensemble_eleves_triee:
            ligne_affichee = f"{key} : {moyenne(value)}"
            if point_ou_moyenne == 'P':
                ligne_affichee += f" => {value}"
            file.write(ligne_affichee + "\n")

            if qui == 'T':
                print(ligne_affichee)
            elif qui == 'R' and moyenne(value) >= 10:
                print(ligne_affichee)
            elif qui == 'E' and moyenne(value) < 10:
                print(ligne_affichee)
        print("\n")



reponse_utilisateur = ""

while reponse_utilisateur.lower() != 'fin':
    print("Pour étaindre le programme écrivez 'fin'")
    print("Que voulez vous faire?\n"
          "A : ouvrir un fichier\n"
          "B : écrire dans le fichier\n"
          "C : afficher les résultats de tous les élèves\n")
    reponse_utilisateur = input(">> ")

    if reponse_utilisateur.upper().strip() == "A":
        nouveau_fichier = input("nom du fichier : ")
        ouverture_fichier(nouveau_fichier)
    elif reponse_utilisateur.upper().strip() == 'B':
        if fichier == "aucun fichier n'a été ouvert\n":
            print("aucun fichier n'a été ouvert, vous devez d'abord ouvrir un fichier\n")
        else:
            ajout_points(fichier)
    elif reponse_utilisateur.upper().strip() == 'C':
        if ensemble_eleves == {}:
            print("aucun élève a été enregistré dans le programme\n"
                  "vous avez pas ouvert de fichier ou le fichier ouvert était vide\n")
        else:
            try:
                qui_afficher = input("Voulez vous afficher le résultats de\n"
                                     "T : tous les élèves\n"
                                     "R : les élèves qui ont réussi\n"
                                     "E : les élèves qui ont réussi\n"
                                     ">> ").upper().strip()
                if qui_afficher not in ['T', 'R', 'E']:
                    raise ValueError("L'entrée est invalide, écrivez T, R ou E")

                quel_affichage = input("Voulez vous afficher\n"
                                 "M : uniquement les moyennes\n"
                                 "P : les moyennes avec tous les points >>").upper().strip()
                if quel_affichage not in ['M', 'P']:
                    raise ValueError("L'entrée est invalide, écrivez M ou P")

                ordre = input("Croissant (C) ou Décroissant (D) >>").upper().strip()
                if ordre not in ['C', 'P']:
                    raise ValueError("L'entrée est invalide, écrivez C ou P")

                affiche(quel_affichage, ordre, qui_afficher)
            except ValueError as e:
                print(e)
    elif reponse_utilisateur.lower() != "fin":
        print("Commande introuvable\n"
              "les commandes sont : A,B,C ou fin\n")
