a = []

n = int(input("Enter the value of n: "))

for i in range(n):
    b = []
    for t in range(n):
        b.append(int(input()))
    a.append(b)
print(a)
