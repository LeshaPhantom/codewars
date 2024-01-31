def how_much_i_love_you(nb_petals:int):
    phrase = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all'] 
    return phrase[(nb_petals % 6) -1] if nb_petals > 6 else phrase[nb_petals-1]

print(how_much_i_love_you(337))
print(how_much_i_love_you(433))
print(how_much_i_love_you(6))

def top_how_much_i_love_you(nb_petals:int):
    return ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all'][nb_petals % 6 - 1] 

