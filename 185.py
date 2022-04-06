# num=int(input())
# l=list(map(int,input().split(' ')))
#
# for i in range(num):
#    while(l[0:i].count(l[i])>0):
#        l[i]+=1
# for i in l:
#    print(i,end=' ')
#    

num = int(input())
l = list(map(int, input().split(' ')))
p = [i for i in range(1000000)]


def find(x):
    if p[x] == x:
        return p[x]
    p[x]=find(p[x])
    return p[x]


for i in range(num):
    l[i] = find(p[l[i]])
    p[l[i]] = find(p[l[i]+1])

for i in range(num):
    print(l[i], end=' ')
