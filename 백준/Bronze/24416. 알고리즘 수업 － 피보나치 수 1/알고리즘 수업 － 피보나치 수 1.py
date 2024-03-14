N = int(input())
li = [1,1]
def fi(n):
    if n < 3:
        return n
    for i in range(2,n):
        li.append(li[i-1]+li[i-2])
fi(N)
print(li.pop(), N-2)