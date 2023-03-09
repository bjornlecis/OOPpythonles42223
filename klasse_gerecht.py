class Gerecht:

    def __init__(self,naam,omschrijving,prijs):
        self.naam =  naam
        self.omschrijving = omschrijving
        self.prijs = prijs

    def __str__(self):
        return f"{self.naam} {self.omschrijving} {self.prijs}"

