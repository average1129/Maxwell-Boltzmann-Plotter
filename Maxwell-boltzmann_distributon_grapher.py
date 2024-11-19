import math 
import numpy as np
import matplotlib.pyplot as plt 

# Defining constants 

# Boltzmann's constant k 
k = 1.380649e-23 
#molecular mass of CO2 in kg 
CO2_m = 44.01e-26 
# Molecular mass of Nitrogen (N2) in kg 
N2_m = 4.65e-26
#Molecular mass of Helium (He) in kg
He_m = 6.64e-27
#Molecular mass of Hydrogen in kg 
H_m = 1.67e-27

##
## Inputs : m (float) in , T (float) in Kelvin , v (array of velocities)
##
def maxwell_boltzmann_distribution_function(m,T, v_range):
    v = np.arange(0, v_range, 5)
    distribution= ((4*np.pi*((m/(2*np.pi*k*T))**1.5)*(v**2)*np.exp((-m*(v**2))/(2*k*T))))
    #print (distribution)
    distribution = distribution.tolist()
    #print (distribution)
    return distribution 

def main():
    # Data for the second graph
    
    _3N2_prob_distribution_300K = maxwell_boltzmann_distribution_function(3*N2_m,300,5000)
    He_prob_distribution_300K = maxwell_boltzmann_distribution_function(He_m,300,5000)
    H_prob_distribution_300K = maxwell_boltzmann_distribution_function (H_m,300,5000) 


    x = [] 
    for v_i in range(0,5000,5):
        x.append(v_i)
    
    # Plot the second set of three plots on the second graph
    plt.figure(figsize=(10,6))
    plt.plot(x, _3N2_prob_distribution_300K, color='purple', marker='o', linestyle='-', label='3*N2 300K')
    plt.plot(x, He_prob_distribution_300K, color='orange', marker='s', linestyle='--', label='He 300K ')
    plt.plot(x, H_prob_distribution_300K, color='brown', marker='x', linestyle='-.', label='H 300K ')
    plt.title('Maxwell Boltzmann Distribution for Varying Atomic Species at 300 K')
    plt.xlabel('Particle Velocity (m/s)')
    plt.ylabel('Fraction of Molecules')
    plt.legend()

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()


