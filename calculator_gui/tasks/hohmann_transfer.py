"""
This module provides functionality to calculate parameters for a Hohmann transfer orbit.
"""


import math

def hohmann_transfer(r1, r2, mu):
    """
    Calculate the Hohmann transfer orbit parameters between two circular orbits.

    Parameters:
    r1 (float): Radius of the initial orbit.
    r2 (float): Radius of the final orbit.
    mu (float): Standard gravitational parameter of the central body.

    Returns:
    dict: A dictionary with the calculated orbit parameters.
    """
    # Semi-major axis of the transfer ellipse
    a = (r1 + r2) / 2

    # Velocities in the initial and final orbits
    v1 = math.sqrt(mu / r1)
    v2 = math.sqrt(mu / r2)

    # Velocities at periapsis and apoapsis of the transfer ellipse
    vp = math.sqrt(mu * (2/r1 - 1/a))
    va = math.sqrt(mu * (2/r2 - 1/a))

    # Delta-Vs required for the transfer
    delta_v1 = vp - v1
    delta_v2 = v2 - va

    # Period of the transfer orbit
    time_period = 2 * math.pi * math.sqrt(a**3 / mu)

    return {
        'semi-major axis': a,
        'velocity at periapsis': vp,
        'velocity at apoapsis': va,
        'initial orbit velocity': v1,
        'final orbit velocity': v2,
        'delta-V for initial burn': delta_v1,
        'delta-V for final burn': delta_v2,
        'period of transfer orbit': time_period
    }
