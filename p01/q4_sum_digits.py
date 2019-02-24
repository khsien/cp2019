
integer = int(input("Enter Integer:"))
a = integer % 10
b = integer // 10
c = b // 10 
d = b % 10
e = c // 10
f = c % 10

print("The sum of the digits are " + str( a + d + e + f) )
