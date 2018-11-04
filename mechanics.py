import sys
sys.path.append('./utils')

import utils
import math

from series   import maclaurin
from capacity import engine_capacity


def pistone_stroke(R, L, alfa, beta):
  return R + L - (R * math.cos(math.radians(alfa)) + L * math.cos(math.radians(beta)))


def pistone_stroke_2(R, L, alfa):
 return R * ((1 - math.cos(math.radians(alfa))) + ((R / L) / 4 * (1 - math.cos(math.radians(2 * alfa)))))

def main(): 
  print("pistone_stroke = %f" % pistone_stroke(50, 25, 20, 10))
  print("pistone_stroke_2 = %f" % pistone_stroke_2(50, 25, 20)) 

if __name__ == "__main__":
  main()
