from copy import copy
import math 
import numpy as np
def norm2(v):
    somme=0
    for i in v :
        somme+=i*i
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
def col(A,j,n):
    v=[]
    for k in range(j,n):
        v.append(A[k][j])
    return v

def fill_it_with_zeroes(X,n,N):
    if n==N :return X
    B=[[0 for i in range(N)] for j in range(N)]
    for i in range(N) :
        B[i][i]=1
    for j in range(N-n,N):
        for k in range(N-n,N):
            B[j][k]=X[j-N+n][k+n-N]
    return B





def houseHolderCraetor(u,n):
    In=matriceIDcreator(n)
    utu=uTu(u,n)
    Hu=np.array(In)-2*np.array(utu)
    return Hu

    


def matricePrinter(M,n) :
    for i in range(n):
        for j in range(n):
            print(M[i][j],end="  ")
        print(" ")
def theEqualizarUpper(Upper,b,n):
    x=[0 for i in range(n)]
    for i in range(n-1,-1,-1):
        somme=0
        for j in range(n-1,-1,-1) :
            somme+=Upper[i][j]*x[j]
        a=1/Upper[i][i]
        x[i]=a*(b[i]-somme)
    return x

A=[
    [4,4,2,0],
    [4,5,0,0],
    [2,0,6,1],
    [0,0,1,2]
]
B= [
    [2,1,2],
    [1,1,2],
    [2,1,1]
]
ww=[1,1,1]
def syswithHouseHolder(A,b,n) :
    Ac=np.array(A)
    bc=np.array(b)
    for i in range(n,1,-1):
        a=(1/norm2(np.array(col(Ac,n-i,n))))*np.array(col(Ac,n-i,n))-np.array(e(i))
        v=(1/(norm2(a)))*np.array(a)
        Hu=houseHolderCraetor(v,i)
        Hu=fill_it_with_zeroes(Hu,i,n)
        Ac=np.dot(Hu,Ac)
        bc=np.dot(Hu,bc)
    for i in range(n) :
        for j in range(n-1 ):
            if Ac[i][j] < 0.0000000001 and i>j :
                Ac[i][j]=0
     
    return [Ac,bc]










    
b=[1,2,3,4]   
cc=syswithHouseHolder(A,b,4)

#matricePrinter(tridiagonalGenerator(A,4),4)
print("MATRICE TRIANGULAIIRE SUPP -------------------------------------")
matricePrinter(cc[0],4)
print("--------------------------------------------------------------")
xxxx=theEqualizarUpper(cc[0],cc[1],4)
print("vecteur de solution-----------------------------")
print(xxxx)
#matricePrinter(fill_it_with_zeroes(A,4,8),8)
#print(cc)
#print(e(3,5))
#print(copy(A))
#rint(norm2(np.array(col(np.array(A),0,4))))