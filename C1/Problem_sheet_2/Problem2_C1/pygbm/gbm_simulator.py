from Geometric_Brownian_motion import geometric_Brownian_motion
import numpy as np

class GBMSimulator(geometric_Brownian_motion):
    """

    This class is the daughter of geometric_Brownian_motion instance and is going to calculate analytically the Geometric Brownian motion. 
    It's going to be componed by the coeficient function, the Brownian_motion, and the simulate_path function.

    """

    def __init__(self, mu, sigma, y_0):
        """
        Initialize a GBMSimulator, duaghter of geometric_Brownian_motion instance.

        Parameters:
        - mu (float): drift coefficient.
        - sigma (float): diffusion coefficient.
        - y_0 (float): point in t=0
        """
        super().__init__(mu, sigma,y_0)


    def coeficient(self):
        return self.mu - (self.sigma**2)/2

    def Brownian_motion(self, T, N):
        """
        This functions calculates the Brownian Motion factor for every step.  Delta t : W(t+Delta t)-W(t) \sim N(0,Delta t); where W(0)=0
        so, the standard desviation is sqrt(Delta t).

        Parameters:
        - T : total time 
        - N : number of steps
        """
        dt = T/N
        Bmlist = [0] # Always strats at 0
        seed = 29072000

        for n in range(1,N):
            # Brownian increments
            dW = np.sqrt(dt) * np.random(seed)
            # Brownian path (cumulative sum of increments)
            Bmlist.add(Bmlist[n-1]+dW)

        return Bmlist
    
    def simulate_path(self,T,N):
        Bmlist = GBMSimulator.Brownian_motion(T, N)
        coef = GBMSimulator.coeficient()
        t = np.linspace(0,T,N)
        y_t = self.y_0*np.exp(coef*t+self.sigma*Bmlist)
        
        return t, y_t
    





