import random

class Deck:                                       ##instance 없이 쓰는 static method로 Deck.make_deck()
    

    def __init__(self):
        print ("good")
    
    def make_deck(self):                               ## deck 을 만든다
        deck = []
        shape = ["S","D","H","C"]
        number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for i in range (0,4):
            res_shape = shape[i]
            for n in range (0, 13):
                res_number = number[n]

                card = res_shape + res_number
                
                deck.append(card)
        return deck
        
        
    def shuffle(self):
        new = self.make_deck()
        random.shuffle(new)
        return new

    
    def pop_card(self):
        new1 = self.shuffle()
        received_card = []
        for i in range(1,3):
            card = new1.pop(i)
            received_card.append(card)
            
        print(received_card)


item = Deck()
item.pop_card()