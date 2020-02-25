from pylab import *
import numpy as np

def f_Affiche(image):
    figure()
    ion()
    imshow(image)
    show()
plt.close('all')

## Question 1
 
Image_missile=np.load("C:\\Users\\Mailys\\Documents\\Prépa Fontainebleau\\PSI\\Info\\Dossier_Missile\\Image_mi.npy")
# f_Affiche(Image_missile)

Nb_Lignes=Image_missile.shape[0] 
Nb_Colonnes=Image_missile.shape[1]

## Question 2-3

def f_Nuances_de_gris(im):
    im_cop=np.copy(im)
    kr=0.5
    kg=0.4
    kb=0.1
    for i in range (Nb_Lignes):
        for j in range (Nb_Colonnes):
            Pixel=im_cop[i,j]
            if Pixel[0]!=0 or Pixel[1]!=0 or Pixel[2]!=0:
                Nuance=kr*Pixel[0]+kg*Pixel[1]+kb*Pixel[2]
                Pixel[0]=Nuance
                Pixel[1]=Nuance
                Pixel[2]=Nuance
    return im_cop

Im_gris=f_Nuances_de_gris(Image_missile)

# f_Affiche(Im_gris)

## Question 4-5-6

def monochrome(im):
    im_cop=np.copy(im)
    M=np.zeros((Nb_Lignes,Nb_Colonnes))
    for i in range (Nb_Lignes):
        for j in range (Nb_Colonnes):
            Pixel=im_cop[i,j]
            if Pixel[0]>=127:
                Pixel[0],Pixel[1],Pixel[2]=255,255,255
                M[i,j]=255
            else:
                Pixel[0],Pixel[1],Pixel[2]=0,0,0
                M[i,j]=0
    return im_cop,M
    
Im_noir_blanc,Mat_pix=monochrome(Im_gris)
# print(Mat_pix)
# f_Affiche(Im_noir_blanc)

## Question 7

def f_CDG(Mat):
    Xg=0
    Yg=0
    somme_m=0
    for i in range(Nb_Lignes):
        for j in range(Nb_Colonnes):
            if Mat[i,j]==0:
                m=0
            else:
                m=255
            Yg=Yg+m*i
            Xg=Xg+m*j
            somme_m=somme_m+m
    Xg_f=Xg/somme_m
    Yg_f=Yg/somme_m
    return Xg_f,Yg_f

Xg,Yg=f_CDG(Mat_pix)
# print(Xg,Yg)

## Question 8-9
    
def f_Ajoute_CDG(im,X,Y,N):
    im_carre=np.copy(im)
    X=round(X)
    Y=round(Y)
    for i in range(Y-2*N,Y+2*N+1):
        for j in range(X-2*N,X+2*N+1):
            im_carre[i,j][0]=255
            im_carre[i,j][1]=0
            im_carre[i,j][2]=0
    return im_carre

Im_detection=f_Ajoute_CDG(Im_noir_blanc,Xg,Yg,10)
f_Affiche(Im_detection)

## Question 10

def f_ecarts(im,X,Y):
    Y0=Nb_Lignes/2
    X0=Nb_Colonnes/2
    Dx=X-X0
    Dy=Y0-Y
    return Dx,Dy

print(f_ecarts(Im_detection,Xg,Yg))

