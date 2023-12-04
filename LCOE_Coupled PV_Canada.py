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
CCpv = 1085
#Capital Cost
OMpv = 0.015*CCpv
#Operation & Maintenance Cost
ICpv = 0.0025*CCpv
#Insurance Cost
nd = 350
#Number of cycles in year
sizest = 60 * 4
#Storage Size(MWh)
CCst = 91848000
#Capital Cost
OMst = 1024704
#Operation & Maintenance Cost
ICst = 336960
#Insurance Cost
LUst = sizest * 30 / 4
#30 m2 per 4 MWh
#Land Use
LUpv = []
#Land Use
LP = []
#Land Price
SR =[]
#Solar Resource
PerFac = []
#Performance Factor
RTE = 0.9
#Round-Trip Efficiency
DegFst = 0.01
#Degradation Factor
DegFpv = 0.005
#Degradation Factor
A = 0.5
DisR = 0.05
#Discount Rate
LCoE = []
LCoS = []
LCoEpp = []
#////////////////////////////////////////////////////
#PV
for i in range(n):

    LUpv.append(random.normalvariate(19.1,5.9))

    LP.append(random.gammavariate(0.417, 2.83))

    SR.append(random.normalvariate(1530, 67.9))

    PerFac.append(random.betavariate(3.53, 1.54)*0.1 + 0.8)

for k in range(n):
    annual_costpv = []
    revenuepv = []
    annual_costst = []
    revenuest = []
    capital_costpv = (CCpv + LUpv[k] * LP[k])
    capital_costst = (CCst + LUst * LP[i])
    for j in range(LT):
        annual_costpv.append(((OMpv + ICpv) / pow((1 + DisR),j+1)))
        revenuepv.append((SR[k] * PerFac[k] * pow((1 - DegFpv),j+1)) / pow((1 + DisR),j+1))
        annual_costst.append((OMst + ICst) / pow((1 + DisR),j+1))
        revenuest.append((sizest * nd * RTE * pow((1 - DegFst),j+1)) / pow((1 + DisR),j+1))

    Total_costpv = capital_costpv + sum(annual_costpv[j] for j in range(LT))
    Total_revenuepv = sum(revenuepv[j] for j in range(LT))
    Total_costst = capital_costst + sum(annual_costst[j] for j in range(LT))
    Total_revenuest = sum(revenuest[j] for j in range(LT))
    
    LCoE.append(1000*(Total_costpv/Total_revenuepv))
    LCoS.append(Total_costst/Total_revenuest)
    LCoEpp.append(LCoE[k]*(1/(1-A*(1-RTE))) + LCoS[k]*((A*RTE)/(1-(A*(1-RTE)))))
positive_numberspv = [num for num in LCoE if num >= 0]
positive_numbersst = [num for num in LCoS if num >= 0]
positive_numberspp = [num for num in LCoEpp if num >= 0]

file = open("Canada.txt", "w") 

for element in positive_numberspp:
   file.write(str(element) + "\n")
file.close()

medianpv = np.median(positive_numberspv)
medianst = np.median(positive_numbersst)
meanpv = np.mean(positive_numberspv)
meanst = np.mean(positive_numbersst)
medianpp = np.median(positive_numberspp)
meanpp = np.mean(positive_numberspp)

print("Median of LCoE & LCoS & LCoEpp:", " ", medianpv," ",medianst, " ", medianpp)
print("Mean of LCoE & LCoS & LCoEpp:" ," ", meanpv, " ", meanst, meanpp)