def isValid(formul:list)->bool:
    print(formul)
    if 7 in formul or 8 in formul:
        if 1 in formul and 2 in formul or 3 in formul and 4 in formul:
            return False
        if 5 in formul and 6 in formul or 5 not in formul and 6 not in formul:
            return True
    return False
print(f'{isValid([1,3,7])}')
print(f'{isValid([7,1,2,3])}')
print(f'{isValid([1,3,5,7])}')
print(f'{isValid([1,5,6,7,3])}')
print(f'{isValid([7,8])}')

