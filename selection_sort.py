def selection_sort(alist):
    for i in range(0,len(alist)-1):
      # min_val = alist[i]
       minIndex = i
       for j in range(i+1,len(alist)):
           if alist[j] < alist[minIndex]:
               minIndex = j

       if minIndex != i :
            alist[i]= alist[i+1]
            alist[i+1]= alist[i]



    return alist

chaine = [1,5,6,10,9,4,2]
print selection_sort(chaine)

