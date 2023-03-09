from HP_menu import menus


class Resto:

    def __init__(self,id,naam):
        self.id = id
        self.naam = naam
        self.menu = menus[0]

    def __str__(self):
        return "{} {}".format(self.id,self.naam)


    def toon_menu(self):
        for gerecht in self.menu.values():
            print(gerecht)



r = Resto("r1","Casa Dario")
r.toon_menu()

