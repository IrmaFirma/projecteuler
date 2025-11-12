n = int(input())
arr = []

for i in range(n):
    i = int(input("Enter element: "))
    arr.append(i)


max = arr[0]

for i in arr:
    if i > max:
        max = i

#remove all duplicates of max
i = max

while i in arr:
    arr.remove(i)

runner_up = arr[0]

for i in arr:
    if i > runner_up:
        runner_up = i

print(runner_up)
