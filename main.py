class Kniha:
    def __init__(self, nazov, autor, ISBN, rok):
        self.nazov = nazov
        self.autor = autor
        self.ISBN = ISBN
        self.dostupnost = True
        self.rok_vydania = rok

    def stav_dostupnost(self):
        self.dostupnost = False


class Kniznica:
    def __init__(self):
        self.zoznam_knih = [kniha_1, kniha_2, kniha_3]

    def pridaj_knihu(self, kniha):
        self.zoznam_knih.append(kniha)
        print(
            f"Pridal si knihu {kniha.nazov} od {kniha.autor}, ISBN: {kniha.ISBN}, ROK: {kniha.rok_vydania}, Status: Dostupna")

    def vypozicaj_knihu(self, ISBN_kniha):
        for kniha in self.zoznam_knih:
            if kniha.ISBN == ISBN_kniha:
                kniha.stav_dostupnost()
                print(
                    f"vypozical si knihu {kniha.nazov} od {kniha.autor}, ISBN: {kniha.ISBN}, ROK: {kniha.rok_vydania}, Status: Vypozicana")

    def vyhladanie_knihy(self, nazov_kniha):
        for kniha in self.zoznam_knih:
            if kniha.nazov == nazov_kniha:
                print(f"vyhladal si {kniha.nazov}")

    def vypis(self):
        for kniha in self.zoznam_knih:
            print("kniha")


kniha_1 = Kniha("Godfather", "Mario Puzo", 325, 1999)
kniha_2 = Kniha("Faust", "J.H.Goethe", 485, 1832)
kniha_3 = Kniha("LoTR", "J.R.Tolkien", 111, 1935)

kniznica = Kniznica()
# kniznica.pridaj_knihu(kniha_1)
# kniznica.pridaj_knihu(kniha_2)
# kniznica.pridaj_knihu(kniha_3)
kniznica.vypozicaj_knihu(325)
kniznica.vyhladanie_knihy("LoTR")
kniznica.vypis()
