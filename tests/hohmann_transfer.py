import sys, os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))

from orbital_gui.tasks.hohmann_transfer import hohmann_transfer

# Example:
mu_earth = 398600.4418  # Gravitational parameter for Earth, km^3/s^2
r1 = 6678  # Radius of initial orbit (LEO), km
r2 = 42164  # Radius of geostationary orbit (GEO), km

transfer_info = hohmann_transfer(r1, r2, mu_earth)
for key, value in transfer_info.items():
    print(f"{key}: {value:.2f}")
