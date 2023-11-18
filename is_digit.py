def is_digit(s:str)-> bool:
    try:
        float(s)
        return True 
    except ValueError:
        return False
print(is_digit('s2    '))
