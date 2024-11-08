import numpy as np

class GBMSimulator:

    def __init__(self, y_0, mu, sigma):
        self.y_0 = y_0
        self.mu = mu
        self.sigma = sigma

    def simulate_path(self,T, N):
        t = np.linspace(0,T,N)
        y = np.zeros([1,N])
        time_interval = T/N
        y[0][0] = self.y_0

        for i in range(1,N):
            y[0][i] = y[0][i-1] * (1 + self.mu * time_interval + self.sigma * np.random.normal(0, time_interval, 1))
        
        return t,y