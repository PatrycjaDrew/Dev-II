import unittest
from script import *


class TestVerifierReponse(unittest.TestCase):
    def test_verifieReponse(self):
        self.assertEqual(verifie_reponse('A = ', ["A", "B"]), "A")

        with self.assertRaises(ValueError):
            verifie_reponse('C = ', ["A", "B"])


class TestMoyenne(unittest.TestCase):
    def test_moyenneUneEntree(self):
        self.assertEqual(moyenne([1]), 1.0)
        self.assertEqual(moyenne([10]), 10.0)

    def test_moyennePlusieursEntree(self):
        self.assertEqual(moyenne([1, 15, 2]), 6.0)
        self.assertEqual(moyenne([10, 10, 10, 10]), 10.0)
        self.assertEqual(moyenne([0, 19]), 9.5)


class TestOuvertureFichier(unittest.TestCase):
    def test_ouvertureFichierExiste(self):
        e = Ecole()
        with open('test.txt', 'w') as file:
            file.write("Harry Potter 3\nScooby Doo 11\n Harry Potter 5")

        e.ouverture_fichier('test.txt')
        self.assertEqual(e.ensemble_eleves, {'Potter Harry': [3, 5], 'Doo Scooby': [11]})

    def test_ouvertureFichierExistePas(self):
        b = Ecole()
        b.ouverture_fichier('fichierInexistant.txt')
        self.assertEqual(b.ensemble_eleves, {})


class TestAjoutDictionnaire(unittest.TestCase):
    def test_ajoutDictionnaireUnPoint(self):
        e = Ecole()
        e.ajout_dictionnaire(['prenom', 'nom', 1])
        self.assertEqual(e.ensemble_eleves, {'nom prenom': [1]})

    def test_ajoutDictionnairePlusieursPoint(self):
        b = Ecole()
        b.ajout_dictionnaire(['prenom', 'nom', 1, 14, 6, 10])
        self.assertEqual(b.ensemble_eleves, {'nom prenom': [1, 14, 6, 10]})

        b.ajout_dictionnaire(['prenom', 'nom', 20])
        self.assertEqual(b.ensemble_eleves, {'nom prenom': [1, 14, 6, 10, 20]})


class TestTri(unittest.TestCase):
    def setUp(self):
        self.a = Ecole()
        self.a.ensemble_eleves = {'A Alice': [5, 5, 5], 'B Bryan': [19, 19], 'C Clara': [6], 'D Dylan': [1, 1, 1]}

    def test_triNom(self):
        self.assertEqual(self.a.tri("N", "C"), ['A Alice', 'B Bryan', 'C Clara', 'D Dylan'])
        self.assertEqual(self.a.tri("N", "D"), ['D Dylan', 'C Clara', 'B Bryan', 'A Alice'])

    def test_triMoyenne(self):
        self.assertEqual(self.a.tri("M", "C"), [('D Dylan', [1, 1, 1]), ('A Alice', [5, 5, 5]),
                                                ('C Clara', [6]), ('B Bryan', [19, 19])])
        self.assertEqual(self.a.tri("M", "D"), [('B Bryan', [19, 19]), ('C Clara', [6]),
                                                ('A Alice', [5, 5, 5]), ('D Dylan', [1, 1, 1])])


if __name__ == '__main__':
    unittest.main()
