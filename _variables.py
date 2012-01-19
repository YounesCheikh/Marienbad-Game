#!/usr/bin/python
# -*- coding: utf-8 -*-

"""                                         """
"""         *** _variables.py ***           """
"""                                         """

from turtle import *


"""
        *** declaration des variables ***
"""

#L'image de l'arierre plan du bienvenue
imagewelcome="images/welcom.gif"


#L'image de l'arierre plan
imagebg="images/bg.gif"
"""
les images:
"""
"""
#IMAGE ALLUMETTE Allumé
img_allumette1="images/allumette1.gif"
#IMAGE allumette eteinte
img_allumette2="images/allumette2.gif"
"""
#IMAGE ALLUMETTE Allumé
img_allumette1="images/carte1.gif"
#IMAGE allumette eteinte
img_allumette2="images/carte2.gif"

img_debut="images/debut.gif"
img_a_moi="images/a_moi.gif"

img_me="images/me.gif"
img_ordi="images/ordi.gif"


img_a_vous="images/a_vous.gif"
img_gagne="images/gagne.gif"
img_perdu="images/perdu.gif"
img_ok="images/ok.gif"
img_quit="images/quit.gif"
img_restart="images/restart.gif"
img_help="images/aide.gif"
img_logo="images/logo.gif"
register_shape(img_allumette1)
register_shape(img_allumette2)
register_shape(img_debut)
register_shape(img_a_moi)
register_shape(img_a_vous)
register_shape(img_gagne)
register_shape(img_perdu)
register_shape(img_ok)
register_shape(img_quit)
register_shape(img_restart)
register_shape(img_help)
register_shape(img_logo)
register_shape(img_me)
register_shape(img_ordi)


#les cordonnees initales
x_i=-260
y_i=-230

#Taille allumette
H_allumette=120
W_allumette=82

#colonne actuelle
col_act=None

min_move=False
#listes
#Liste etat allumettes pardefault
LEA_default=[[1,1,1,1,1,1,1],[1,1,1,1,1],[1,1,1],[1]]
#List des situations perdants
LSP=[[0,0,0,1],[0,1,1,1],[0,0,2,2],[0,0,3,3],[0,1,2,3],[1,1,2,2],[0,0,4,4],[1,1,3,3],[0,0,5,5],[0,1,4,5],[1,1,4,4],[0,2,4,6],[1,1,5,5],[0,2,5,7],[0,3,4,7],[1,2,4,7],[0,3,5,6],[1,2,5,6],[1,3,4,6],[1,3,5,7]]
#Liste Etat Allumette
LEA=[[1,1,1,1,1,1,1],[1,1,1,1,1],[1,1,1],[1]]
#Liste cordonnees Allumette dans l'ecran
LCA=[[],[],[],[]]
#LCA=[[(20,20)],[(40,20),(40,40)],[(60,20),(60,40),(60,60)],[(80,20),(80,40),(80,60),(80,80)],[(100,20),(100,40),(100,60),(100,80),(100,100)],[(120,20),(120,40),(120,60),(120,80),(120,100),(120,120)],[(140,20),(140,40),(140,60),(140,80),(140,100),(140,120),(140,140)]]
#autre variables
jouer=0  #Nombre du joueur acctuel
shape_act=0 #L'id du shape acctuel
out_of=False
first_welcome=True #pour eviter de placer les shapes a chaque fois on appel la fonction welcome
ordi_play=True #utilisé dans la fonction welcome()
