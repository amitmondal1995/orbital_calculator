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
