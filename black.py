import random

class Deck:
    def shuffle_cards():
        deck = []
        shape = ["S","D","H","C"]
        number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for i in range (0,4):
            res_shape = shape[i]
            for n in range (0, 13):
                res_number = number[n]
                card = res_shape + res_number
                deck.append(card)
                random.shuffle(deck)          
        print (deck)
        
    def suffled_deck():
        
        deck = random.shuffle(deck)
        
    shuffle_cards()
    recieved_card = []


    start = input("게임에 참석하시겠습니까? (Usage: Yes / No)\n")
    if start == "Yes":
        suffled_deck()
        first_card = deck.pop(1)
        second_card = deck.pop(2)
        recieved_card = [first_card, second_card]
        print(recieved_card)
    
################################


