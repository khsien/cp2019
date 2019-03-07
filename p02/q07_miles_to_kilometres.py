
def mlstokm(miles):
    km = miles * 1.609
    return "{0:.3f}".format(km)
def kmtomls(kilometres):
    miles = kilometres/1.609
    return "{0:.3f}".format(miles)
print("Miles",'\t','Kilometres','\t',"Kilometres",'\t',"Miles")
for i in range(1,11):
    print(str(i) + '\t ' + mlstokm(i) + '\t         ' + str(i*5+15) + '\t         ' + kmtomls(i*5+15))
