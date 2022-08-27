import numpy as np
def suma_complejos(m,n):
    preal = m[0] + n[0]
    pimag = m[1] + n[1]
    return(preal , pimag)


def resta_complejos(m,n):
    preal = m[0] - n[0]
    pimag = m[1] - n[1]
    return(preal , pimag)


def prod_complejos(m,n):
    preal = (m[0] * n[0]) - (m[1] * n[1])
    pimag = (m[0] * n[1]) + (n[0] * m[1])
    return(preal , pimag)




def div_complejos(m,n):
    preal = ((((m[0] * n[0]) + (m[1] * n[1])) / ((n[0] ** 2) + (n[1] ** 2))))
    pimag = ((((m[1] * n[0]) - (m[0] * n[1])) / ((n[0] ** 2) + (n[1] ** 2))))
    return (preal , pimag)




def mod_complejos(m):
    modulo = (((m[0] ** 2) +(m[1] ** 2)) ** 1/2)
    return modulo



def conj_complejos(m):
    conjreal = (m[0] * -1)
    conjimag = (m[1] * -1)
    return (conjreal , conjimag)



def polar_cart(m):
    theta = np.arctan2(m[1] , m[0])
    rho = np.sqtr(m[1] , m[0]) + (m[1] * m[1])
    return (rho , theta)



def fase_complejos(m):
    theta = np.arctan2(m[1]/m[0])
    return theta



def prettyprinting(m):
    print( str(m[0]) + "+" + str(m[1]) + "i")

def polprettyprinting(m):
    print( str(m[0]) + "e^(i " + str(m[1]) + ")")

print(polprettyprinting(fase_complejos([1,1])))


