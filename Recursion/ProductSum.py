l = [5,2,[7,-1]]

def ProductSum(l,mul = 1):
    prodsum = 0
    for i in l:
        if type(i) is list:
            prodsum+=ProductSum(i,mul+1)
        else:
            prodsum+=i
    return prodsum*mul

ProductSum(l)            