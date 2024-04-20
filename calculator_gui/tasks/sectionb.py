# Problem Statement : calculation of the state vector (r, v) given the initial state vector (r 0 ,
# v 0 ) and the time lapse

import math
import numpy as np

MU = 398600


def main1(r0: list[float], v0: list[float], t: int) -> tuple[list[float], list[float]]:
    # magnitude
    r0_norm = np.linalg.norm(r0)
    v0_norm = np.linalg.norm(v0)
    r0 = np.array(r0)
    v0 = np.array(v0)
    print(f"r0 : {r0}  && v0 : {v0}")
    vr0 = np.dot(r0, v0) / r0_norm

    alpha = (2 / r0_norm) - (v0_norm**2) / MU
    print(f"alpha : {round(alpha * (10**5), 4)} x 10^(-5) Km^(-1)")

    x = kepler_u(t, r0_norm, vr0, alpha)
    print(f"x : {round(x, 4)}")

    f, g = f_and_g(x, t, r0_norm, alpha)
    print(f"f : {round(f, 4)} && g : {round(g, 4)}")

    R = (f * r0) + (g * v0)

    r = np.linalg.norm(R)
    print(f"r : {r}")

    fdot, gdot = fdot_and_gdot(x, r, r0_norm, alpha)
    print(f"fdot : {round(fdot, 4)} && gdot : {round(gdot, 4)}")

    V = fdot * r0 + gdot * v0
    print(V)

    return R, V


def stump_c(z):
    if z > 0:
        c = (1 - math.cos(math.sqrt(z))) / z
    elif z < 0:
        c = (math.cosh(math.sqrt(-z)) - 1) / (-z)
    else:
        c = 1 / 2
    return c


def stump_s(z):
    if z > 0:
        s = (math.sqrt(z) - math.sin(math.sqrt(z))) / (math.sqrt(z)) ** 3
    elif z < 0:
        s = (math.sinh(math.sqrt(-z)) - math.sqrt(-z)) / (math.sqrt(-z)) ** 3
    else:
        s = 1 / 6
    return s


def f_and_g(x, t, r0, alpha):
    f = 1 - (x**2 / r0) * stump_c(alpha * (x**2))
    g = t - (1 / math.sqrt(MU)) * (x**3) * stump_s(alpha * (x**2))
    return f, g


def fdot_and_gdot(x, r, r0, alpha):
    fdot = (math.sqrt(MU) / (r * r0)) * (alpha * (x**3) * stump_s(alpha * (x**2)) - x)
    gdot = 1 - (x**2 / r) * stump_c(alpha * (x**2))
    return fdot, gdot


def kepler_u(t, r0, vr0, alpha):
    error = 10 ** (-8)
    nMax = 1000
    x = math.sqrt(MU) * abs(alpha) * t
    ratio = 1
    itr = 0

    while abs(ratio) > error and itr < nMax:
        z = alpha * (x**2)
        f_xi = (
            (r0 * vr0 / math.sqrt(MU)) * (x**2) * stump_c(z)
            + (1 - alpha * r0) * (x**3) * stump_s(z)
            + r0 * x
            - math.sqrt(MU) * t
        )
        fdot_xi = (
            ((r0 * vr0 / math.sqrt(MU)) * x * (1 - alpha * (x**2) * stump_s(z)))
            + (1 - alpha * r0) * (x**2) * stump_c(z)
            + r0
        )
        ratio = f_xi / fdot_xi
        x = x - ratio

    return x

def main2(R: list[float], V: list[float]) -> tuple[float, float, float, float, float, float]:
    eps = 1e-10
    pi = 3.14
    rad = 180/(pi)
    r = np.linalg.norm(R)
    v = np.linalg.norm(V)
    R = np.array(R)
    V = np.array(V)

    vr = np.dot(R, V)/r
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


    E = (1/MU) * ((v**2 - MU/r)*R - r*vr*V)
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

    a = h**2/(MU * (1 - e**2))

    T = (2*pi / math.sqrt(MU)) * (math.sqrt(a**3))
    RA = RA*rad
    w = w*rad
    TA = TA*rad
    incl = incl*rad

    return h, incl, RA, e, w, TA, a, T

def main3(h:float, e:float, RA:float, incl:float, w:float, TA:float)->\
    tuple[list[float], list[float]]:
    rxp = (h**2 / MU) * (1/(1 + e*np.cos(TA))) * (np.array([[np.cos(TA)], [np.sin(TA)], [0]]))
    vxp = (MU / h) * (np.array([[-np.sin(TA)], [e + np.cos(TA)], [0]]))

    R3_W = np.array([[np.cos(RA), np.sin(RA), 0], [-np.sin(RA), np.cos(RA), 0], [0, 0, 1]])
    R1_i = np.array([[1, 0, 0], [0, np.cos(incl), np.sin(incl)], [0, -np.sin(incl), np.cos(incl)]])
    R3_w = np.array([[np.cos(w), np.sin(w), 0], [-np.sin(w), np.cos(w), 0], [0, 0, 1]])
    temp_cal = np.dot(R3_w, R1_i)
    QXx = np.dot(temp_cal, R3_W)

    QxX = np.transpose(QXx)

    rX = np.dot(QxX, rxp)
    vX = np.dot(QxX, vxp)
    return rX, vX
