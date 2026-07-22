## Quantum States 

### Superposition & Measurement

import numpy as np 
import matplotlib.pyplot as plt 



class System: 
    
    def __init__(self, spin, _appa):
        self.spin = spin 
        self.appa = _appa

    def normalization(): 
        pass

    def measure(two_state, state, bias):

        H = [1,0] 
        T = [0,1]
        two_state = (H, T)

        pauli_comp = np.mathmul(two_state)

        ### How do I want to structure this function? This current code will be deleted below
        for b in bias:
            if spin == -1: 
                b = np.matmul(b, T)
            else: 
                print(pauli_comp)
    
        print(pauli_comp)
        ## until ---- 
    def expectation(spin):

        pass

    def outcomes(): 

        ## histograms of theoretical probs.
        pass
















if __name__ == "__main__":
    State(any)

    pass

