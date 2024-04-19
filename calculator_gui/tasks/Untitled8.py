import math

def kepler_equation(e: float, M: float, tol=1e-9, max_iter=1000)-> float:
    # Initial guess for eccentric anomaly (E)
    E = M / e
    
    # using Newton's method
    for _ in range(max_iter):
        f = E - e * math.sin(E) - M
        f_prime = 1 - e * math.cos(E)
        g = f / f_prime
        E= E- g
        
        # Check for convergence
        if abs(g) < tol:
            return E
    

# Example usage
e = float(input("Enter the value of Eccentricity:" )) # Eccentricity 
M = float(input("Enter the value of Mean anomaly:")) # Mean anomaly(radians)


# Solve Kepler's equation 
E = kepler_equation(e, M)
print("Eccentric Anomaly (E):",E)






