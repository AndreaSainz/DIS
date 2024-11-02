from pygbm.Geometric_Brownian_motion import GeometricBrownianMotion
import numpy as np

class GBMSimulator(GeometricBrownianMotion):
    r"""

    This class is the daughter of geometric_Brownian_motion instance and is going to calculate analytically the Geometric Brownian motion. 
    It's going to be componed by the coeficient function, the Brownian_motion, and the simulate_path function.

    """

    def __init__(self, mu, sigma, y_0):
        r"""
        Initialize a GBMSimulator, duaghter of geometric_Brownian_motion instance.

        Parameters:
        - mu (float): drift coefficient.
        - sigma (float): diffusion coefficient.
        - y_0 (float): point in t=0
        """
        super().__init__(mu, sigma,y_0)


    def coeficient(self):
        return self.mu - 0.5 *(self.sigma**2)

    @staticmethod
    def Brownian_motion(T, N):
        
        r"""
        This functions calculates the Brownian Motion factor for every step.  Delta t : W(t+Delta t)-W(t) \sim N(0,Delta t); where W(0)=0
        so, the standard desviation is sqrt(Delta t).

        Parameters:
        - T : total time 
        - N : number of steps
        """
        np.random.seed(29072000)
        dt = T / N  
        dW = np.sqrt(dt) * np.random.normal(size= N-1) # N-list with N(0,dt)
        dW = np.insert(dW, 0, 0)
        Bmlist = np.cumsum(dW)  # Accumulative sum
        return Bmlist
    
    
    def simulate_path(self,T,N):
        Bmlist = GBMSimulator.Brownian_motion(T, N)
        coef = self.coeficient()
        t = np.linspace(0,T,N)
        y_t = self.y_0 *np.exp(coef*t+self.sigma*Bmlist)
        return t, y_t
    





