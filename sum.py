import random


deck = []
shape = ["S","D","H","C"]
number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] # A, J, Q, K 정수화


def make_deck():

for i in range (0,4):
    res_shape = shape[i]
    for n in range (0, 13):
        res_number = number[n]
        card = res_shape + res_number
        deck.append(card)

def shuffle():

    random.shuffle(deck)


def card_pop():

    card_pop = deck.pop()

    my_list = []
    my_list.append(card_pop)



def sum():
    
    sum_result = 0
    
    if i[1:2] == 'J', 'Q', 'K':
        int(i[1:2]) = 10

    for i in my_list:
        sum_result += int(i[1:2])


def a_decision():

    if i[1:2] == 'A' and sum_result > 21:
        
        int(i[1:2]) = 1

    elif i[1:2] == 'A' and sum_result =< 21:
        
        int(i[1:2]) = 10
        

















