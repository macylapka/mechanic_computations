import utils 

def maclaurin_factor(n):
  return math.pow(-1, n) * math.factorial(2 * n) / \
         ((1 - 2 * n) * math.pow(math.factorial(n), 2) * math.pow(4, n))


def maclaurin_series(x, number):
  
  result = 0.0
  for n in range(0, number + 1):
      result += (maclaurin_factor(n) * math.pow((-1.0 * x), n))
    
  print("result = %f" % (result)) 
  return result

