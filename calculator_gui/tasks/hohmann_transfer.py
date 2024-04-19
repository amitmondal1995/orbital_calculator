"""
This module provides functionality to calculate parameters for a Hohmann transfer orbit.
"""

from dataclasses import dataclass
import math

@dataclass
class HohmannTransferData:
    """
    Data class containing all the calculated parameters for a Hohmann transfer orbit.
    
    Attributes:
        semi_major_axis (float): Semi-major axis of the transfer ellipse.
        v_periapsis (float): Velocity at periapsis of the transfer ellipse.
        v_apoapsis (float): Velocity at apoapsis of the transfer ellipse.
        vi (float): Initial orbit velocity.
        vf (float): Final orbit velocity.
        delta_vi (float): Delta-V for the initial burn.
        delta_vf (float): Delta-V for the final burn.
        time_period (float): Period of the transfer orbit.
    """
    semi_major_axis: float
    v_periapsis: float
    v_apoapsis: float
    vi: float
    vf: float
    delta_vi: float
    delta_vf: float
    time_period: float

def hohmann_transfer(ri: float, rf: float, mu: float) -> HohmannTransferData:
    """
    Calculate the Hohmann transfer orbit parameters between two circular orbits.

    Parameters:
    ri (float): Radius of the initial orbit.
    rf (float): Radius of the final orbit.
    mu (float): Standard gravitational parameter of the central body.

    Returns:
    HohmannTransferData: Data class containing all the calculated parameters for the transfer.
    """
    # Calculate the semi-major axis of the transfer ellipse
    a = (ri + rf) / 2

    # Calculate velocities in the initial and final orbits
    vi = math.sqrt(mu / ri)
    vf = math.sqrt(mu / rf)

    # Calculate velocities at periapsis and apoapsis of the transfer ellipse
    v_periapsis = math.sqrt(mu * (2 / ri - 1 / a))
    v_apoapsis = math.sqrt(mu * (2 / rf - 1 / a))

    # Calculate the delta-Vs required for the transfer
    delta_vi = v_periapsis - vi
    delta_vf = vf - v_apoapsis

    # Calculate the period of the transfer orbit
    time_period = 2 * math.pi * math.sqrt(a**3 / mu)

    # Create and return an instance of HohmannTransferData
    return HohmannTransferData(
        semi_major_axis=a,
        v_periapsis=v_periapsis,
        v_apoapsis=v_apoapsis,
        vi=vi,
        vf=vf,
        delta_vi=delta_vi,
        delta_vf=delta_vf,
        time_period=time_period
    )
