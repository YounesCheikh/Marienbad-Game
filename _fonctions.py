#!/usr/bin/python
# -*- coding: utf-8 -*-

"""                                         """
"""          *** _fonctions.py ***          """
"""                                         """

from turtle import *
from random import randint
from copy import deepcopy
from _variables import *

up()
"""
Fonctions
"""

#Fonction calcul le nombre d'allumettes restes
#Dans la liste LEA

def _nb_allumettes():
    global LEA
    s=0
    for i in LEA:
        s=s+sum(i)
    return s
#TEST:
#print _nb_allumettes()

#######################################################

#fonction dessine l'alluemette
def dessine_allumette(x,y,b): #(cordonnees x, y, et booleen allumé ou eteinte)
    goto(x,y)
    if (b==True):
        shape(img_allumette1)
        stamp()
    else:
        shape(img_allumette2)
        stamp()
#TEST:
#dessine_allumette(100,100,True)

#######################################################

#Fonction verif si le jouer a cliquer sur une allumette ou pas

def point_in_liste(x,y):
    global LCA
    for i in range(0,len(LCA)):
        for j in range(0,len(LCA[i])):
            (a,b)=LCA[i][j]
            if (x>=a-W_allumette/2 and x<=a+W_allumette/2 and y>=b-H_allumette/2 and y<=b+H_allumette/2):
                return(True)

#######################################################

#Fonction renvoi les indices d'une allumettes dans la liste LEA

def point_of_cordonnees(x,y):
    global LCA
    for i in range(0,len(LCA)):
        for j in range(0,len(LCA[i])):
            (a,b)=LCA[i][j]
            if (x>=a-W_allumette/2 and x<=a+W_allumette/2 and y>=b-H_allumette/2 and y<=b+H_allumette/2):
                return(i,j)


########################################################

#Fonction place les allumettes
def placer_allumettes():
    global LEA,LCA #Liste des etats et liste des cordonnees x,y
    for i in range(len(LEA)-1,-1,-1):
        for j in range(len(LEA[i])-1,-1,-1):
            x=x_i+j*90
            y=y_i+i*130
            LCA[i]+=[(x,y)]
            if(LEA[i][j]==1):
                dessine_allumette(x,y,True)
            else:
                dessine_allumette(x,y,False)

#########################################################

#Fonction change le joueur
def changer_jouer():
    global jouer 
    if (jouer==1): 
        jouer=2
    else:
        jouer=1

########################################################

#fonction dessine l'etat de 2eme jouer (l'ordinateur
def image_jouer(etat):
    global shape_act
    chaine=""
    color("#2D2D2D")
    if etat==img_perdu:
        chaine="Vous avez Gagné!"
    elif etat==img_gagne:
        chaine="J'ai Gagné!"
    goto(-120,90)
    write(chaine, move=False, align="left", font=("Arial", 20, "normal"))
    color()
    clearstamp(shape_act)
    goto(160,100)
    shape(etat)
    shape_act=stamp()

##########################################################

#fonction Affiche les resultats a la fin de la partie
def resultat(b):
    global shape_act
    if (b==2):
        image_jouer(img_perdu)
        stamp()
    else:
        image_jouer(img_gagne)
        stamp()

###########################################################

#Fonction places le menu et les buttons
def placer_menu_graphics():
    global shape_act
    goto(-130,200)
    color("#800000")
    write("Jeu Marienbad", move=True, align="left", font=("Arial", 28, "bold"))
    color()
    goto(300,0)
    shape(img_quit)
    stamp()
    goto(225,0)
    shape(img_help)
    stamp()
    goto(150,0)
    shape(img_restart)
    stamp()
    goto(75,0)
    shape(img_ok)
    stamp()

############################################################

#Acctualise la fenetre 
def start_new_graphics():
    goto(330,210)
    shape(img_logo)
    stamp()
    placer_menu_graphics()
    image_jouer(img_debut)

############################################################

#Quit Aide
def _QUIT_AIDE(x,y):
    global out_of
    if x>=175 and x<=225 and y>=-225 and y<=-175:
        clear()
        start_new_graphics()
        placer_allumettes()
        onscreenclick(gestion_click)
    else:
        onscreenclick(None)
        onscreenclick(_QUIT_AIDE)

############################################################

#L'affichage d'aide
#on import l'aide d'un fichier text 'help'
    
def afficher_aide():
    fic = open('help','r')  #mode lecture
    ligne = fic.readlines()
    fic.close()
    nb_ligne=100
    goto(-130,170)
    color("red")
    write("REGLES DU JEU:", move=True, align="left", font=("Arial", 20, "bold"))
    for i in ligne:
        goto(-260,nb_ligne)
        color("black")
        write(i, move=False, align="left", font=("Arial", 12, "normal"))
        nb_ligne=nb_ligne-30
    goto(200,-200)
    shape(img_quit)
    stamp()
    onscreenclick(_QUIT_AIDE)

##############################################################

#Fonction renvoi le nombre de la premiere allumette allumé
def first_actif(col):
    for i in range(len(col)-1,-1,-1):
        if col[i]==1:
            return i


##############################################################

#Fonction convert un nombre decimal en binaire
def d2b(a):
    L=[]
    n=""
    while a/2!=0:
        L+=[a%2]
        a=a/2
    L+=[a%2]
    i=len(L)
    while i>0:
        n=n+str(L[i-1])
        i=i-1
    if len(n)==1:
        n="00"+n
    elif len(n)==2:
        n="0"+n
    return (n)

################################################################

def _situation_actuelle():
    global LEA
    L=[0,0,0,0]
    for i in range(len(LEA)):
        L[i]=sum(LEA[i])
    return L

###############################################################

#Fonction calcul la somme du nombres dans chaque collonnes apres
#la convertion en binaire
def sum_cols():
    global LEA
    __LIST__=[]
    for i_tmp in LEA:
        __LIST__+=[d2b(sum(i_tmp))]
        
    __L_SUM__=[0,0,0]
    for i in range(len(__L_SUM__)):
        for B in __LIST__ :
            __L_SUM__[i]=__L_SUM__[i]+int(B[i])
    return __L_SUM__
            
################################################################

#Fonction booleene renvoi vrai si la situation suivante est gagnante
def situation_gagnante(S):
    global LSP
    L=sorted(_situation_actuelle())
    for i in LSP:
        if L==sorted(i):
            return True
    return False
    



#################################################################

def _joue_hasard():
    global LEA
    for col in range(len(LEA)):
        s=sum(LEA[col])
        if s>=1:
            nb=randint(1,s)
            #print "joue:",col,nb
            return(col,nb)


#################################################################

#Fonction cherche la premiere situation gagnante et renvoi le bon
# nombre colonne est nombre ligne qu'il faut jouer

def situations_try():
    global LEA
    LEA_TMP=deepcopy(LEA)
    _TROUVE=False
    for i in range(len(LEA)):
        if sum(LEA[i])!=0:
            f_actif=first_actif(LEA[i])
            now_actif=f_actif
            for j in range(len(LEA[i])-1,-1,-1):
                if j==first_actif(LEA[i]):
                    LEA[i][j]=0
                    if situation_gagnante(_situation_actuelle()):
                        now_actif=j
                        _TROUVE=True     
            LEA=deepcopy(LEA_TMP)
            if _TROUVE==True:
                nb=abs(now_actif-f_actif)+1
                if nb==_nb_allumettes():
                    nb=nb-1
                return(i,nb)
    LEA=deepcopy(LEA_TMP)
    #print "ordi:",_situation_actuelle()
    #print "reste:",_nb_allumettes()
    #print "sit non trouve.. passe au _joue_hasard()"
    (col,nb)=_joue_hasard()
    return(col,nb)

##################################################################

#Fonction qui enleve les allumettes si le joueur acctuel est l'ordinateur

def play_now(col,n):
    global LEA,LCA
    while n>0:
        j=first_actif(LEA[col])
        (a,b)=LCA[col][j]
        LEA[col][j]=0
        dessine_allumette(a,b,False)
        n=n-1
###################################################################

#la fonction qui gere le 2eme jouer (L'ordi)
def player2():
    global LEA,jouer
    if(_nb_allumettes()>1):
        image_jouer(img_a_moi)
        L_tmp=_situation_actuelle()
        (col,nb)=situations_try()
        play_now(col,nb)
        #print "ordi:",_situation_actuelle()
        #print "reste:",_nb_allumettes()
        if (_nb_allumettes()==1):
                resultat(1)
        else:
            changer_jouer()
    if(_nb_allumettes()>1 and jouer==1):
        image_jouer(img_a_vous)


####################################################################

#Fonction gere les click
def gestion_click(x,y):
    up()
    global jouer,shape_act,col_act,LEA,LEA_default,min_move,out_of
    if(jouer==0):
        jouer=1
    if(x>=275 and x<=325 and y>=-25 and y<=25):
        bye()
    elif(x>=200 and x<=250 and y>=-25 and y<=25):
        clear()
        out_of=True
        afficher_aide()
    elif(x>=125 and x<=175 and y>=-25 and y<=25):
        clear()
        LEA=deepcopy(LEA_default)
        jouer=0
        col_act=None
        up()
        ht()
        speed(0)
        goto(175,-80)
        shape(img_me)
        stamp()
        goto(225,-80)
        shape(img_ordi)
        stamp()
        goto(0,-45)
        color("#800000")
        write("Qui joue le premier ?", move=False, align="left", font=("Arial", 16, "bold"))
        welcome()
    elif(point_in_liste(x,y)):
        (a,b)=point_of_cordonnees(x,y)
        (i,j)=LCA[a][b]
        if(col_act==None):
            col_act=a
        if(a==col_act and b==first_actif(LEA[a]) and _nb_allumettes()!=1 ):
            dessine_allumette(i,j,False)
            LEA[a][b]=0
            min_move=True
    elif(x>=50 and x<=100 and y>=-25 and y<=25 and min_move==True):
        if (_nb_allumettes()==1):
            resultat(2)
        else:
            changer_jouer()
            min_move=False
            col_act=None
            player2()

############################################################

#Quit Aide
def _QUIT_WELCOME(x,y):
    global ordi_play
    if x>=150 and x<=200 and y>=-115 and y<=-65:
        clear()
        bgpic(imagebg) #L'image de l'arriere plan
        start_new_graphics()
        placer_allumettes()
        ordi_play=False
        onscreenclick(gestion_click)
    elif x>200 and x<=250 and y>=-115 and y<=-65:
        clear()
        bgpic(imagebg) #L'image de l'arriere plan
        start_new_graphics()
        placer_allumettes()
        ordi_play=True
        player2()
        onscreenclick(gestion_click)
    else:
        onscreenclick(None)
        onscreenclick(_QUIT_WELCOME)

        
############################################################
def welcome():
    global first_welcome
    if first_welcome==True:
        bgpic(imagewelcome) #L'image de l'arriere plan
        up()
        ht()
        speed(0)
        goto(175,150)
        shape(img_debut)
        stamp()
        goto(175,-80)
        shape(img_me)
        stamp()
        goto(225,-80)
        shape(img_ordi)
        stamp()
        goto(0,-45)
        color("#800000")
        write("Qui joue le premier ?", move=False, align="left", font=("Arial", 16, "bold"))
        first_welcome=not first_welcome
    onscreenclick(_QUIT_WELCOME)

