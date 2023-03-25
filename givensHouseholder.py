from math import sqrt
import numpy as np 
import math
def norm2(v):
    somme=0
    for i in v :
        somme+=i**2
    return math.sqrt(somme)
def e(n):
    E=[0 for j in range(n)]
    E[0]=1
    return E

def matriceIDcreator(n):
    I=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j : I[i][j]=1
    return I

def uTu(u,n):
    v=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            v[i][j]=u[i]*u[j]
    return v 

def houseHolderCraetor(u,n):
    In=matriceIDcreator(n)
    utu=uTu(u,n)
    Hu=np.array(In)-2*np.array(utu)
    return Hu


def col(A,j,n):
    v=[]
    for k in range(0,n):
        v.append(A[k][j])
    return v


def VvectorGenerator(A,n,k) :
    v=[]
    sgma=0
    for i in range(k+1) : v.append(0)
    kcol=col(A,k,n)
    print(kcol[k:])
    for o in range(k+1,n):sgma+=A[i][k]*A[i][k]
    sgma=abs(sgma)
    sgma=math.sqrt(sgma)
    v.append(sqrt(0.5*(1+abs(A[k+1][k])/sgma)))
    B=2*v[k+1]*sgma
    if (A[k+1][k])>=0:
        for j in range(k+2,n):
            v.append(A[j][k]/B)
    else :
        for j in range(k+2,n) :
            v.append(-A[j][k]/B)
    return v


def tridiagonalizationHouseHolder(A,n) :
    Ac=np.array(A)
    for i in range(1,n-1):
        v=VvectorGenerator(Ac,n,i)
        print(v,"yoyo")
        Hv=houseHolderCraetor(v,n)
        vH=np.transpose(Hv)
        Ac=np.dot(Hv,Ac)
        Ac=np.dot(Ac,Hv)
        print("----------------------------------------")
        matricePrinter(Ac,4)
        print("-----------------------------------------")
    return Ac
def matricePrinter(M,n) :
    for i in range(n):
        for j in range(n):
            print(M[i][j],end="  ")
        print(" ")



A=[
    [4,4,2,0],
    [4,5,0,0],
    [2,0,6,1],
    [0,0,1,2]
]

tridiagonalizationHouseHolder(A,4)























print([0.04,1.82,5.975,9.164])































