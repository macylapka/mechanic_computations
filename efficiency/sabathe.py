import math
from efficiency import utils

def get_sabathe_efficiency(p1, p5, v1, v2, v4, cp, cv):
  k       = get_k(cp, cv)
  alfa    = get_alfa(p1, p5)
  fi      = get_fi(v1, v2)
  epsilon = get_epsylon(v1, v4)

  return 1 - (alfa * math.pow(fi, k) - 1) / \
         (math.pow(epsilon, k - 1) * ((alfa - 1) + \
         k * alfa * (alfa - 1))
