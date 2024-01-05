def verifie_reponse(message, reponse_possible):
    """ vérifie que l'utilisateur a introduit une réponse valide

    PRE: 'message' est une chaine de caractères qui est la question posé à l'utilisateur
         'reponse_possible' est une liste qui contient les réponse que l'utilisateur est autorisé à donné
    POST: retourne la réponse de l'utilisateur si elle est validé
    RAISE: ValueError si la réponse de l'utilisateur n'est pas dans 'reponse_possible'
    """
    reponse_utilisateur = input(message).strip().upper()
    if reponse_utilisateur in reponse_possible:
        return reponse_utilisateur
    else:
        raise ValueError("Commande introuvable !")


def moyenne(liste_points):
    """ calcule la moyenne de tous les points contenu dans une liste

    PRE : 'liste_points' doit être une liste qui n'est pas vide et qui contient des nombres
    POST : retourne la moyenne de tous les points contenu dans 'lite_points'
    """
    if len(liste_points) == 1:
        return liste_points[0]
    else:
        total = 0
        for point in liste_points:
            total += point
        return total / len(liste_points)


class Ecole:
    def __init__(self):
        self.ensemble_eleves = {}
        self.aide = ("fin : arrête le programme\n"
                     "aide : pour obtenir de l'aide\n"
                     "O : ouvrir un fichier\n"
                     "A : afficher la liste des élèves et leurs moyenne\n"
                     "S : afficher les points et la moyenne d'un seul élève\n")

    def ouverture_fichier(self, nom_fichier):
        """ ouvre un fichier texte, lit sont contenu et l'ajoute dans un dictionnaire

            PRE : 'nom_fichier' est le nom d'un fichier texte existant
            POST : ouvre et lit le fichier si il existe
                   ajoute chaque ligne du fichier dans le dictionnaire 'ensemble_eleves'
                   affiche à l'écran un message à l'utilisateur pour lui dire que le fichier a été ouvert correctement
            """

        try:
            with open(nom_fichier) as file:
                for line in file:
                    if line != "":
                        line = line.split()
                        self.ajout_dictionnaire(line)
            print("Le fichier a été ouvert\n")
        except FileNotFoundError:
            print('Fichier introuvable\n')

    def ajout_dictionnaire(self, liste):
        """ ajoute le contenu d'une liste dans un dictionnaire
        PRE: le premier élément de la liste doit être un nom
             le deuxième élément de la liste doit être un prénom
             le reste de la liste doivent être des chaines de caractères qui représentent des nombres entiers
        POST: création d'un nouvel élève avec des points dans ensemble_eleves
              ou ajout de nouvaux points dans ensemble_eleves pour les élèves déjà existants
        """
        nom = liste[1]
        prenom = liste[0]
        points = liste[2:]

        eleve = f"{nom} {prenom}"
        if eleve in self.ensemble_eleves:
            for point in points:
                self.ensemble_eleves[eleve].append(int(point))
        else:
            self.ensemble_eleves[eleve] = []
            for point in points:
                self.ensemble_eleves[eleve].append(int(point))

    def tri(self, quel_tri, ordre):
        """ trie un dictionnaire soit en fonction de nom soit en fonction des moyennes

        PRE: 'quel_tri' doit être une chaine de caractères qui indique si le tri se fait sur les moyennes ou les noms
             'ordre' doit être une chaine de caractères qui indique si le tri doit être croissant ou décroissant
        POST: retourne une liste triée en fonction des critères indiqué par l'utilisateur dans les préconditions
        """
        if quel_tri == "M":
            ensemble_eleves_triee = sorted(self.ensemble_eleves.items(), key=lambda x: moyenne(x[1]))
        else:
            ensemble_eleves_triee = sorted(self.ensemble_eleves.keys())
        if ordre == 'D':
            ensemble_eleves_triee.reverse()
        return ensemble_eleves_triee

    def affiche(self, liste_triee, qui, quel_tri):
        """ affiche à l'utilisteur la liste des élèves ainsi que leur moyenne

        PRE: 'liste_triee' doit être une liste qui représente ensemble_eleves trié en fonction des critères de
             l'utilisateur
             'qui' doit être une chaine de caractères qui indique quels élèves vont être affichés:
             tous - ceux qui ont réussi - ceux qui on raté
             'quel_tri' doit être une chaine de caractères qui indique si le tri se fait sur les moyennes ou les noms
        POST: écrit dans le fichier 'eleves.txt' la liste du groupe que l'utilisateur a sélectionné avec leur moyenne
              affiche à l'écran la liste du groupe que l'utilisateur a sélectionné avec leur moyenne
        """
        with open("eleves.txt", "w") as file:
            print(10 * '---------')
            if quel_tri == "M":
                for key, value in liste_triee:
                    ligne_affichee = f"{key} : {moyenne(value)}"

                    if qui == 'T':
                        print(ligne_affichee)
                        file.write(ligne_affichee + "\n")
                    elif qui == 'R' and moyenne(value) >= 10:
                        print(ligne_affichee)
                        file.write(ligne_affichee + "\n")
                    elif qui == 'E' and moyenne(value) < 10:
                        print(ligne_affichee)
                        file.write(ligne_affichee + "\n")
            else:
                for key in liste_triee:
                    ligne_affichee = f"{key} : {moyenne(self.ensemble_eleves[key])}"

                    if qui == 'T':
                        print(ligne_affichee)
                        file.write(ligne_affichee + "\n")
                    elif qui == 'R' and moyenne(self.ensemble_eleves[key]) >= 10:
                        print(ligne_affichee)
                        file.write(ligne_affichee + "\n")
                    elif qui == 'E' and moyenne(self.ensemble_eleves[key]) < 10:
                        print(ligne_affichee)
                        file.write(ligne_affichee + "\n")
            print(10 * '---------')

    def demarre(self):
        reponse_utilisateur = ' '
        print(self.aide)
        while reponse_utilisateur.lower() != 'fin':
            reponse_utilisateur = input("Que voulez-vous faire : ").upper().strip()
            if reponse_utilisateur == 'O':
                reponse_utilisateur = input("Quel fichier voulez vous ouvrir : ")
                self.ouverture_fichier(reponse_utilisateur)
            elif reponse_utilisateur == "A":
                if self.ensemble_eleves == {}:
                    print("aucun élève a été enregistré dans le programme\n"
                          "vous avez pas ouvert de fichier ou le fichier ouvert était vide\n")
                else:
                    try:
                        quel_tri = verifie_reponse("Afficher les élèves trié en fonction des\n"
                                                   "N : noms\n"
                                                   "M : moyennes\n"
                                                   ">> ", ["N", "M"])

                        ordre = verifie_reponse("Afficher de manière\n"
                                                "C : Croissante\n"
                                                "D : Décroissante\n"
                                                ">> ", ["C", "D"])
                        qui_afficher = verifie_reponse("Voulez vous afficher le résultats de\n"
                                                       "T : tous les élèves\n"
                                                       "R : les élèves qui ont réussi\n"
                                                       "E : les élèves qui ont réussi\n"
                                                       ">> ", ["T", "R", "E"])

                        liste_triee = self.tri(quel_tri, ordre)

                        self.affiche(liste_triee, qui_afficher, quel_tri)
                    except ValueError as e:
                        print(e)

            elif reponse_utilisateur == "S":
                nom = input("Quel est le nom de l'élève : ").strip()
                prenom = input("Quel est le prénom de l'élève : ").strip()
                if f"{nom} {prenom}" in self.ensemble_eleves:
                    points = self.ensemble_eleves[f"{nom} {prenom}"]
                    print(10 * '---------')
                    print(f"Voici tous les points qu'a obtenu {nom} {prenom} :\n"
                          f"{points}\n"
                          f"Ça lui donne une moyenne de {moyenne(points)}")
                    print(10 * '---------')
                else:
                    print(f"Aucun élève avec le nom {nom} {prenom} n'a été trouvé")
            elif reponse_utilisateur == "AIDE":
                print(self.aide)
            else:
                if reponse_utilisateur != "FIN":
                    print("Commande introuvable")


a = Ecole()
a.demarre()
