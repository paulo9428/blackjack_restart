import random


deck = []
shape = ["S ","D ","H ","C "]
number = ["2","3","4","5","6","7","8","9","10"]
for i in range (0,4):
    res_shape = shape[i]
    for n in range (0, 9):
        res_number = number[n]
        card = res_shape + res_number
        deck.append(card)
        random.shuffle(deck)          
print(deck)





result = 0
my_card = []
for i in range(1,3):
    card = deck.pop(i)
    a = card.split(' ')
    my_card.append(card)

for res in my_card:
    a = res.split(' ')
    result += int(a[1]) 

