T=[7,992438,1006399,781139,985280,4729,872779,563580]
if __name__='__main__':
    total=T.pop(0)
    alice=0
    bob=0
    while total!=0:
        if alice==0 and bob==0:
            num=max(T)
            alice=alice^num
            T.remove(num)
        
