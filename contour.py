import imageio
import numpy as np
from numpy import sqrt
 
image=imageio.imread(".png")  #à compléter 

image=np.array(image,dtype=np.uint8)
image=image[:,:,:3]  #permet d'enlever la 4 couche qui correspond à la transparence
taille=image.shape

##naive, couleur uni(noir et blanc)
def remplacement(L):
	taille=L.shape
	x=taille[0]
	y=taille[1]
	for i in range(1,x-1):
		for j in range(1,y-1):
			if L[x][y][0]!=L[x+1][y][0]:
				if L[x][y][0]==L[x-1][y][0]:
					L[x][y]=[50,255,50]
			elif L[x][y][0]!=L[x][y+1][0]:
				if L[x][y][0]==L[x][y-1][0]:
					L[x][y]=[50,255,50]

##détection de contour

def contour(L):
	taille=L.shape
	a=taille[0]
	b=taille[1]
	M=np.zeros(taille)    #pas besoin de la conversion en uint8
	for i in range(1,a-1):
		for j in range(1,b-1):
			Lh=L[i][j]-L[i-1][j]
			Lv=L[i][j]-L[i][j-1]
			M[i][j]=sqrt(Lh**2+Lv**2)
	return M

image_contour=contour(image)
imageio.imwrite("",image_contour)  #à compléter 


