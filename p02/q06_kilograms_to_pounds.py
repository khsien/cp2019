
def pounds(mass):
    p = mass * 2.2
    return p
print("Kilograms" + '\t' + "Pounds")
for i in range(1,11):
    print(i, "\t       " ,"{0:.1f}".format(pounds(i)))
