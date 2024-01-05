class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : -
        POST : crée un objet Fraction avec un dénominateur et un numérateur simplifié
        RAISE : TypeError si le numérateur ou dénominateur ne sont pas des nombres entiers
                ZeroDivisionError si le dénominateur == 0
        """

        if type(num) != int or type(den) != int:
            raise TypeError("Le numérateur et le dénominateur doivent être des nombres entiers")

        if den == 0:
            raise ZeroDivisionError("Le dénominateur doit être différent de 0")

        diviseur_commun = 1
        for diviseur in range(1, den + 1):
            if (num % diviseur) == 0 and (den % diviseur) == 0:
                diviseur_commun = diviseur

        self.__num = num // diviseur_commun
        self.__den = den // diviseur_commun

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : -
        POST : retourne une chaine de charactère qui est une fraction réduite
        """

        return self.as_mixed_number()

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : une valeur associé à self.num et self.den qui est un nombre,
              self.den doit être différent de 0
        POST : retourne une chaine de charactère qui est la fraction réduite
        """

        nbre_entier = self.numerator // self.denominator
        if self.is_zero():
            return "0"
        elif nbre_entier == 0:
            return f"{self.numerator}/{self.denominator}"
        elif self.is_integer():
            return str(nbre_entier)
        else:
            return f"{nbre_entier} + {self.numerator - (nbre_entier * self.denominator)}/{self.denominator}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other est un objet de la classe Fraction
         POST : renvoi un nouvel objet Fraction qui est le résultat de self + other qui sont tous les 2 des fractions
         """
        if self.denominator == other.denominator:
            num = self.numerator + other.numerator
            den = self.denominator
        else:
            num = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            den = self.denominator * other.denominator

        return Fraction(num, den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : other est un objet de la classe Fraction
        POST : renvoi un nouvel objet Fraction qui est le résultat de self - other qui sont tous les 2 des fractions
        """
        if self.denominator == other.denominator:
            num = self.numerator - other.numerator
            den = self.denominator
        else:
            num = (self.numerator * other.denominator) - (other.numerator * self.denominator)
            den = self.denominator * other.denominator

        return Fraction(num, den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other est un objet de la classe Fraction
        POST : renvoi un nouvel objet Fraction qui est le résultat de self * other qui sont tous les 2 des fractions
        """
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator

        return Fraction(num, den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other est un objet de la classe Fraction
        POST : renvoi un nouvel objet Fraction qui est le résultat de self / other qui sont tous les 2 des fractions
        RAISE : ZeroDivisionError si other = 0
        """
        if other.is_zero():
            raise ZeroDivisionError("Division par zéro pas possible")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator

        return Fraction(num, den)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : other est un objet de la classe Fraction
        POST : renvoi un nouvel objet Fraction qui est le résultat de self ** other qui sont tous les 2 des fractions
        """
        exposant = other.numerator / other.denominator

        num = int(self.numerator ** exposant)
        den = int(self.denominator ** exposant)

        return Fraction(num, den)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other est un objet de la classe Fraction
        POST : renvoi True si self et other sont égaux et False si non

        """
        return (self.numerator * other.denominator) == (self.denominator * other.numerator)

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : self.denominator doit être différent de 0
        POST : renvoi un float qui est la valeur décimale de la fraction
        """
        return self.numerator/self.denominator

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : -
        POST : renvoi True si la fraction vaux 0 et False sinon
        """
        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : le dénominateur doit être différent de 0
        POST : renvoie True si la fraction représente un entier et False si non
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : le dénominateur doit être différent de 0
        POST : renvoi True si la valeur absolue de la fraciton est plus grande que 1 et False sinon
        """

        return abs(self.numerator/self.denominator) < 1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : -
        POST : renvoi True si le paramètre num est 1 et False sinon
        """
        diviseur_commun = 1

        for diviseur in range(1, self.numerator + 1):
            if (self.numerator % diviseur) == 0 and (self.denominator % diviseur) == 0:
                diviseur_commun = diviseur

        return self.numerator / diviseur_commun == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : other est un objet de la classe Fraction
        POST : renvoi True is il y a que 1 unité de différence entre self et other
        """
        return (self - other).is_unit()


if __name__ == "__main__":
    a = Fraction(3, 3)
    b = Fraction(1, 3)
    c = Fraction(2, 2)
    d = Fraction(2, 6)
    print(f"3/3 = {a}")
    print(f"2/6 = {d}")
    print(f"3/3 - 1/3 = {a - b}")
    print(f"3/3 + 1/3 = {a + b}")
    print(f"1/3 * 2/2 = {b * c}")
    print(f"3/3 / 1/3 = {a/b}")
    print(f"1/3 == 2/6 {b == d}")
    print(f"3/3 == 1/3 {a == b}")
    print(f"1/3 = {float(b)}")
    print(f"O/1 is_zero = {Fraction(0, 1).is_zero()}")
    print(f"3/3 is_integer = {a.is_integer()}")
    print(a.is_adjacent_to(b))
    print(f"1/3 ** 2/1 = {b ** Fraction(2, 1)}")
