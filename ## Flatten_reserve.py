## Flatten

flatten = lambda *n: (e for a in n
    
    for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))

q1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print (list(flatten(q1)))


# Reserve 

def deep_rev(L):
    L[:] = [list(reversed(row)) for row in reversed(L)]

L = [[1, 2], [3, 4], [5, 6, 7]]
deep_rev(L)
print(L)