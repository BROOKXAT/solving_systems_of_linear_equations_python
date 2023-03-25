from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def jacobi(A,b,N=25,x=None):
    
                                                                                                                                                               
    if x is None:
        x = zeros(len(A[0]))

                                                                                                                                                    
                                                                                                                                                                   
    D = diag(A)
    R = A - diag(D)

    for i in range(N):
        x = (b - dot(R,x)) / D
    return x

A = array([
    [4,4,2,0],
    [4,5,0,0],
    [2,0,6,1],
    [0,0,1,2]
])
b = array([1,2,3,4])
guess = array([-10,9,4,-1])

sol = jacobi(A,b,N=2500,x=guess)
print(sol)
