##Exercice 1 - 1)

def inverse_ch(chaine):
    k=len(chaine)-1      #k est le nombre de lettres dans la chaine de caractère 
    chaine1=''           #initialisation de la chaine 1
    while k>-1:          # tant que l'on a pas parcouru toutes les lettres de la liste 
        chaine1=chaine1+chaine[k]   #on attribue à chaine1 la kème lettre, puis la k-1 ème lettre...
        k=k-1                
    return chaine1

chaine=input('mot?')
print (inverse_ch(chaine))

##Exercice 1 - 2)

def palindrome(chaine):
    k=len(chaine)                      #k est le nombre de lettres dans la chaine de caractère 
    for i in range (k):                #pour le nombre de lettre dans le mot 
        if chaine[i]!=chaine[i-1]:     #on compare la 1ère lettre du mot avec la dernière, puis la 2eme avec l'avant dernière... et s'il y a une différence 
            return False               #alors ce n'est pas un palindrome 
        else:                          #s'il n'y a pas de différence
            return True                # le mot est un palinrome
    

chaine=input('mot?')
print (palindrome(chaine))

##
#Ce n'est pas judicieux d'utliser la fonction inverse car cela voudrait dire que l'on devrait comparer deux chaines de caractères ce qui n'est pas facile car on ne peut pas faire si chaine[i]=chaine[k] par exemple

##Exercice 1 - 3)

def annagramme(chaine1,chaine2):
    if len(chaine1)!=len(chaine2):    #si ils n'ont pas le même nombre de lettres 
        return False                 
    else:                             #si les deux mots ont le même nombre de lettres
        for i in range (len(chaine1)):  #pour toutes les lettres du mot1
            for j in range (len(chaine1)):  #pour toutes les lettres du mot2
                if chaine1[i]!=chaine2[j]:   #si en comparant tour à tour une lettre du mot1 avec toutes les lettres du mot2 et qu'intervient une différence
                    return False     #alors ce n'est pas un annagramme
                else:  
                    return True 


chaine1,chaine2=input('mot1?'),input('mot2?')
print (annagramme(chaine1,chaine2))
##
#ce programme marche juste pour certains mots et je n'arrive pas à faire un programme qui fonctionne 

##Exercice 2 - 1)

def crypter(n,mot):
    alph='abcdefghijklmnopqrstuvwxyz'
    crypt=''               #initialisation de la chaine de caractère qui contiendra le mot codé 
    for lettres in mot:                      #Pour les lettres dans le mot
        if lettres in alph:                  #si la lettre est dans l'alphabet 
            for i in range (26):    
                if lettres==alph[i]:         #on cherche l'indice de la lettre dans l'alphabet 
                    crypt=crypt+alph[(i+n)%26]    #on ajoute au code la lettre avec le décalage demandé 
    return crypt


##
#Je n'ai pas réussi à faire le programme qui laisse les caractères qui ne sont pas compris dans l'alphabet minuscule.

##Exercice 2 - 2)

def decrypter(n,code):                                 #Même principe que le code précédent sauf à la ligne 74
    alph='abcdefghijklmnopqrstuvwxyz'
    crypt=''               
    for lettres in code:                      
        if lettres in alph:                  
            for i in range (26):    
                if lettres==alph[i]:         
                    crypt=crypt+alph[(i-n)%26]      #cette fois on fait i-n pour décoder la lettre
    return crypt

print(decrypter(n,code))

##Exercice 2 - 3)

def decod_hum(code):
    alph='abcdefghijklmnopqrstuvwxyz'
    crypt=''     #initialisation de la chaine de caractère qui contiendra le mot codé 
    n=1                                #initialisation du décalage n
    for j in range (26):               #Pour tester les 26 décalages 
        for lettres in code:           
            if lettres in alph:         
                for i in range (26):    
                    if lettres==alph[i]:        
                        crypt=crypt+alph[(i-n)%26]   
        crypt=crypt+';'     #quand le message est décodé on met un point virgule à la fin pour faire la distinction
        n=n+1                 #n prend la valeur n+1 pour tester le décalage suivant 
    return crypt
                
print (decod_hum('nhalhb'))

##
#La faiblesse de ce type de code est qu'il y a un nombre limité de codage possible car on peut faire un décalage de 26 lettres au maximum. Ainsi pour qu'un humain puisse décoder le message il suffit d'essayer de décoder le code avec tous les décalages possibles et de voir quand le code à un sens

##Exercice 2 - 4)

mes=input("Ce programme permet de coder en César, et de décoder un message crypté en code César. Afin de pouvoir utliser la fonction qui vous intéresse, veuillez suivre les règles suivantes: -si vous voulez crypter un message, veuillez rentrer la valeur n de votre décalage ainsi que le mot à crypter (ne pas remplir l'autre information demandé) . \  -si vous voulez décoder un message et que vous connaisez la valeur du décalage, rentrer la valeur de n ainsi que le code que vous voulez décoder et ne pas remplir la variable qui ne vous intéresse pas. \ -Enfin si vous voulez décrypter un message et que vous n'avez pas la valeur du décalage rentrer 0 pour la valeur de n et rentrer le code à décoder. ")
n=int(input('décalage?'))
mot=input('message à coder?')
code=input('message à décoder?')
if n!=0:                           #si le décalage est connu 
    if code=='':                   #si le code est une chaine de caractère vide 
        print (crypter(n,mot))         #on utilise la focntion crypter le message
    else:                          #si le code n'est pas une chaîne de caractère vide
        print (decrypter(n,code))     #on utlise la fonction decrypter 
else:                              #si le décalage n'est pas connu 
    print (decod_hum(code))
##Exercice 3 - 1)
import numpy as np

x=[]
x=np.linspace(-3,3,100)
print (x)
    
##Exercice 3 - 2)

from math import exp 
from math import sin

def f(x,y):               
    return exp(x+y**2)*sin(x+y)-3

def ord_debut(f,x0,a,b,eps):   #pas besoin de vérifier s'il y a inversion de signe car c'est une donnée de l'énoncé
    while (b-a)<eps:
        y0=(a+b)/2
        if f(x0,y0)*f(x0,a)>0:
            a=y0
        else:
            b=y0
    return y0
    
##Exercice 3 - 4)

def der_f(f,x,y,h):
    return (f(x+h,y)-f(x-h,y))/(2*h)   # calcul de la dérivée 
    
##Exercice 3 - 5)

def ord_newton(x,x0,eps):
    y=y0
    x=y0+2*eps
    while abs(x-y)>eps:
        x=y
        y=y-f(x,y0)/der_f(f,x,y,h)
    return y
    
