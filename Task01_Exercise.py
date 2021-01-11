
n = int(input())
curent = 1

for i in range(1, n+1):
    for x in range(1, n+1):
        print(curent, end=" ")
        curent += 1
        if x >= i:
            print()
            break
        if curent > n:
            break

    if curent > n:
        break