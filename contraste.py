import imageio
import numpy as np

image=imageio.imread(".png") #à compléter 

image=np.array(image,dtype=np.uint8)
image=image[:,:,:3]  #permet d'enlever la 4 couche qui correspond à la transparence
taille=image.shape

print(taille)

def nuance_gris(L):
	r=0.33
	g=0.34		#definition des coefficients pour la nuance de gris
	b=0.33
	taille=L.shape
	a=taille[0]
	b=taille[1]
	#L_constraste=L.copy()
	#L_constraste=r*L[:,:,0]+g*L[:,:,1]+b*L[:,:,2]
	for i in range(a):
		for j in range(b):
			sous_liste=L[i][j]
			R=sous_liste[0]
			G=sous_liste[1]
			B=sous_liste[2]
			valeur_gris=int(r*R+g*G+b*B)
			L[i][j]=[valeur_gris,valeur_gris,valeur_gris]
	
	return L

def contraste(L):
	seuil=128
	taille=L.shape
	a=taille[0]
	b=taille[1]
	for i in range(a):
		for j in range(b):
			valeur=L[i][j][0]
			if valeur<seuil:
				L[i][j]=[0,0,0]
			else:
				L[i][j]=[255,255,255]
	return L

def contraste_gris(L): # passage au gris, puis affectation noir et blanc automatiqueL
	r=0.33
	g=0.34		#definition des coefficients pour la nuance de gris
	b=0.33
	seuil=128
	taille=L.shape
	a=taille[0]
	b=taille[1]
	for i in range(a):
		for j in range(b):
			sous_liste=L[i][j]
			R=sous_liste[0]
			G=sous_liste[1]
			B=sous_liste[2]
			valeur_gris=int(r*R+g*G+b*B)
			if valeur_gris<seuil:
				L[i][j]=[0,0,0]
			else:
				L[i][j]=[255,255,255]
	return L


image_nuance_gris=nuance_gris(image)
imageio.imwrite("",image_nuance_gris)  #à compléter 

def nombre_voisin(L,i,j):
	compteur=0
	test=255
	if L[i-1][j-1][0]==test:
		compteur+=1
	elif L[i-1][j][0]==test:
		compteur+=1
	elif L[i-1][j+1][0]==test:
		compteur+=1
	elif L[i][j-1][0]==test:
		compteur+=1
	elif L[i][j+1][0]==test:
		compteur+=1
	elif L[i+1][j-1][0]==test:
		compteur+=1
	elif L[i+1][j][0]==test:
		compteur+=1
	elif L[i+1][j+1][0]==test:
		compteur+=1
	return compteur


def filtre_trois(L): #filtre contraste plus contraignant, il faut au moins trois pixel blanc a coté pour y le rester
	seuil_compteur=3
	taille=L.shape
	a=taille[0]
	b=taille[1]
	for i in range(1,a-1):
		for j in range(1,b-1):
			if L[i][j][0]==255:
				nbr_voisin=nombre_voisin(L,i,j)
				if nbr_voisin<2:
					L[i][j]=[0,0,0]
	return L

image_filtre=filtre_trois(image)
imageio.imwrite("",image_filtre)  #à compléter 

