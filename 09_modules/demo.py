# importing of module
 
# 1 st appraoach -----> Whole module
import math
print(math.sqrt(25)) #5.0

#2nd approach ---------> specific functinolity in module
from math import sqrt
print(sqrt(25)) #5.0

# optinol ---> can use alias names as well for easy readability
import math as m
print(m.sqrt(25)) #5.0