# TODO implement mergesort


def mergesort(list: list, left =0, right= -1) -> list:
    
    if right == -1:
        right = len(list) -1
    if right > left:
        middle = int(left + (right - left) / 2)
        
        mergesort(list, left, middle)
        mergesort(list, middle+1, right)
        return merge(list,left,middle,right)
        
def merge(list, left, middle, right):
    
    n1 = middle - left + 1
    n2 = right - middle
    
    left_lst = [None] * n1
    right_lst = [None] * n2
    
    for i in range(n1):
        left_lst[i] = list[left + i]
    
    for j in range(n2):
        right_lst[j] = list[middle + 1 + j]
        
    i = 0
    
    j = 0
    
    k = left
    
    while i < n1 and j < n2:
        if left_lst[i] <= right_lst[j]:
            list[k] = left_lst[i]
            i += 1
        else:
            list[k] = right_lst[j]
            j += 1
        k += 1
    
    while i < n1:
        list[k] = left_lst[i]
        i+=1
        k+=1
    while j < n2:
        list[k] = right_lst[j]
        j+=1
        k+=1
    return list