from klasse_gerecht import Gerecht

g1 = Gerecht("Tomatensoep","Verse huisgemaakte tomatensoep met brood",5)
g2 = Gerecht("Steak Friet","Een Heerlijke steak met een dakje van steppengras",24)
g3 = Gerecht("Tiramisu","Huisgemaakte Tiramisu met speculoos en amaretto",13)
g4 = Gerecht("Kapsalon","Kebab met kaas en frietjes",10)
g5 = Gerecht("Baklava","Turkse dessert met honing en thee",10)
g6 = Gerecht("Fishsteak met appelmoes","Fishsteak met appelmoes op grootmoeders wijze",14)

menu_dario = {"voorgerecht":g1,"hoofdgerecht":g2,"dessert":g3}
menu_toon = {"hoofdgerecht":g4,"nagerecht":g6,"dessert":g5}

menus = [menu_dario,menu_toon]

def print_menu():
    for menu in menus:
        print("#################Menu###########")
        for naam_menu,gerecht in menu.items():
            print("*******************************************")
            print(naam_menu)
            print("*******************************************")
            print(gerecht)
