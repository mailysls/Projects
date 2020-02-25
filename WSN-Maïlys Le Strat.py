from tkinter import *
 
from tkinter import ttk

##Paramétrage de l'interface

#Création de la fenêtre
window = Tk()
window.title("Gestionnaire de cycle")
window.geometry('470x530')
 
tab_control = ttk.Notebook(window)

#Permet la création de 3 onglets différents (tab1->Composants, tab2->Capteurs, tab3->Paramètres)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
 
tab_control.add(tab1, text='Composants')
tab_control.add(tab2, text='Capteurs')
tab_control.add(tab3, text='Paramètres')

#REMARQUE: Pour l'affichage de la courbe, on doit avoir :
#         les puissances en mW,les durées en ms
#Cependant, pour ne pas que l'utilisateur ait à rentrer des valeurs à rallonge avec beaucoup de virgule, sur l'interface il rentrera les valeurs dans l'unité indiqué et la conversion dans la bonne unité sera fait dans le code. 

## Fenetre Composants 

#cette fenètre permet à l'utilisateur de régler les paramètres du microcontroleurs et de l'emetteur recepteur 

#fonctions permettant de commander les boutons valider du microcontroleur et de l'emmeteur recepteur ->récuperer les valeurs rentrés par l'utilisateur avec la fonction get(). On obtiendra alors la liste microcontroleur et capteurs sous la forme : [Pveille,Pactif,Preveil,Tactif,Tréveil]
def micro():    
    global microcontroleur
    Pv=Pveille.get()*0.001   # *0.001 ->conversion en mW
    Pr=Preveil.get()*0.001   #idem
    Po=Pon.get()*0.001       #idem
    Tr=Treveil.get()
    To=Ton.get()
    print([Pv,Po,Pr,To,Tr])
    microcontroleur=[Pv,Po,Pr,To,Tr]

def emetteur_recepteur():   
    global emet_recept
    Pv=Pveille1.get()*0.001   #idem
    Pr=Preveil1.get()   
    Po=Pon1.get()     
    Tr=Treveil1.get()
    To=Ton1.get()
    print([Pv,Po,Pr,To,Tr])
    emet_recept=[Pv,Po,Pr,To,Tr]
    

#Interface Microcontôleur

label_micro= Label(tab1, text="  Microcontrôleur  ", font=("Arial Bold",11,'bold'),fg="dimgray")
label_micro.grid(column=1, row=0)

#Chaque bloc ci-dessous permet d'obtenir les puissances et temps du microcontroleur que l'utilisateur rentre sur l'interface. Par ailleurs, j'ai fixé une valeur par défaut (avec set()) correspondant aux valeurs du cours. L'utilisateur peut rentrer des float grâce à la fonction DoubleVar() et à la ligne de code "%.2f" dans le réglage de la Spinbox

Pveille=DoubleVar()
Pveille.set(0.15)
label_micro= Label(tab1, text="Pveille (μW)", font=("Arial Bold",8))
label_micro.grid(column=0,row=1)
spin1 = Spinbox(tab1, from_=0, to=100, width=6, textvariable=Pveille,format="%.2f") 
spin1.grid(column=0,row=2)

Preveil=DoubleVar()
Preveil.set(2.7)
label_micro= Label(tab1, text="Preveil (μW)", font=("Arial Bold",8))
label_micro.grid(column=1,row=1)
spin2 = Spinbox(tab1, from_=0, to=100, width=7,textvariable=Preveil,format="%.2f") 
spin2.grid(column=1,row=2)

Pon=DoubleVar()
Pon.set(2.7)
label_micro= Label(tab1, text="Pon (μW)", font=("Arial Bold",8))
label_micro.grid(column=2,row=1)
spin3 = Spinbox(tab1, from_=0, to=100, width=6,textvariable=Pon,format="%.2f") 
spin3.grid(column=2,row=2)

Treveil=DoubleVar()
Treveil.set(1500)
label_micro= Label(tab1, text="Treveil (ms)", font=("Arial Bold",8))
label_micro.grid(column=1,row=3)
spin4 = Spinbox(tab1, from_=0, to=3000, width=8,textvariable=Treveil,format="%.2f") 
spin4.grid(column=1,row=4)

Ton=DoubleVar()
Ton.set(0.1)
label_micro= Label(tab1, text="Ton (ms)", font=("Arial Bold",8))
label_micro.grid(column=2,row=3)
spin5 = Spinbox(tab1, from_=0, to=100, width=6,textvariable=Ton,format="%.2f") 
spin5.grid(column=2,row=4)

label_micro= Label(tab1, text="     ")
label_micro.grid(column=1, row=6)

#Création du bouton Valider, lorsque l'utilisateur appuira dessus cela permettra de garder en mémoire la liste microcontroleur. La ligne command=micro déclenche le code micro() lorsque le bouton est préssé. 
btn_m = Button(tab1, text='Valider',command=micro)
btn_m.grid(column=1, row=7)

label_micro= Label(tab1, text=" ________________________________    ")
label_micro.grid(column=1, row=8)

#Interface Emetteur récepteur

label_em= Label(tab1, text="  Emetteur récepteur  ", font=("Arial Bold",11,'bold'),fg="dimgray")
label_em.grid(column=1, row=9)

#Chaque bloc ci-dessous permet d'obtenir les puissances et temps de l'emetteur récepteur. Idem que pour le microcontroleur ci dessus. 

Pveille1=DoubleVar()
Pveille1.set(2.7)
label_em= Label(tab1, text="Pveille (μW)", font=("Arial Bold",8))
label_em.grid(column=0,row=10)
spin1_em = Spinbox(tab1, from_=0, to=100, width=6,textvariable=Pveille1,format="%.2f") 
spin1_em.grid(column=0,row=11)

Preveil1=DoubleVar()
Preveil1.set(1)
label_em= Label(tab1, text="Preveil (mW)", font=("Arial Bold",8))
label_em.grid(column=1,row=10)
spin2_em = Spinbox(tab1, from_=0, to=100, width=6,textvariable=Preveil1,format="%.2f") 
spin2_em.grid(column=1,row=11)

Pon1=DoubleVar()
Pon1.set(33.9)
label_em= Label(tab1, text="Pon (mW)", font=("Arial Bold",8))
label_em.grid(column=2,row=10)
spin3_em = Spinbox(tab1, from_=0, to=200, width=6,textvariable=Pon1,format="%.2f") 
spin3_em.grid(column=2,row=11)

Treveil1=DoubleVar()
Treveil1.set(100)
label_em= Label(tab1, text="Treveil (ms)", font=("Arial Bold",8))
label_em.grid(column=1,row=12)
spin4_em = Spinbox(tab1, from_=0, to=500, width=6,textvariable=Treveil1,format="%.2f") 
spin4_em.grid(column=1,row=13)

Ton1=DoubleVar()
Ton1.set(0.35)
label_em= Label(tab1, text="Ton (ms)", font=("Arial Bold",8))
label_em.grid(column=2,row=12)
spin5_em = Spinbox(tab1, from_=0, to=50, width=6,textvariable=Ton1,format="%.2f") 
spin5_em.grid(column=2,row=13)

label_em= Label(tab1, text="     ")
label_em.grid(column=1, row=14)

#Bouton valider relié à la commande emetteur_recepteur (cette fonction garde en mémoire la liste emet_recept)
btn_em = Button(tab1, text='Valider',command=emetteur_recepteur)
btn_em.grid(column=1, row=15)


## Fenetre Capteur
C=[]   #Création de la liste vide C qui contiendra les listes correspondant aux différents capteurs, elle sera utilisé comme variable globale. 

#Nombre_capteur() : Garde en mémoire le nombre de capteur(nbCapt qui est une variable global) et permet de compléter l'interface en ajoutant une combobox pour choisir le capteur que nous voulons modifier

def Nombre_capteur():   
    global nbCapt
    nbCapt=Nbcapt.get()
    
    #Création de la liste de la Combobox de [1,2,..,nbCapt]
    L=[]
    for i in range(1,nbCapt+1):
        L.append(i)
        
    label_capt = Label(tab2, text="Modification du capteur n° : ", font=("Arial Bold",8))
    label_capt.grid(column=0,row=3)
    
    combo=ttk.Combobox(tab2,values=L,width=4)
    combo.grid(column=1,row=3)
    
    #Bouton ✓: lié à la commande ajout_capteur 
    btn=Button(tab2,text="✓",command=ajout_capteur)
    btn.grid(column=2,row=3)
    
    return(nbCapt)
 
#ajout_capteur(): appelle la fonction modif_capteur qui permettra de modifier le capteur sélectionné via la combobox 
def ajout_capteur():
    labelc= Label(tab2, text=" _________________________    ")
    labelc.grid(column=0, row=4)
    modif_capteur()

#sup_capt(): permet de supprimer le capteur sélectionné par l'utilisateur
def sup_capt():
    numCapt=captSup.get()
    del C[numCapt-1]
    print(C)
    
#modif_capteurs(): Complête l'interface en permettant à l'utilisateur de modifier les caractéristiques des capteurs sélectionnés. Toutes les puissances et temps sont des variables global car on doit garder en mémoire ces valeurs car elles vont être utilisés dans une autre fonction. On évite ainsi de les passer en argument. 
def modif_capteur():
    global Pveille2
    global Preveil2
    global Pon2
    global Treveil2
    global Ton2
    global captSup
    
    #Les blocs suivant permettent d'obtenir les puissances et les temps du capteur séléctionné via la combobox. Idem que pour le microcontroleur et pour l'émetteur récepteur
    Pveille2=DoubleVar()
    Pveille2.set(15)
    label2= Label(tab2, text="Pveille (μW)", font=("Arial Bold",8))
    label2.grid(column=0,row=5)
    spin12 = Spinbox(tab2, from_=0, to=100, width=6,textvariable=Pveille2,format="%.2f") 
    spin12.grid(column=1,row=5)
    
    Preveil2=DoubleVar()
    Preveil2.set(1.5)
    label2= Label(tab2, text="Preveil (mW)", font=("Arial Bold",8))
    label2.grid(column=0,row=6)
    spin22 = Spinbox(tab2, from_=0, to=100, width=6,textvariable=Preveil2,format="%.2f") 
    spin22.grid(column=1,row=6)
    
    Pon2=DoubleVar()
    Pon2.set(1.5)
    label2= Label(tab2, text="Pon (mW)", font=("Arial Bold",8))
    label2.grid(column=0,row=7)
    spin32 = Spinbox(tab2, from_=0, to=100, width=6,textvariable=Pon2,format="%.2f") 
    spin32.grid(column=1,row=7)
    
    Treveil2=DoubleVar()
    Treveil2.set(2)
    label2= Label(tab2, text="Treveil (ms)", font=("Arial Bold",8))
    label2.grid(column=0,row=8)
    spin42 = Spinbox(tab2, from_=0, to=100, width=6,textvariable=Treveil2,format="%.2f") 
    spin42.grid(column=1,row=8)
    
    Ton2=DoubleVar()
    Ton2.set(2)
    label2= Label(tab2, text="Ton (ms)", font=("Arial Bold",8))
    label2.grid(column=0,row=9)
    spin52 = Spinbox(tab2, from_=0, to=100, width=6,textvariable=Ton2,format="%.2f") 
    spin52.grid(column=1,row=9)
    
    label_rien=Label(tab2,text=" ")
    label_rien.grid(column=0,row=10)
    
    #Bouton valider lié à la commande capt
    btn_val=Button(tab2, text='Valider',command=capt)
    btn_val.grid(column=0,row=11)
    
    label_v=Label(tab2, text='  ')
    label_v.grid(column=0,row=12)
    
    #Les lignes suivantes permettent à l'utilisateur de supprimer un capteur qu'il a déja paramétré s'il le souhaite 
    captSup=IntVar()
    captSup.set(0)
    label_sup=Label(tab2, text='Capteurs à supprimer')
    label_sup.grid(column=0,row=13)
    spin62 = Spinbox(tab2, from_=0, to=nbCapt, width=6,textvariable=captSup) 
    spin62.grid(column=1,row=13)
    
    #Le bouton supprimer est relié à la fonction sup_capt
    btn_s=Button(tab2, text='Supprimer',command=sup_capt)
    btn_s.grid(column=2, row=13)
    
    
    
#capt(): Permet de garder en mémoire la liste de tous les capteurs. 
def capt(): 
    global C
    Pv=Pveille2.get()*0.001   #conversion en mW
    Pr=Preveil2.get()   
    Po=Pon2.get()     
    Tr=Treveil2.get()
    To=Ton2.get()
    C.append([Pv,Po,Pr,To,Tr])
    print(C)
 
    return [Pv,Po,Pr,To,Tr]

capteurs=C   #liste des capteurs utilisés avec leurs caractéristiques 

#Interface Capteurs : Permet seulement de choisir le nombre de capteurs

label_capteurs = Label(tab2, text="                         Capteurs", font=("Arial Bold",11,'bold'),fg="dimgray")
label_capteurs.grid(column=0, row=0)

label_capt = Label(tab2, text="Nombre de capteurs", font=("Arial Bold",8))
label_capt.grid(column=0, row=2)

Nbcapt=IntVar()
Nbcapt.set(1)
spin_capt=Spinbox(tab2,from_=0, to=15, width=6,textvariable=Nbcapt)
spin_capt.grid(column=1,row=2)

btn_capt = Button(tab2, text='✓',command=Nombre_capteur)   #Bouton ✓ lié à la fonction Nombre_capteur 
btn_capt.grid(column=2, row=2)


## Fenêtre Paramètres 

#Interface réservoir

#R(): Retourne l'énergie contenue dans le réservoir à l'origine 
def R():
    en=energie.get()
    print(en)
    return(en)


label_alim = Label(tab3, text="                         Alimentation", font=("Arial Bold",11,'bold'),fg="dimgray")
label_alim.grid(column=0, row=0)

label_capteurs = Label(tab3, text="Capacité du réservoir (en Joule)", font=("Arial Bold",8))
label_capteurs.grid(column=0, row=1)

energie=DoubleVar()
energie.set(5000)
txt=Entry(tab3,width=7,text=energie)
txt.grid(column=1,row=1)

#Bouton lié à la commande R. 
btn_alim=Button(tab3,text="✓",command=R)
btn_alim.grid(column=2,row=1)

label_capteurs = Label(tab3, text="    ")
label_capteurs.grid(column=0, row=2)

#Interface Contrôleur de charge 

#puis_cc(): Retourne la puissance consommé par le contrôleur de charge  
def puis_cc():
    global PContCharge
    PContCharge=Pcc.get()
    print(PContCharge)
    return PContCharge

label_cc=Label(tab3,text="                  Contrôleur de charge", font=("Arial Bold",11,'bold'),fg="dimgray")
label_cc.grid(column=0,row=3)

label_cc = Label(tab3, text="Puissance du controleur de charge (en mW)", font=("Arial Bold",8))
label_cc.grid(column=0,row=4)

Pcc=DoubleVar()
Pcc.set(0)
spin_cc=Spinbox(tab3, from_=0, to=1000, width=6,textvariable=Pcc,format="%.2f")
spin_cc.grid(column=1,row=4)

#Bouton lié à la commande puis_cc (ci-dessus)
btn_cc=Button(tab3,text='✓',command=puis_cc)
btn_cc.grid(column=2,row=4)

#Phase final de l'interface pour fermer la fénêtre

#Cycle(): Garde en mémoire le nombre de cycle voulu par l'utilisateur. Si l'utilisateur choisi la valeur 0, il y aura le nombre de cycle nécéssaire pour décharger le réservoir
def Cycle():
    global nbC
    nbC=nbCycle.get()
    print(nbC)

#fermer(): Détruit la fénêtre principal et ouvre une nouvelle fenêtre
def fermer():
    shutdown_ttk_repeat()


label_end = Label(tab3, text="_____________")
label_end.grid(column=0,row=5)

#Choix du nombre de cycle 
label_end = Label(tab3, text="Nombre de cycle" )
label_end.grid(column=0,row=6)

nbCycle=IntVar()
nbCycle.set(1)
spin_cc=Spinbox(tab3, from_=0, to=20, width=6,textvariable=nbCycle)
spin_cc.grid(column=1,row=6)

btn_C=Button(tab3,text='✓',command=Cycle)
btn_C.grid(column=2,row=6)

label_end = Label(tab3, text="NbCycle=0 -> Nbcycle non défini ",font=("Arial",7,'italic'))
label_end.grid(column=0,row=7)


#Bouton Valider et quitter lié à la commande fermer
btn_end=Button(tab3,text='Valider et quitter',fg="red",command=fermer)
btn_end.grid(column=0,row=9)


##End Interface 
tab_control.pack(expand=1, fill='both')

def shutdown_ttk_repeat():     #permet d'éviter des bugs lors de l'utilisation de la bibliothèque Tkinter
    window.eval('::ttk::CancelRepeat')
    window.destroy()
    


window.protocol("WM_DELETE_WINDOW", shutdown_ttk_repeat)

window.mainloop()



## Code permettant l'affichage du cycle 

global P
global tps
tps=[-2,0]   #On incrémente à -2 et 0 ce qui correspondra au step0 ou tous les composants sont considérés en veille 
P=[]

#Temps choisit par défaut. Ces temps auraient également pu être choisit par l'utilisateur via l'interface.
global ttd
ttd=50  #temps de traitement des données et de l'envoi des données
global tmv
tmv=50 #temps de mise en veille

t_res=[0]

reservoir=R()
res=[R()]



##
import matplotlib.pyplot as plt 

#Calcul_res(t,puis): Permet de calculer l'énergie restant dans le réservoir après chaque étape. reservoir -> variable gardant en mémoire l'énergie dans le réservoir à chaque étape; res -> liste contenant l'énergie à la durée t. 
def calcul_res(t,puis):
    global res     # global car on doit garder en mémoire leur dernière valeur.
    global t_res
    global reservoir
    reservoir=reservoir-t*puis
    res.append(reservoir)
    t_res.append(t_res[-1]+t)

#tpsMax_micro_emet(..): Permet de calculer la durée maximale de l'étape entre le mircroporcesseur et l'emetteur. Renvoie ensuite la valeur max qui sera donc la durée utilisé lors d'une étape qui utilise ces 2 composants
def tpsMax_micro_emet(L1,L2,ind1,ind2):
    t_max=L1[ind1]
    if L2[ind2]>=t_max:
        t_max=L2[ind2]
    return t_max

#tpsmax_micro_capteur(..): Idem que la fonction précédente mais cette fois pour une étape ou le microprocesseur et les capteurs sont utilisés simultanément.
def tpsmax_micro_capteur(L,C,ind_l,ind_c):
    t_max=L[ind_l]
    t_C=C[0][ind_c]
    for i in range (len(C)):
        if t_C<=C[i][ind_c]:
            t_C=C[i][ind_c]
    if t_C>=t_max:
        t_max=t_C
    return t_max

#veille(L): Cette fonction va être utilisé à chaque étape pour soustraire de la somme des puissances la puissance en veille des composants utilisés dans l'étape correspondantes. Ce calcul va être fait différement si c'est un microcontroleur/emetteur_recepteur ou des capteurs 
def veille(L):
    N=len(L)
    if len(L)==5:
        CompoVeille=P[0]-L[0]
    else: 
        for i in range(N):
            CompoVeille=P[0]-(L[i][0])
    return CompoVeille

#Puissance_capt(...): Calcul la somme des puissances des différents capteurs utilisés 
def Puissance_capt(C,ind,N):
    P_capt=0
    for i in range(len(C)):
        P_capt+=C[i][ind]
    return P_capt
    
def incremente_tps(t):
    tps.append(tps[-1])
    tps.append(tps[-1]+t)

def incremente_P(puissance):
    P.append(puissance)
    P.append(puissance)

#step0_veille(L1,L2,C): Avant d'entreprendre l'étape 1 (réveil du microcontroleur), je considère que tous les composants sont en veille. On a donc besoin de calculer la somme de la puissance en veille de tous les composants. 
def step0_veille(L1,L2,C):
    P0=L1[0]+L2[0]
    for i in range (len(C)):
        P0+=C[i][0]
    incremente_P(P0)
    return P0

#step1(L): Réveil du microcontrôleur
def step1(L):
    Pv=veille(L)
    puis=L[2]
    incremente_tps(L[4])
    incremente_P(Pv+puis)
    calcul_res(L[4],Pv+puis)

#step2(L,C,N): Réveil des capteurs 
def step2(L,C,N):
    Pv=veille(C)
    Pbase=Pv-L[0]
    t_max=tpsmax_micro_capteur(L,C,3,4)
    incremente_tps(t_max)
    puis_C=Puissance_capt(C,2,N)
    puis_L=L[2]
    puis=Pbase+puis_C+puis_L
    incremente_P(puis)
    calcul_res(t_max,puis)

#step3(L,C,N): Mesures avec les capteurs     
def step3(L,C,N):
    Pv=veille(C)
    Pbase=Pv-L[0]
    t_max=tpsmax_micro_capteur(L,C,3,3)
    incremente_tps(t_max)
    puis_C=Puissance_capt(C,1,N)
    puis_L=L[2]
    puis=Pbase+puis_C+puis_L
    incremente_P(puis)
    calcul_res(t_max,puis)
   
#step4(L): Traitement des données et mise en sommeil des capteurs 
def step4(L):   
    Pv=veille(L)
    incremente_tps(ttd)
    incremente_P(Pv+L[1])
    calcul_res(ttd,Pv+L[1])

#step5(L1,L2): Réveil de l'emetteur/recepteur
def step5(L1,L2):  
    Pv=veille(L1)
    pbase=Pv-L2[0]
    t_max=tpsMax_micro_emet(L1,L2,3,4)
    incremente_tps(t_max)
    puis=L1[1]+L2[2]+pbase
    incremente_P(puis)
    calcul_res(t_max,puis)

#step6(L1,L2): Envoie des données 
def step6(L1,L2):  
    Pv=veille(L1)
    pbase=Pv-L2[0]
    incremente_tps(ttd)
    puis=pbase+L1[1]+L2[1]
    incremente_P(puis)
    calcul_res(ttd,puis)

#Mise en veille de tous les composants
def step7(L1,L2,C):  
    step0_veille(L1,L2,C)
    incremente_tps(tmv)
    calcul_res(tmv,P[0])

#Cycle complet appelant toutes les étapes dans l'ordre     
def cycle(M,ER,C,N):
    step1(M)
    step2(M,C,N)
    step3(M,C,N)
    step4(M)
    step5(M,ER)
    step6(M,ER)
    step7(M,ER,C)

## Obtention du cycle 
#on considère dans un premier temps que tous les composants sont en veille 
Puisveille=step0_veille(microcontroleur,emet_recept,capteurs)


nbcycle=0
if nbC==0:  #Si l'utilisateur n'a pas renseigné le nombre de cycle 
    while res[-1]>Puisveille:  #tant que le réservoir est plus grand que 0 on fait un cycle. 
        cycle(microcontroleur,emet_recept,capteurs,nbCapt)
        nbcycle+=1
else:      # dans le cas contraire
    for i in range(nbC):
        while res[-1]>Puisveille:
            cycle(microcontroleur,emet_recept,capteurs,nbCapt)
            nbcycle+=1
            if nbcycle==nbC:  # Dans le cas ou tous les cycles demandé par l'utilisateur ont été complété 
                break
    print(nbcycle,"cycle(s) ont pu être complété, si cela ne correspond pas à la valeur que vous avez rentré, cela signifie que le réservoir n'était pas assez remplie.")
 

#Ajout de la puissance du controleur de charge (qui est constant)
for i in range (len(P)):
    P[i]=P[i]+PContCharge


##Affichage 
plt.show()

#affichage des cycles 
plt.subplot(1,2,1)
plt.plot(tps,P)
plt.title("Cycle de consommation")
plt.xlabel("Temps (ms)")
plt.ylabel("Puissance (mW)")
axes = plt.gca()
axes.set_xlim(-2,tps[-1]) 
axes.set_ylim(-10,70) 

#affichage de l'énergie en fonction du temps
plt.subplot(1,2,2)
plt.title("Energie consommée en fonction du temps")
plt.xlabel("Temps (ms)")
plt.ylabel("Energie (J)")
plt.plot(t_res,res)

if nbC==0:
    print("Le réservoir est vide au bout de ",nbcycle,"cycle(s)")

