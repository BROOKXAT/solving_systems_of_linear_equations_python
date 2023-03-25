
import numpy.linalg as np
from decimal import Decimal
import math
from re import A

def Cholesky_Decomposition(matrix, n):
 
    lowM = [[0 for x in range(n + 1)]
                for y in range(n + 1)]
    upM=[[0 for x in range(n + 1)]
                for y in range(n + 1)]
 
    # Decomposing a matrix
    # into Lower Triangular
    for i in range(n):
        for j in range(i + 1):
            sum1 = 0
 
            # summation for diagonals
            if (j == i):
                for k in range(j):
                    sum1 += pow(lowM[j][k], 2)
                lowM[j][j] = math.sqrt(matrix[j][j] - sum1)
            else:
                 
                # Evaluating L(i, j)
                # using L(j, j)
                for k in range(j):
                    sum1 += (lowM[i][k] *lowM[j][k])
                if(lowM[j][j] > 0):
                    lowM[i][j] = ((matrix[i][j] - sum1) /lowM[j][j])
    
    return lowM


def theEqualizarLower(lowM,b,n):
    x=[0 for i in range(n)]
    for i in range(0,n):
        somme=0
        for j in range(0,n) :
            somme+=lowM[i][j]*x[j]
        a=1/lowM[i][i]
        x[i]=a*(b[i]-somme)
    return x


def theEqualizarUpper(Upper,b,n):
    x=[0 for i in range(n)]
    for i in range(n-1,-1,-1):
        somme=0
        for j in range(n-1,-1,-1) :
            somme+=Upper[i][j]*x[j]
        a=1/Upper[i][i]
        x[i]=a*(b[i]-somme)
    return x
def lower_to_upper(A,n):
    s=[[0 for i in range(n)] for j in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            s[j][i]=A[i][j]
    return s


def syswithcholesky(A,b,n):
    lowM=Cholesky_Decomposition(A,n)
    y=theEqualizarLower(lowM,b,n)
    upM=lower_to_upper(lowM,4)
    x=theEqualizarUpper(upM,y,n)
    return x

    



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
b=[1,2,3,4]
Z=Cholesky_Decomposition(A,4)
print("la matrice de cholesky :")
print("-----------------------")
matricePrinter(Cholesky_Decomposition(A,4),4)
print("------------------------------")
print("la solution ________________________")
print(syswithcholesky(A,b,4))   
# print(theEqualizarLower(Z,b,4))
print("-"*50)
#matricePrinter(lower_to_upper(Z,4),4)
print("-"*50)
#print(theEqualizarUpper(lower_to_upper(Z,4),b,4))                                           