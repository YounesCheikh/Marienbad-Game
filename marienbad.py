#!/usr/bin/python

"""                                         """
"""         *** marienbad.py ***            """
"""                                         """

from turtle import *
setup(800,600) #Taille de la fenetre turtle et sa position sur l'ecran
#screensize(800,600)

from _variables import *
from _fonctions import *

def main():
    up()
    ht()
    speed(0)
    title("PROJET Python: Jeu Marienbad") #Le titre de la fenetre
    home()
    onscreenclick(gestion_click) 
    welcome()

main()
mainloop()
