def a(x):
    for i in range(len(x)-1,0,-1):
        for j in range(i):
            if x[j]>x[j+1]:
                temp = x[j]
                x[j]=x[j+1]
                x[j+1]=temp
angka = [3,1,4,2,8]
a(angka)
print(angka)