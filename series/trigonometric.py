import math 
from utils import factorial

def trigonometric_factor(n):
  return math.pow(-1, n) / (factorial.factorial(2 * n))


def trigonometric_series(x, number):
    
  result = 0.0
  for n in range(0, number):
    step = trigonometric_factor(n) * math.pow(-1 * x, 2 * n)
    print("result = %f + %f = %f" % (result, step, result + step))
    result += step
        
  return result
