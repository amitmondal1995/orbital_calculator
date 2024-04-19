# Problem statement : 2. calculation of the orbital elements from the state vector

import numpy as np
import math

def coe_from_sv(R: [float], V: [float]) -> float, float, float, float, float, float:
    global mu
    eps = 1e-10
    pi = 3.14
    rad = 180 / pi 
    
    r = np.linalg.norm(R)
    v = np.linalg.norm(V)

    vr = np.dot(R, V) / r 

    H = np.cross(R, V)  
    h = np.linalg.norm(H)

    incl = np.arccos(H[2]/h)

    N = np.cross([0, 0, 1], H)
    n = np.linalg.norm(N)

    if n != 0:
        RA = np.arccos(N[0]/n)
        if N[1] < 0:
            RA = 2*pi - RA
    else:
        RA = 0


    E = (1/mu) * ((v**2 - mu/r)*R - r*vr*V)
    e = np.linalg.norm(E)

    if n!= 0:
        if e > eps:
            w = np.arccos(np.dot(N, E)/(n*e))
            if E[2] < 0:
                w = 2*pi - w
        else:
            w = 0
    
        
    if e > eps:
        TA = np.arccos(np.dot(E, R)/(e*r))
        if vr < 0:
            TA = 2*pi - TA
    else:
        cp = np.cross(N, R)
        if cp[2] >= 0:
            TA = np.arccos(np.dot(N, R) / n*r)
        else:
            TA = 2*pi - np.arccos(np.dot(N, R) / n*r)

    a = h**2/(mu * (1 - e**2))

    T = (2*pi / math.sqrt(mu)) * (math.sqrt(a**3))

    return h, incl, RA, e, w, TA, a, T


global mu, pi 
pi =  3.1415926
mu = 398600
rad = 180 / pi

# r = np.array([-6045, -3490, 2500])
# v = np.array([-3.457, 6.618, 2.533])

r_l = []
v_l = []

for i in range(0, 3):
    val = float(input("value of r : "))
    r_l.append(val)

for i in range(0, 3):
    val = float(input("Value of v : "))
    v_l.append(val)

r = np.asarray(r_l)
v = np.asarray(v_l)

h, incl, RA, e, w, TA, a, T  = coe_from_sv(r, v)

print(f"R = {r[0]}i + {r[1]}j + {r[2]}k km")
print(f"V = {v[0]}i + {v[1]}j + {v[2]}k km/sec")

print(f"Angular Momentum (h): {h} km^2/sec")
print(f"Eccentricity (e): {e}")
print(f"Right ascension  (RA in deg): {RA * rad} deg")
print(f"Inclination (i): {incl * rad} deg")
print(f"Argument of perigee (w): {w * rad} deg")
print(f"True anomaly (TA): {TA * rad} deg")
print(f"Semi major axis : {a} km")
print(f"Time Period : {T} sec")
