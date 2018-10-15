def list_powers(n, m):
    "returns a list of squares"
    li = [] 
    for i in range(1, n+1):
        li.append(i**m)
    return li

for i in list_powers(4, 3):
    print(i)