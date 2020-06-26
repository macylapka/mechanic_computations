import sys
import utils
import math
import series.maclaurin
import capacity.engine_capacity


def piston_stroke(R, L, alfa, beta):
  return R + L - (R * math.cos(math.radians(alfa)) + L * math.cos(math.radians(beta)))

def piston_stroke_2(R, L, alfa):
 return R * ((1 - math.cos(math.radians(alfa))) + ((R / L) / 4 * (1 - math.cos(math.radians(2 * alfa)))))

def main():
  print("Enter main")
  print("piston_stroke   = %f" % piston_stroke(50, 25, 20, 10))
  print("piston_stroke_2 = %f" % piston_stroke_2(50, 25, 20)) 
  print("Leave main")

if __name__ == "__main__":
  main()
