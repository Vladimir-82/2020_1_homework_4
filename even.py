def prog(some_list):
    even_list=[]
    for i in some_list:
        if i%2==0:
            even_list.append(i)
        if i==237:
            break
    return even_list
N=int(input("Enter a size:"))
somelist=[0]*N

for k in range(N):
    somelist[k]=int(input("enter a numbers:"))

print(prog(somelist))