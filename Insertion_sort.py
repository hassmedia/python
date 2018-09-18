def insert_sort(alist):
    for i in range(1,len(alist)):
        current_val = alist[i]
        position = i
        while position > 0 and current_val < alist[position-1]:
            alist[position] = alist[position-1]
            position -=1
        alist[position] = current_val
    return alist
chaine =[5,0,4,3,10,8,17]
print insert_sort(chaine)



