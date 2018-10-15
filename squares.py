def list_powers(n, m):
    "returns a list of squares"
    li = [] 
    for i in range(1, n+1):
        li.append(i**m)
    return li

print(__name__)

if __name__ == "__main__":
    for i in list_powers(4, 3):
        print(i)
