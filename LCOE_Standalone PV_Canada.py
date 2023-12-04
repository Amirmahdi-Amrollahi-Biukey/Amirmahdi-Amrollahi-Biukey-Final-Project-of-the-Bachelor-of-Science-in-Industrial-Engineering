import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.stats import norm
from scipy.stats import stats

np.random.seed(10)
random.seed(10)
n = 100000
#Iteration
LT = 25
#Lifetime
CC = 1085
#Capital Cost
OM = 0.015*CC
#Operation & Maintenance Cost
IC = 0.0025*CC
#Insurance Cost
LU = []
#Land Use
LP = []
#Land Price
SR =[]
#Solar Resource
PerFac = []
#Performance Factor
DegF = 0.005
#Degradation Factor
DisR = 0.05
#Discount Rate
LCoE = []
#////////////////////////////////////////////////////

for i in range(n):

    LU.append(random.normalvariate(19.1,5.9))

    LP.append(random.gammavariate(0.417, 2.83))

    SR.append(random.normalvariate(1530, 67.9))

    PerFac.append(random.betavariate(3.53, 1.54)*0.1 + 0.8)
#///////////////////////////////////////////////////

for k in range(n):
    annual_cost = []
    revenue = []
    capital_cost = (CC + LU[k] * LP[k])
    for j in range(LT):
        annual_cost.append(((OM + IC) / pow((1 + DisR),j+1)))
        revenue.append((SR[k] * PerFac[k] * pow((1 - DegF),j+1)) / pow((1 + DisR),j+1))
    Total_cost = capital_cost + sum(annual_cost[j] for j in range(LT))
    Total_revenue = sum(revenue[j] for j in range(LT))
    LCoE.append(1000*(Total_cost/Total_revenue))

positive_numbers = [num for num in LCoE if num >= 0]

file = open("Canada.txt", "w") 

for element in positive_numbers:
   file.write(str(element) + "\n")
file.close()

plt.hist(LCoE , color = "Orange" , bins = 50)
plt.title("The LCOE of Standalone PV Technology in Canada")
plt.xlabel("LCOE($/MWh)")
plt.ylabel("Frequency")


median = np.median(positive_numbers)
mean = np.mean(positive_numbers)
print("Median of LCoE:", " ", median)
print("Mean of LCoE:" ," ", mean)