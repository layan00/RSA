# Extended Euclidean Algorithm. 
# By Layan Alnamlah
# This program illustrates the Extended Euclidean Algorithm (a.k.a. the Pulverizer)
# it computes every component of the algorithms  
# last edited 4/23/2023

# consts
x = [1,0]
y = [0,1]
i = 0
R =[]
Q =[]
A = []
B = []

# for reusing the program because python apparently stores arrays' variables 
def clear():
    global x, y, i, R, Q, A, B
    x = [1,0]
    y = [0,1]
    i = 0
    R =[]
    Q =[]
    A = []
    B = []


def init(n,m):
    global R, Q, A, B, x, y, i
    R = [n%m]
    Q = [n//m]
    A =[n]
    B = [m]
    compute(n,m)

def compute(n,m):
    global R, Q, x, y, i, A, B 

    if (R[i] == 0):
        return (y[i]-y[i+1]*Q[i]) 

    x.append(x[i]-x[i+1]*Q[i])
    y.append(y[i]-y[i+1]*Q[i])

    Q.append(m // R[i]) 
    R.append(m % R[i])

    A.append(B[i])
    B.append(R[i])  
    i += 1
 
    compute(m,R[i-1])

 

def EEthm(n,m):

    init(n,m)

    ret = B[i]
    clear()
    return ret

# this function is redundent but it makes the code and passing of values neater 
def get_d(n,m):

    init(n,m)
    ret = y[i+1]
    clear()
    return ret


