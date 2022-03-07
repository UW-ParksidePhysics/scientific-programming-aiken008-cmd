STANDARD_GRAVITY = 9.80665      # m/s/s
INITIAL_VELOCITY = 15.          # km/h
LAUNCH_ANGLE = 60.              # °
HORIZONTAL_RANGE = 0.5          # m
INITIAL_HEIGHT = 1.             # m

print(f'v0 = {INITIAL_VELOCITY:.1f} km/h')
print(f'theta = {LAUNCH_ANGLE:.0f} °')
print(f'x = {HORIZONTAL_RANGE:.1f} m')
print(f'y0 = {INITIAL_HEIGHT:.1f} m')

from math import pi, tan, cos

# Convert initial velocity to m/s
INITIAL_VELOCITY = INITIAL_VELOCITY * 3600/1000
# Convert angle to radians
LAUNCH_ANGLE = LAUNCH_ANGLE * pi/180

height = HORIZONTAL_RANGE * tan(LAUNCH_ANGLE) - 1/(2 * INITIAL_VELOCITY**2) *\
 STANDARD_GRAVITY * HORIZONTAL_RANGE**2/((cos(LAUNCH_ANGLE))**2) + INITIAL_HEIGHT
print(f'y	= {height:.1f} m')
