def getNthFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n<1:
        return "Incorrect input"
    else:
       return getNthFib(n-1) + getNthFib(n-2)              


n=int(input("Enter nth term: "))   
 
for i in range(n):
    print(getNthFib(i), end=' ')

