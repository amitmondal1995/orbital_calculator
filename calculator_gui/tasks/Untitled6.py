import math

def kepler_hyperbolic(e: float, M: float, tol=1e-9, max_iter=1000)-> float:
    # Initial guess for eccentric anomaly (E)
    E = M / e
    
    # using Newton's method
    for _ in range(max_iter):
        f = e * math.sinh(E)-E - M
        f_prime = e * math.cosh(E)-1
        g= f / f_prime
        E= E- g
        
        # Check for convergence
        if abs(g) < tol:
            return E
    

# Example usage
e = float(input("Enter the value of Eccentricity:" )) # Eccentricity 
M = float(input("Enter the value of Mean anomaly:")) # Mean anomaly(radians)


# Solve Kepler's equation for hyperbolic orbits
E = kepler_hyperbolic(e, M)
print("Eccentric Anomaly (E):", E)






