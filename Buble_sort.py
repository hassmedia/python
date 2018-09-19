def Buble_sort(alist):
    for i in range(0,len(alist)):
        for j in range(0,len(alist)-1-i):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1] = alist[j+1], alist[j]
    return alist
chaine=[1,5,0,9,4,6,3,10,45,23]
print Buble_sort(chaine)