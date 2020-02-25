#!/usr/bin/env python
# coding: utf-8

# # PMI-GROUPE 7
# ## Loi de Beer-Lambert appliquée à la traversée d'un champ de mines 

# ### Notations

# On note:
# -  L : Largeur du champ (correspond à l'axe des abscisses).
# -  l : Longueur du champ (correspond à l'axe des ordonnées). 
# -  M : Nombre de mine dans le champ.
# -  N0 : Nombre de lapins initial sur "la ligne de départ".
# -  ev_pop : Liste dont le i-ème élément corréspond au nombre de lapin ayant survécu jusqu'à la distance i.
# -  Xm,Ym : Listes contenant respectivement l'abscisse et l'ordonnée des bombes.
# -  Rb : Rayon de la bombe.
# -  Re : Rayon de l'explosion.

# **Hypothèses :** 
# 
# Nous considérerons 2 types de mines dans les programmes: 
# -  des mines carrées de longueur 10cm 
# -  des mines rondes de diamètre 10cm
# 
# La position en abscisse Xm[i] et en ordonnée Ym[i] d'une mine correspondra au centre celle-ci. De plus, la mine explosera dès lors qu'un lapin s'approchera à plus ou moins 5cm du centre de la mine. On considera également qu'aucune mines ne sera placé sur la ligne de départ ni sur la ligne d'arrivée et que plusieurs lapins peuvent être superposés (c'est à dire avoir la même position initiale et donc la même trajectoire).

# **Remarque** : En ce qui concerne l'affichage des courbes, nous avons utilisé les ressources bibliographiques [5] et [6]

# **Initialisation** 

# Le choix des valeurs de M et de N0 peuvent être modifié selon ce que nous voulons observer.

# In[1]:


L=1000
l=1000
M=100
N0=100
Re=10
Rb=5


# ## Programmation 1

# In[2]:


#importation des bibliothèques nécéssaire
import random
import math
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import time


# -  La fonction **position_mines** définit la position des mines dans le champ en générant des entiers aléatoires inférieurs ou égaux aux dimensions du champ. Elle renvoie la liste des abscisses et la liste des ordonnées des mines tirées au sort de manière aléatoire en suivant une loi uniforme.
# 
# -  La fonction **position_init** définit la position des lapins sur la ligne de départ : leur abscisse est tirée aléatoirement suivant une loi uniforme. 

# In[3]:


def position_mines(M,L,l):
    Xm=[]
    Ym=[]
    for i in range(M):
        Xm.append(random.randint(0,L))
        Ym.append(random.randint(1,l-1))
    return(Xm,Ym)

def position_init(N0,L):
    position=[]
    for i in range (N0):
        position.append(random.randint(0,L))
    return(position)


# **Affichage du champ**

# In[4]:


def programmation1(Xm,Ym,abs_lap,ord_lap):
    plt.scatter(Xm,Ym,s=10,c='orange',marker="x")
    plt.xlabel("Largeur du champ en cm")
    plt.ylabel("Longueur du champ en cm")
    plt.scatter(abs_lap,ord_lap,s=10,c='saddlebrown', marker="o")
    plt.title("Répartition alétoire des mines dans un champ et position initiale des lapins")


# In[5]:


Xm,Ym=position_mines(M,L,l)
abs_lap=position_init(N0,L)
ord_lap=[0]*N0

programmation1(Xm,Ym,abs_lap,ord_lap)


# ## Programmation 2

# La fonction **un_trajet_carre** retourne la distance parcourue par un lapin jusqu'à ce qu'il rencontre une mine (ou non). Cette fonction prend entre autre **x0** comme argument qui représente la position en abscisse d'un lapin. Dans cette fonction, on considérera que la mine est carrée.

# In[6]:


def un_trajet_carre(x0,l,Xm,Ym):
    explosion=l # Explosion est la variable qui stocke le distance à laquelle le lapin meurt : elle est initialisée à l puis décroit si une mine est placée sur le chemin du lapin.
    for i in range (len(Xm)):  # On fait une boucle sur chaque centimètre de la largeur du terrain. 
        if Xm[i]-5<=x0 and Xm[i]+5>=x0: # On teste sur l'abscisse de la mine...
            if Ym[i]<explosion : # ...puis sur son ordonnée.
                explosion = Ym[i] # S'il y a une bombe sur le chemin, explosion prend la valeur de l'ordonnée de la bombe.
    if explosion != l:
        if explosion-5<0: # On prend en compte la largeur de la mine.
            return(1)
        else :
            return(explosion-5)
    else :
        return(l)


# La fonction **un_trajet_rond** retourne la distance parcourue par un lapin jusqu'à ce qu'il rencontre une mine (ou non) et les coordonnées du centre de la bombe ayant fait exploser le lapin. Cette fonction prend également **x0** en argument. Dans cette fontion, on considérera que la mine est ronde.

# In[7]:


def un_trajet_rond(x0,l,Xm,Ym,Rb):
    rep=0 
    bombe_explosee=[0,0] #bombe_explosee est la liste de 2 variables qui correspondent à l'abscisse et à l'ordonnée de la bombe qui explosera 
    for d in range (l): #on fait une boucle sur chaque centimètre de la longueur du terrain
        for i in range (len(Xm)):  #on fait une boucle sur chaque centimètre de la largeur du terrain
            if (x0-Xm[i])**2+(d-Ym[i])**2<=Rb**2:  #on teste si la position du lapin est dans le rayon de la bombe 
                rep=1
                bombe_explosee[0]=Xm[i]
                bombe_explosee[0]=Ym[i]
        if rep==1:
            return(d,bombe_explosee)
    return(d,bombe_explosee)


# Les fonctions **traversee_carre** et **traversee_rond** renvoient deux listes: 
# - une liste N dans laquelle, à chaque indice **`i`**, on trouve le nombre de lapins vivants à la distance **`i`** de la ligne de départ
# - une liste d ou chaque élément **`i`** correspond à la distance **`i`** parcourue
# 
# Elles parcourent l’ensemble des lapins et remplient un tableau « morts » dont l’élément à la i-éme position contient le nombre de lapins morts à la distance y=i. Une fois ce tableau rempli, on crée un autre tableau **N** de la longueur « l » du terrain contenant pour chaque centimètre le nombre de lapins vivants.
# 

# In[8]:


#Cas pour des mines carrées: 

def traversee_carre(Xm,Ym,l,L,N0,position):
    N=[N0]
    d=[0]
    morts=[0]*(l+1) # morts[i]=nombre de lapins qui meurent en y=i.
    for i in range (len(position)):# On parcourt la liste des lapins.
        y= un_trajet_carre(position[i],l,Xm,Ym) # On calcule la distance à laquelle le i-ème lapin meurt ainsi que les coordonnées de la bombe qui l'a fait exploser.
        morts[y]=morts[y]+1 # On rajoute 1 à la l'élément de la liste morts comptant le nombre de lapins morts en y.
    for i in range (l):
        N.append(N[-1]-morts[i])
        d.append(i+1)
    return(N,d)


# In[9]:


#Cas pour des mines rondes:

def traversee_rond(Xm,Ym,l,L,N0,Re,Rb,position):
    N=[N0]
    d=[0]
    morts=[0]*(l+1) # morts[i]=nombre de lapins qui meurent en y=i
    for i in range (len(position)):
        y,b= un_trajet_rond(position[i],l,Xm,Ym,Rb)
        morts[y]=morts[y]+1
        for i in range (len(N)):
            if (b[0]-Re)>N[i]and N[i]>(b[0]+Re):#on teste sur tout les lapins s'ils sont dans le rayon d'explosion de la bombe qui vient d'exploser.
                y2,b2=un_trajet_rond(position[i],l,Xm,Ym,Rb)
                if y2>=y:#on teste si le lapin sélectionné est mort avant, s'il ne l'est pas on le tue : on rajoute un à l'élément de la liste morts qui contient le nombre de morts en y
                    morts[y]=morts[y]+1
    for i in range (l):
        N.append(N[-1]-morts[i])
        d.append(i+1)
    return(N,d)


# **Affichage**

# In[10]:


def programmation2(L,l,N0,M,Re,Rb):
    Xm,Ym= position_mines(M,L,l)
    position=position_init(N0,L)
    ev_pop_carre,ev_dist_carre=traversee_carre(Xm,Ym,l,L,N0,position)    
    plt.scatter(ev_dist_carre,ev_pop_carre,s=0.5,marker='*')
    plt.xlabel("Distance en cm")
    plt.ylabel("Nombre de lapins vivants")
    plt.title("Evolution du nombre de lapins en fonction de la distance (avec des mines carrées)")
    plt.show()
    ev_pop_rond,ev_dist_rond=traversee_rond(Xm,Ym,l,L,N0,Re,Rb,position)
    plt.scatter(ev_dist_rond,ev_pop_rond,s=0.5,marker='*')
    plt.xlabel("Distance en cm")
    plt.ylabel("Nombre de lapins vivants")
    plt.title("Evolution du nombre de lapins en fonction de la distance (avec des mines rondes)")
    plt.show()
    return()


# In[11]:


programmation2(L,l,N0,M,Re,Rb)


# ## Programmation 3

# In[12]:


def reg_lin(X,Y):
    sumxy=0
    sumx=0
    sumy=0
    sumx2=0
    for i in range (len(X)):
        sumxy=sumxy+X[i]*Y[i]
        sumx=sumx+X[i]
        sumy=sumy+Y[i]
        sumx2=sumx2+X[i]**2
    a=(len(X)*sumxy-sumx*sumy)/(len(X)*sumx2-sumx**2)
    b=(sumy-a*sumx)/len(X)
    regression=[]
    for i in range (len(Y)):
        regression.append(a*X[i]+b)
    return(regression,a,b)

def affichage_regression(X,Y):
    regression,a,b=reg_lin(X,Y)
    plt.plot(X,Y,"-",X,regression,'-.')
    plt.xlabel("distance en cm")
    plt.ylabel("ln(N[i]/N0)")
    plt.axis()
    plt.title("Vérification concordance loi de Beer Lambert")
    plt.grid()
    plt.show()
    print("coefficient directeur = ",a)
    print("ordonnée à l'origine = ",b)
    return()


# In[13]:


def programmation3(L,l,N0,M,Re,Rb):
    Xm,Ym= position_mines(M,L,l)
    position=position_init(N0,L)
    ev_pop_carre,ev_dist_carre=traversee_carre(Xm,Ym,l,L,N0,position)
    ev_pop_rond,ev_dist_rond=traversee_rond(Xm,Ym,l,L,N0,Re,Rb,position)
    tmp_carre=[]
    tmp_rond=[]
    i=0
    j=0
    while i<len(ev_pop_carre) and ev_pop_carre[i]!=0:
        tmp_carre.append(math.log(ev_pop_carre[i]/N0))
        i=i+1
    while j<len(ev_pop_rond) and ev_pop_rond[j]!=0:
        tmp_rond.append(math.log(ev_pop_rond[j]/N0))
        j=j+1
    plt.scatter(ev_dist_carre,ev_pop_carre,s=0.5,marker='*')
    plt.xlabel("distance en cm")
    plt.ylabel("Nombre de lapins vivants")
    plt.title("Evolution du nombre de lapins en fonction de la distance (mines carrées)")
    plt.show()
    affichage_regression(ev_dist_carre[:len(tmp_carre)],tmp_carre)
    plt.scatter(ev_dist_rond,ev_pop_rond,s=0.5,marker='*')
    plt.xlabel("distance en cm")
    plt.ylabel("Nombre de lapins vivants")
    plt.title("Evolution du nombre de lapins en fonction de la distance (mines rondes)")
    plt.show()
    affichage_regression(ev_dist_rond[:len(tmp_rond)],tmp_rond)
    return()
    


# In[14]:


programmation3(L,l,N0,M,Re,Rb)


# ## Etude de la convergence

# Lors des programmes qui suivent, nous avons choisi d'utiliser le cas où **les mines sont carrées** par souci d'efficacité.

# In[15]:


#Fonctions utiles pour étudier la convergence.

def moyenne(liste):
    sum=0
    for i in range(len(liste)):
        sum=sum+liste[i]
    return(sum/len(liste))

def ecart_type(liste,moyenne):
    sum=0
    for i in range(len(liste)):
        sum=sum+(liste[i]-moyenne)**2
    return(math.sqrt(sum/len(liste)))


# La fonction **etude_conv** permet de créer un fichier texte. Dans ce programme, on recupère le nombre de lapins final obtenu pour plusieurs simulations effectuées avec un nombre de mines et un nombre initial de lapins donné. On calcule ensuite l'écart-type de la liste obtenue.

# In[16]:


def etude_conv(L,l):
    Convergence=open("etu_conv.txt","w") # ouverture d’un fichier texte
    Convergence.write("L=")
    Convergence.write(str(L))
    Convergence.write("  l=")
    Convergence.write(str(l))
    for k in range (10): # simulation 10 fois
        Nf=[]
        N0=random.randint(80,1000)
        M=random.randint(50,300)
        Xm,Ym=position_mines(M,L,l)
#on choisit un nombre d’animaux initial et un nombre de mines aléatoire
        Convergence.write("\nN0=")
        Convergence.write(str(N0))
        Convergence.write("   M=")
        Convergence.write(str(M))
        Convergence.write("   N={ ")
        for i in range (15):# 15 simulations
            position=position_init(N0,L)
            N,d=traversee_carre(Xm,Ym,l,L,N0,position)
            Convergence.write(str(N[l])) # on écrit le nombre final d’animaux
            Nf.append(N[l])
            Convergence.write("; ")
        Convergence.write("}")
        moy=moyenne(Nf)
        e_type=ecart_type(Nf,moy)
        Convergence.write("     Ecart type=")
        Convergence.write(str(e_type))
    Convergence.close()


# In[17]:


etude_conv(L,l)


# On veut maintenant regarder l'influence des paramètres initiaux ( du nombre de lapins initial et du nombre de mines) sur l'évolution de l'ecart-type. On fait donc varier un seul des paramètres à la fois, nous utilisons donc 2 fonctions: 
# 
# -  **convergence_Mfixe(L,l,M)** : dans cette fonction, nous avons tracé l'évolution de l'écart type du nombre de lapins ayant survécus sur toute la longueur du champ en fonction du nombre de lapins initial (pour un nombre de mines fixe). Pour un N0 compris entre 80 et 2000, le programme fait 20 simulations différentes ce qui permettra de calculer une moyenne des nombres de lapin ayant survécus pour ensuite calculer l'écart type associé à ce N0. L'écart type sera calculer pour plusieurs valeurs de N0.
# 
# -  **convergence_N0fixe(L,l,N0)**  : permet de tracer l'évolution de l'écart type du nombre de lapins ayant survécus sur toute la longueur du champ en fonction du nombre de mines placées dans le champ (pour un nombre de lapins initial fixe). Pour un nombre de mines compris entre 50 et 300 le programme fait 20 simulations différentes ce qui permettra de calculer une moyenne des nombres de lapins ayant survécus pour ensuite calculer l'écart type associé à ce nombre de mines. L'écart type sera calculé pour plusieurs valeurs du nombre de mines.
# 

# In[18]:


def convergence_Mfixe(L,l,M):
    x=[]
    y=[]
    for N0 in range (80,2000,100):  # Pour un nombre différent de lapins initial
        Xm,Ym=position_mines(M,L,l)
        liste=[]
        x.append(N0)
        for i in range (20): #on fait 20 simulations 
            position=position_init(N0,L)
            N,d=traversee_carre(Xm,Ym,l,L,N0,position)
            liste.append(N[l])
        m=moyenne(liste)  #calcule la moyenne de la liste comprenant le nombre de lapins ayant survévu (lors des 20 simulations)
        e=ecart_type(liste,m)  #calcule l'écart type pour un N0
        y.append(e)
    plt.plot(x,y,'o')
    plt.xlabel("Nombre de lapins initial")
    plt.ylabel("Ecart type")
    plt.title("Ecart type en fonction du nombre de lapins initial")
    return()
    
def convergence_N0fixe(L,l,N0):
    x=[]
    y=[]
    for M in range (50,300,10):  # pour un nombre différent de mines dans le champ 
        Xm,Ym=position_mines(M,L,l)
        liste=[]
        x.append(M)
        for i in range (20): # on fait 20 simulations 
            position=position_init(N0,L)
            N,d=traversee_carre(Xm,Ym,l,L,N0,position)
            liste.append(N[l])
        m=moyenne(liste) #calcule la moyenne de la liste comprenant le nombre de lapins ayant survévu (lors des 20 simulations)
        e=ecart_type(liste,m) #calcule l'écart type pour un nombre de mines précis
        y.append(e)
    plt.plot(x,y,'o')
    plt.xlabel("Nombre de mines")
    plt.ylabel("Ecart type")
    plt.title("Ecart type en fonction du nombre de mines")
    return()


# In[19]:


convergence_Mfixe(L,l,M)


# In[20]:


convergence_N0fixe(L,l,N0)


# ## Analyse

# Pour vérifier la concordance avec la loi de Beer Lambert nous avons décidé d'étudier l'évolution du coefficient de corrélation en fonction du nombre de lapins initial. Nous considérerons qu'il y a concordance avec la Loi de Beer Lambert si ce coefficient est proche de 1 (ou -1).

# In[21]:


# Expression du coefficient de corrélation en fonction du nombre de lapins initial.
def correlation_lapin(M,L,l):
    X1=[]
    Y1=[]
    for N0 in range(1,100,2):  #on teste de 1 à 100 lapins de 2 en 2
        X1.append(N0)
        Y=[]
        for i in range(20):  #moyenne sur 10 valeurs
            Xm,Ym=position_mines(M,L,l)
            position=position_init(N0,L)
            (N,d)=traversee_carre(Xm,Ym,l,L,N0,position)
            (pente,ordo,coef,pvalue,error)=stats.linregress(d,N)   #cf bibliographie: [4]
            Y.append(coef)
        moy=0   
        for j in range(len(Y)):
            moy+=-(Y[j]/20)
            
        Y1.append(moy)
            
    return(X1,Y1)

def affichage_correlation(M,L,l):
    (X,Y)=correlation_lapin(M,L,l)
    plt.scatter(X,Y,label='M=1000',s=3)
    plt.ylabel("coefficient de corrélation")
    plt.xlabel("nombre de lapins initial")
    plt.title("Coefficient de corrélation en fonction du nombre de lapins initial")
    plt.grid()
    plt.legend()
    plt.plot([0,100],[0.95,0.95],color='orange',label=0.95)
    plt.show()
    return ()


# In[22]:


affichage_correlation(M,L,l)


# In[23]:


S=[10,70,100,600,1200]
for i in S:
    (X,Y)=correlation_lapin(i,L,l)
    plt.scatter(X,Y,label=i,s=3)
plt.plot([0,100],[0.95,0.95],label=0.95)

plt.ylabel("coefficient de corrélation")
plt.xlabel("nombre de lapins initial")
plt.title("Coefficient de corrélation en fonction du nombre de lapins initial")

plt.grid()
plt.legend()
plt.show()


# La fonction **seuil** permet de calculer pour quelle valeur de lapins initial il est certain que le nombre de lapins survivants soit nul. Nous afficherons ensuite grâce à la fonction **affichage_seuil** la regression linéaire de la courbe représentant le nombre de lapins survivants en fonction du nombre initial de lapins.

# In[24]:


def seuil(l,L,M,Nmax):
    Ym,Xm=position_mines(M,L,l)
    Nfinaux=[]
    x=[]
    for N0 in range (Nmax):
        tmp=0
        for i in range (20): #On fait 20 simulations avec  le même nombre de mines
            position=position_init(N0,L)
            N,d=traversee_carre(Xm,Ym,l,L,N0,position)
            tmp=tmp+N[-1]
        Nfinaux.append(tmp/20) # tmp/20 est la moyenne du nombre de lapins survivants pour un nombre donné de lapins initial
        x.append(N0)
    return(Nfinaux,x)


def affichage_seuil(l,L,M,Nmax):
    Nfinaux,x=seuil(l,L,M,Nmax)
    regression,a,b=reg_lin(x,Nfinaux)    
    plt.plot(x,Nfinaux,".")
    plt.plot(x,regression)
    plt.plot([0,Nmax],[1.0,1.0])
    plt.title("Nombre de lapins survivants en fonction du nombre de lapins initial")
    plt.xlabel('Nombre de lapins initial')
    plt.ylabel('Nombre de lapins survivants')
    plt.show()
    return ()   


# In[25]:


affichage_seuil(l,L,400,200)


# ### Animation

# Tentative d'animation de la trajectoire des lapins dans un champ. 
# Prends beaucoup de temps pour s'exécuter donc nous l'utilisons seulement sur un champ de dimension 1000 x 100 (avec L=1000 et l=100).  

# In[26]:


import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np

l_ani=100
Xm,Ym=position_mines(M,L,l_ani)
position=position_init(N0,L)
N,d=traversee_carre(Xm,Ym,l_ani,L,N0,position)   


def trajectoire(position,l,X,Y):   # cette fonction permet de renvoyer une liste de la trajectoire d'un lapin 
    traj_laps=[]
    for i in range (len(position)):
        y= un_trajet_carre(position[i],l,X,Y)
        traj_laps.append(y)    
    return traj_laps

stop=trajectoire(position,l_ani,Xm,Ym)

fig, ax = plt.subplots()
ax.axis([0,L,0,l_ani])
plt.scatter(Xm,Ym,s=5,c='k', marker="s")  # Affiche la position des mines (carrées) sur le graphique

def animate(i):  #Permet de tracer la trajetoire de chaque lapin, il prend en argument i qui va prendre N0 valeurs et donc tracer la position pour les N0 lapins. 
    for k in range (stop[i]):
        plt.scatter(position[i],k,s=1,c='chocolate', marker="o")


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=len(stop))  # cf bibliographie: [6]

from IPython.display import HTML
HTML(ani.to_jshtml())

