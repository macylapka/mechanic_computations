import math

def get_pistone_stroke(r):
  return 2 * r

#cylinder capacity in dm^3
def get_cylinder_capacity(bore, pistone_stroke):
  return math.pi * math.pow(bore, 2) * pistone_stroke / \
         (4 * math.pow(10, 3))

def sum_of_the_capacity(cylinder_capacity, cylinder_count):
  return cylinder_capacity * cylinder_count

def total_capacity(cylinder_capacity, combustion_chamber_capacity):
    return cylinder_capacity + combustion_chamber_capacity

#epsylon
def compression_ratio(total_capacity, combustion_chamber_capacity):
    return total_capacity / combustion_chamber_capacity
