n = int(input())
l = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        for x in range(1, l+1):
            for y in range(1, l+1):
                for z in range(1, n+1):
                    if z > i and z > j:
                        password = str(i) + str(j) + chr(96 + x) + chr(96 + y) + str(z)
                        print(password, end=" ")
