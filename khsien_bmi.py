# get input
weight = float(input("Enter Weight(kg):"))
height = float(input("Enter Height(m):"))

# compute bmi
bmi = weight / (height*height)

# output result
print("BMI = {0:.2f}".format(bmi))
if bmi < 18.5:
    print("please eat more")
elif 18.5 <= bmi < 23:
    print("low risk")
elif 23 <= bmi < 27.5:
    print("Moderate risk")
else:
    print("high risk")
