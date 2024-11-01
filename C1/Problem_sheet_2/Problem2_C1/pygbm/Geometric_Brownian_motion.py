class geometric_Brownian_motion:
    def __init__(self, mu, sigma, y_0):
        r"""
        Initialize a Geometric_Brownian_motion instance.

        Parameters:
        - mu (float): drift coefficient.
        - sigma (float): diffusion coefficient.
        - y_0 (float): point in t=0
        """
        self.mu = mu
        self.sigma = sigma
        self.y_0 = y_0

    
    
    