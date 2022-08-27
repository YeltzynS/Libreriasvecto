import numpy as np

# SUMA NUMEROS COMPLEJOS
def suma_complejos(m,n):
    preal = m[0] + n[0]
    pimag = m[1] + n[1]
    return(preal , pimag)

# RESTA DE NUMEROS COMPLEJOS
def resta_complejos(m,n):
    preal = m[0] - n[0]
    pimag = m[1] - n[1]
    return(preal , pimag)

# PRODUCTO NUMEROS COMPLEJOS
def prod_complejos(m,n):
    preal = (m[0] * n[0]) - (m[1] * n[1])
    pimag = (m[0] * n[1]) + (n[0] * m[1])
    return(preal , pimag)



#DIVISION NUMEROS COMPLEJOS
def div_complejos(m,n):
    preal = ((((m[0] * n[0]) + (m[1] * n[1])) / ((n[0] ** 2) + (n[1] ** 2))))
    pimag = ((((m[1] * n[0]) - (m[0] * n[1])) / ((n[0] ** 2) + (n[1] ** 2))))
    return (preal , pimag)



#MODULO NUMEROS COMPLEJOS
def mod_complejos(m):
    modulo = (((m[0] ** 2) +(m[1] ** 2)) ** 1/2)
    return modulo


#CONJUGADO NUMEROS COMPLEJOS
def conj_complejos(m):
    conjreal = (m[0] * -1)
    conjimag = (m[1] * -1)
    return (conjreal , conjimag)


#POLAR A CARTESIANOS
def polar_cart(m):
    theta = np.arctan2(m[1] , m[0])
    rho = np.sqtr(m[1] , m[0]) + (m[1] * m[1])
    return (rho , theta)


#FASE DE NUMEROS COMPLEJOS
def fase_complejos(m):
    theta = np.arctan2(m[1]/m[0])
    return theta



def prettyprinting(m):
    print( str(m[0]) + "+" + str(m[1]) + "i")

def polprettyprinting(m):
    print( str(m[0]) + "e^(i " + str(m[1]) + ")")

print(polprettyprinting(fase_complejos([1,1])))


