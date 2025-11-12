r1 = 0
r2 = 0
r3 = 0
fr = 0

for i in range(1, 101, 2):
    r1 += (i**2) + ((i+1)**2) #sum of squares
    print("Tests ", i**2, (i+1)**2)
    print("Results: ", r1)

for i in range(1, 101):
    r2 += i #square of sums

r3 = r2**2
fr = r3 - r1
print(r1, r3)
print(fr)
