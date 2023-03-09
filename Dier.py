class Dier:

     def __init__(self,naam,soort):
         self.naam = naam
         self.soort = soort

     def print_info(self):
         print(self.naam,self.soort)

"""Hond = Dier("Samson","Hond")
Hond.print_info() #instantie zelf
Dier.print_info(Hond) # vanuit de klasse, geef een instantie mee"""
