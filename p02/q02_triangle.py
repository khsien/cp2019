
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if (a + b <= c) or (b + c <= a) or (a + c <= b):
    print("invalid triangle")
else:
    print("Perimeter = " + str(a+b+c))
