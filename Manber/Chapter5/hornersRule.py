def hornersRule(l, x):

    size = len(l)
    P = l[size - 1]
    
    for i in range(1, size):
        P = P*x + l[size - 1 - i]
    
    return P
