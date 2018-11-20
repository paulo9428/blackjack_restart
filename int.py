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

class Sum:

    a = 11

    def a_decision():

       
        if i[1] == 'A' and sum_result + a > 21:               ## A의 숫자를 정한다                   
            
            i[1] = 1

        elif i[1] == 'A' and sum_result + a <= 21:
            
            i[1] = 11
            
    def jqk_decision():

        if i[1] == 'J' or i[1] == 'Q' or i[1] == 'K':
            
            i[1] = 10

    def sum(self):
        
        sum_result = 0
        
        for i in self.received_card:
            sum_result += i[1]

        print(sum_result)

sum1 = Sum()
sum1.sum()

    
