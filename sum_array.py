def sum_array(arr:list):
    if bool(arr) == True and len(arr)>2: 
        arr.sort()
        print(arr)
        arr.pop(0)
        arr.pop(-1)
        print(sum(arr))
    else:
        print('Пустота, меньше 3')

sum_array(None)
sum_array([])
sum_array([-3])
sum_array([-3,3])
sum_array([-6, -20, -1, -10, -12])

def top_sum_array(arr):
    return 0 if arr == None else sum(sorted(arr)[1:-1])
