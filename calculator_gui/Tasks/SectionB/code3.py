# Problem Statement : calculation of the state vector from the orbital elements


import numpy as np 

def coe_to_sv(h: float, e: float, RA: float, incl: float, w: float, TA: float) -> [float], [float]:
    global mu
    rxp = (h**2 / mu) * (1/(1 + e*np.cos(TA))) * (np.array([[np.cos(TA)], [np.sin(TA)], [0]]))
    vxp = (mu / h) * (np.array([[-np.sin(TA)], [e + np.cos(TA)], [0]]))

    R3_W = np.array([[np.cos(RA), np.sin(RA), 0], [-np.sin(RA), np.cos(RA), 0], [0, 0, 1]])
    R1_i = np.array([[1, 0, 0], [0, np.cos(incl), np.sin(incl)], [0, -np.sin(incl), np.cos(incl)]])
    R3_w = np.array([[np.cos(w), np.sin(w), 0], [-np.sin(w), np.cos(w), 0], [0, 0, 1]])
    
    temp_cal = np.dot(R3_w, R1_i)
    QXx = np.dot(temp_cal, R3_W)

    QxX = np.transpose(QXx)

    rX = np.dot(QxX, rxp)
    vX = np.dot(QxX, vxp)
    return rX, vX

global mu 
mu = 398600
pi = 3.14
deg = pi / 180

# h = 80000
# e = 1.4
# RA = 40 * deg
# incl = 30 * deg
# w = 60 * deg
# TA = 30 * deg

h = float(input("Value of h : "))
e = float(input("Value of e : "))
RA = float(input("Value of RA : "))
RA = RA * deg 
incl = float(input("Value of incl : "))
incl = incl * deg
w = float(input("Value of w : "))
w = w * deg
TA = float(input("Value of W : "))
TA = TA * deg

rX, vX = coe_to_sv(h, e, RA, incl, w, TA)

print("rX = \n", rX)
print("vX = \n", vX)
