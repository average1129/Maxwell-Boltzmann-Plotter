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
    # Data for the first graph
    C0_2_prob_distribution_160K = maxwell_boltzmann_distribution_function(CO2_m,160,1200)    
    C0_2_prob_distribution_270K = maxwell_boltzmann_distribution_function(CO2_m,270,1200)
    C0_2_prob_distribution_300K = maxwell_boltzmann_distribution_function(CO2_m,300,1200)
    C0_2_prob_distribution_2000K = maxwell_boltzmann_distribution_function(CO2_m,2000,1200)

    x = [] 
    for v_i in range(0,1200,5):
        x.append(v_i)
    
    # Set up the figure
    
    plt.figure(figsize=(10,6))
    # Plot the first set of three plots on the first graph
    plt.plot(x, C0_2_prob_distribution_160K, color='blue', marker='o', linestyle='-', label='CO2 160 K ')
    plt.plot(x, C0_2_prob_distribution_270K, color='orange', marker='s', linestyle='--', label='CO2 270K')
    plt.plot(x, C0_2_prob_distribution_300K, color='green', marker='s', linestyle='--', label='CO2 300K')
    plt.plot(x, C0_2_prob_distribution_2000K, color='red', marker='x', linestyle='-.', label='CO2 2000K')
    plt.title('Maxwell Boltzmann Distribution for CO2 at varying temperatures')
    plt.xlabel('Particle Velocity (m/s)')
    plt.ylabel('Fraction of Molecules')
    plt.legend()


    
    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
