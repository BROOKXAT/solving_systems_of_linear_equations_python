import numpy as np

def gradientpasoptimal(A,B,tol) :
    x0=np.array([0,0,0,1])
    r0=np.dot(A,x0)-B
    ni,x,R=0,x0,r0
    while (np.linalg.norm(R)/np.linalg.norm(r0))>tol :
        ni+=1
        alpha=(np.linalg.norm(R)**2)/np.dot(R.T,np.dot(A,R))
        x=x-(alpha*R)
        R=np.dot(A,x)-B
    return x,ni
A=np.array([
    [4,4,2,0],
    [4,5,0,0],
    [2,0,6,1],
    [0,0,1,2]
])
b=np.array([1,2,3,4])
print(gradientpasoptimal(A,b,0.001))