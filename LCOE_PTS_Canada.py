import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.stats import norm
from scipy.stats import stats

np.random.seed(10)
random.seed(10)
n = 100000
#Iteration
LT = 30
#Lifetime
CC = 4811.24501
#Capital Cost
OM = 84.611844
#Operation & Maintenance Cost
IC = 14.4261
#Insurance Cost
LU = []
#Land Use
LP = []
#Land Price
SR =[]
#Solar Resource
MirA = []
#Mirror Area
CapF = []
#Capacity Factor
TurEf = 0.4
#Turbine Efficiency
DegF = 0.002
#Degradation Factor
DisR = 0.05
#Discount Rate
LCoE = []
#////////////////////////////////////////////////////

for i in range(n):
    LU.append(random.betavariate(0.984, 1.21)*33 + 19.5)

    LP.append(random.gammavariate(0.417, 2.83))

    CapF.append(random.uniform(0.35,0.41))

    SR.append(random.normalvariate(1450, 117))

    MirA.append(random.betavariate(6.35, 6.03)*4.68 + 8.11)

#///////////////////////////////////////////////////

for k in range(n):
    annual_cost = []
    revenue = []
    capital_cost = (CC + LU[k] * LP[k])
    for j in range(LT):
        annual_cost.append(((OM + IC) / pow((1 + DisR),j+1)))
        revenue.append((SR[k] * TurEf * MirA[k] * CapF[k] * pow((1 - DegF),j+1)) / pow((1 + DisR),j+1))
    Total_cost = capital_cost + sum(annual_cost[j] for j in range(LT))
    Total_revenue = sum(revenue[j] for j in range(LT))
    LCoE.append(1000*(Total_cost/Total_revenue))

file = open("Canada.txt", "w") 

for element in LCoE:
   file.write(str(element) + "\n")
file.close()

plt.hist(LCoE , color = "Orange" , range= [50,300])
plt.xlabel("LCOE($/MWh)")
plt.ylabel("Frequency")


median = np.median(LCoE)
mean = np.mean(LCoE)
print("Median of LCoE:", " ", median)
print("Mean of LCoE:" ," ", mean)

