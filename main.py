
class Kniha:
    def __init__(self):
        self.nazov = nazov
        self.autor = autor
        self.ISBN = ISBN
        self.dostupna = True
        self.rok_vydania = rok_vydania
    def vypozicaj(self):
        self.dostupna = False

class Kniznica:
    def __init__(self):
        self.zoznam_knih = []

    def pridaj_knihu(self, kniha):
        self.zoznam_knih.append(kniha)

    def pozicaj_knihu(self, ISBN_knihy):
        for kniha in self.zoznam_knih:
            if (kniha.ISBN == ISBN_knihy)
                kniha.vypozicaj()