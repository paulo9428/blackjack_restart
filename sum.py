import random


deck = []
shape = ["S","D","H","C"]
number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] # A, J, Q, K 정수화
for i in range (0,4):
    res_shape = shape[i]
    for n in range (0, 13):
        res_number = number[n]
        card = res_shape + res_number
        deck.append(card)

random.shuffle(deck)

a = deck.pop()
b = deck.pop()


my_list = [a,b]
print(my_list)

for card in my_list:
    sum += int(card[1,2])











