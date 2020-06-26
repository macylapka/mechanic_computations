import math

def f1(R, L, alfa):
  return math.pow((R / L), 2) * math.pow(math.sin(math.radians(alfa)), 2)

#------------------------------------------------------------------------------
#                            Angular velocity
#                            Prędkośc kątowa
#------------------------------------------------------------------------------
#fi in radians
def angular_velocity(d_fi, d_t):
  return d_fi/d_t

#fi in degrees
def angular_velocity_deg(d_fi, d_t):
  return angular_velocity(math.radians(d_fi), d_t)

#------------------------------------------------------------------------------
#                            Angular acceleration
#                            Przyśpieszenie kątowe
#------------------------------------------------------------------------------
def angular_acceleration(d_omega, d_t):
    return d_omega / d_t

#------------------------------------------------------------------------------
#                            Area of a circle
#                            Pole koła
#------------------------------------------------------------------------------
def area_of_a_circle_m(r):
  return math.pi * math.pow(r, 2)

#------------------------------------------------------------------------------
#                            Circumference of a circle
#                            Obwód koła
#------------------------------------------------------------------------------
def circumference_of_a_circle_m(r):
  return 2 * math.pi * r
