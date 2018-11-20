import random

class Deck:
    
    deck = []
    shape = ["S","D","H","C"]
    number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    
    
    
    def make_deck():                            ## deck 을 만든다
        
        for i in range (0,4):
            res_shape = shape[i]
            for n in range (0, 13):
                res_number = number[n]
                card = res_shape + res_number
                deck.append(card)
        
        

    
Deck().make_deck()