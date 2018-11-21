import random

class Deck:                                       ##instance 없이 쓰는 static method로 Deck.make_deck()
    
 
    deck = []

    received_card = []

    def __init__(self):
        print ("good")
    
    def make_deck(self):                               ## deck 을 만든다
        
        shape = ["S","D","H","C"]
        number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for i in range (0,4):
            res_shape = shape[i]
            for n in range (0, 13):
                res_number = number[n]

                card = res_shape + res_number
                
                self.deck.append(card)
        print(self.deck)
        
        
    def shuffle(self):
        random.shuffle(self.deck)
        print(self.deck)
    
    def pop_card(self):
        # received_card = [] 여기 있었더니 구동 안 됨.....
        for i in range(2):
        
            self.received_card.append(self.deck.pop(0))
       
        print(self.received_card)

    def hit(self):

        self.received_card.append(self.deck.pop(0))        # [list].append("aa") append함수는 return값 없음 -> print(list)해야 함. [list].sort도 마찬가지

        print(self.received_card)


card= Deck()
card.make_deck()
card.shuffle()
card.pop_card()
card.hit()
