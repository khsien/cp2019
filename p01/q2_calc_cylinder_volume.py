
radius = int(input("Enter Radius Here:"))

length = int(input("Enter Length Here:"))

from math import pi

area = radius ** 2 * pi

volume = area * length

print("Volume is " + str(volume))
