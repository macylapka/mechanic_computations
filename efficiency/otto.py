import math
from efficiency import utils

def get_otto_efficiency(v1, v4, cp, cv):
  k       = get_k(cp, cv) 
  epsilon = get_epsilon(v1, v4)

  return 1 - (1 / math.pow(epsilon, k - 1)) 
