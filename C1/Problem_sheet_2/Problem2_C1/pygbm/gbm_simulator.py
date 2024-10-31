from Geometric_Brownian_motion import geometric_Brownian_motion

class GBMSimulator(geometric_Brownian_motion):
    def __init__(self, mu, sigma, y_0, T, N):
        super().__init__(mu, sigma,y_0)