import numpy as np

def f_det(U,V):
	a,b,c,d=U[0],U[1],V[0],V[1]
	return a*d-b*c

def f_Aire_CG_Tri(A,P1,P2):
	P1=np.array(P1)
	P2=np.array(P2)
	AP1=P1-A
	AP2=P2-A
	aire=f_det(AP1,AP2)/2
	centre_g=np.array(AP1+AP2)/3
	return aire,centre_g

def f_Aire_CG(L):
	n=len(L)
	Aire_totale=0
	A=np.array([0,0])
	Centre_gravite=np.array([0,0])
	for i in range(0,n-1):
		P1=L[i]
		P2=L[i+1]
		Aire,centre_g=f_Aire_CG_Tri(A,P1,P2)
		Aire_totale+=Aire
		Centre_gravite=np.add(Aire*centre_g,Centre_gravite)
	P1=L[n-1]
	P2=L[0]
	Aire,centre_g=f_Aire_CG_Tri(A,P1,P2)
	Centre_gravite=np.add(Aire*centre_g,Centre_gravite)
	Aire_totale+=Aire
	Centre_gravite=Centre_gravite/Aire_totale
	return abs(Aire_totale),Centre_gravite

L = np.array([[2,2],[2,4],[3,5],[5,5],[7,3],[10,-1],[8,-2],[5,-3],[3,-3]])

print(f_Aire_CG(L))
