def list_squares(n):
    "returns a list of squares"
    li = [] 
    for i in range(1, n+1):
        li.append(i**2)
    return li

print(__name__)

if __name__ == "__main__":
    for i in list_squares(4):
        print(i)