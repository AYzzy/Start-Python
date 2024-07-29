#Promtr use to enter the radius of the cylinder and length of the cylinder
#To get area we will multiply the pi(3.142) against the radius raise to the power of 2
# To get the volume of the cylinder we will multiply the radius against length

import function1

radius = int(input("Enter the radius of the cylinder: "))
length = int(input("Enter the length of the cylinder: "))

total = area(radius)
total1 = volume(total,length) 

print('Been given that the area of the cylinder', total ,'and the length of the cylinder is ', length, ',The volume of the cylinder is ',total1)