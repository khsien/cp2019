
sscore = {}
def grades(name, score):
    sscore[name] = score
students = int(input("Enter Number of Students Here:"))
x = 0
while x < students:
    n = input("Name: ")
    s = input("Score: ")
    grades(n,s)
    x = x + 1
print(max(sscore))
sscore.pop(max(sscore))
print(max(sscore))
