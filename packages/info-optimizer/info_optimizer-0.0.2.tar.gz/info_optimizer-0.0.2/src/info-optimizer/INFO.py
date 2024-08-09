import numpy as np  
import math  
import time  
from random import randint  

class Solution:  
    def __init__(self):  
        self.startTime = None  
        self.endTime = None  
        self.executionTime = None  
        self.convergence = None  
        self.optimizer = None  
        self.BestCost = None  
        self.Best_X = None  

def INFO(lb, ub, dim, nP, MaxIt, fobj):  
    Best_X = np.zeros(dim)  
    Best_Cost = float("inf")  
    Convergence_curve = np.zeros(MaxIt)  

    s = Solution()  
    timerStart = time.time()  
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")  

    Cost = np.zeros(nP)  
    M = np.zeros(nP)  
    W = np.zeros(3)  
    New_Cost = np.zeros(nP)  
    X = np.random.uniform(0, 1, (nP, dim)) * (ub - lb) + lb  

    for i in range(nP):  
        Cost[i] = fobj(X[i, :])  
        M[i] = Cost[i]  

    Ind = np.argsort(Cost)  
    Best_X = X[Ind[0], :]  
    Best_Cost = Cost[Ind[0]]  

    for it in range(MaxIt):  
        alpha = 2 * math.exp(-4 * it / MaxIt)  

        M_Best = Best_Cost  # M_Best is a scalar  

        for i in range(nP):  
            dl = 2 * np.random.rand() * alpha - alpha  
            sigm = 2 * np.random.rand() * alpha - alpha  

            a, b, c = np.random.choice(list(set(range(nP)) - {i}), 3, replace=False)  
            e = 1e-25  
            epsi = e * np.random.rand()  

            omg = max([M[a], M[b], M[c]])  # max of the M array  
            MM = [  
                (M_Best - M[a]),   
                (M_Best - M[b]),   
                (M_Best - M[c])  
            ]  

            W[0] = (math.cos(MM[0] + math.pi)) * math.exp(-abs(MM[0] / omg))  
            W[1] = (math.cos(MM[1] + math.pi)) * math.exp(-abs(MM[1] / omg))  
            W[2] = (math.cos(MM[2] + math.pi)) * math.exp(-abs(MM[2] / omg))  
            Wt = sum(W)  

            WM1 = dl * (W[0] * (X[a, :] - X[b, :]) + W[1] * (X[a, :] - X[c, :]) + W[2] * (X[b, :] - X[c, :])) / (Wt + 1) + epsi  

            # Second set of calculations  
            MM2 = [  
                (M_Best - M_Best),  
                (M_Best - M_Best),  
                (M_Best - M_Best)  
            ]  

            W[0] = (math.cos(MM2[0] + math.pi)) * math.exp(-abs(MM2[0] / 1e-10))  
            W[1] = (math.cos(MM2[1] + math.pi)) * math.exp(-abs(MM2[1] / 1e-10))  
            W[2] = (math.cos(MM2[2] + math.pi)) * math.exp(-abs(MM2[2] / 1e-10))  
            Wt = sum(W)  

            WM2 = dl * (W[0] * (Best_X - Best_X) + W[1] * (Best_X - Best_X) + W[2] * (Best_X - Best_X)) / (Wt + 1) + epsi  
            
            r = np.random.uniform(0.1, 0.5)  
            MeanRule = r * WM1 + (1 - r) * WM2  

            if (np.random.rand() < 0.5):  
                z1 = X[i, :] + sigm * (np.random.rand() * MeanRule) + np.random.randn() * (Best_X - X[a, :]) / (M_Best - M[a] + 1)  
                z2 = Best_X + sigm * (np.random.rand() * MeanRule) + np.random.randn() * (X[a, :] - X[b, :]) / (M[a] - M[b] + 1)  
            else:  
                z1 = X[a, :] + sigm * (np.random.rand() * MeanRule) + np.random.randn() * (X[b, :] - X[c, :]) / (M[b] - M[c] + 1)  
                z2 = Best_X + sigm * (np.random.rand() * MeanRule) + np.random.randn() * (X[a, :] - X[b, :]) / (M[a] - M[b] + 1)  

            u = np.zeros(dim)  
            for j in range(dim):  
                mu = 0.05 * np.random.randn()  
                if (np.random.rand() < 0.5):  
                    if (np.random.rand() < 0.5):  
                        u[j] = z1[j] + mu * abs(z1[j] - z2[j])   # Use z1  
                    else:  
                        u[j] = z2[j] + mu * abs(z1[j] - z2[j])   # Use z2  
                else:  
                    u[j] = X[i, j]  # Retain current solution  
            
            # Local search stage  
            if (np.random.rand() < 0.5):  
                L = np.random.rand() < 0.5  
                v1 = (1 - L) * 2 * (np.random.rand()) + L                # Eqs. (11.5) & % Eq. (11.6)  
                v2 = np.random.rand() * L + (1 - L)  

                Xavg = (X[a, :] + X[b, :] + X[c, :]) / 3   # Eq. (11.4)  
                phi = np.random.rand()  
                Xrnd = phi * (Xavg) + (1 - phi) * (phi * Best_X + (1 - phi) * Best_X)  # Corrected to use Best_X  

                Randn = L * np.random.randn(1, dim) + (1 - L) * np.random.randn()  
                if (np.random.rand() < 0.5):  
                    u = Best_X + Randn * (MeanRule + np.random.randn() * (Best_X - X[a, :]))  # Eq. (11.1)  
                else:  
                    u = Xrnd + Randn * (MeanRule + np.random.randn() * (v1 * Best_X - v2 * Xrnd))  # Eq. (11.2)  

            # Ensure New_X is shaped correctly  
            New_X = np.clip(u, lb, ub)  # Clip values to ensure they are within bounds  
            
            # Ensure the objective function returns a scalar  
            new_cost_value = fobj(New_X)  # This should return a scalar  
            if np.ndim(new_cost_value) != 0:  
                raise ValueError("Objective function must return a scalar value.")  

            New_Cost[i] = new_cost_value  # Assign the scalar cost value to New_Cost[i]  
                         
            if (New_Cost[i] < Cost[i]):  
                X[i, :] = New_X  
                Cost[i] = New_Cost[i]  
                M[i] = Cost[i]  
                if Cost[i] < Best_Cost:  
                    Best_X = X[i, :]  
                    Best_Cost = Cost[i]  

        Ind = np.argsort(Cost)  
        
        # Determine the worst solution  
        Worst_X = X[Ind[nP-1], :]  
        Worst_Cost = Cost[Ind[nP-1]]  
        
        # Determine the better solution  
        I = randint(2, 5)  
        Better_X = X[Ind[I], :]  
        Better_Cost = Cost[Ind[I]]  
        
        # Update Convergence_curve  
        Convergence_curve[it] = Best_Cost  
        
        # Show Iteration Information  
        print(f'It : {it}, BestCost : {Best_Cost}')   

    timerEnd = time.time()  
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")  
    s.executionTime = timerEnd - timerStart  
    s.convergence = Convergence_curve  
    s.optimizer = "INFO"   
    s.BestCost = Best_Cost  
    s.Best_X = Best_X  
    return s



