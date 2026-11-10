n = 7

for i in range(n):
    for j in range(n):
        print(max(abs(i - 3), abs(j - 3)) + 1, end=" ")
    print()
