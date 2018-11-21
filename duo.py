import random

class Deck:                                       ##instance 없이 쓰는 static method로 Deck.make_deck()
    

    def __init__(self):

        deck = []
        
        self.deck = deck
        
    
    def make_deck(self):                               ## deck 을 만든다
        
        shape = ["S","D","H","C"]
        number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
       
        for i in range (0,4):
            res_shape = shape[i]
            for n in range (0, 13):
                res_number = number[n]

                card = res_shape + res_number
                
                self.deck.append(card)
        
        return self.deck
        
        
    def shuffle(self):

        random.shuffle(self.deck)

        shuff_deck = self.deck
        
        

    
    def pop_card(self):
        
        new1 = self.shuffle()
        received_card = []
        
        for i in range(0,2):
            card = new1.pop(i)
            received_card.append(card)
        return received_card, new1
    
    def hit(self, received, new1):
                 ## hit 하는거                
        received.append(new1.pop(0))
        return received

class Sum:    
    
    score = []

    def jqk_decision(self,f):
        for i in f:
            if 'J' or 'Q' or 'K' in i[1]:
                self.score.append(i[1])
            
            else :
                self.score.append(i[1])
            
        print (self.score)

    def machine_hit(self):

        if Sum.make_score <= 17:
            self.hit()
        elif Sum.sum_result > 17:
            return dealer.received_card 
    
    sum_result = 0   

    def make_score(self):
        num = []
        for i in self.score:
            if 'J' == i or 'Q' == i or 'K' == i:
                i = 10
                num.append(i)
           
            else :
                s = int(i)
                num.append(s) 
        
        return sum(num)
        
            # else :
            #     i = int(i[1])

        # print (sum(self.score))       
            #         for i in self.received_card:
            
            # sum_result += int(i[1])
        
    # def plus_score(self):
    #     sum
    def a_decision():
        
        if i[1] == 'A' and sum_result + 11 > 21:
            a = i[1]
            a = 1
            d = a + sum_result
        elif i[1] == 'A' and sum_result + 11 < 21:
            a = i[1]
            a = 11
            d = a + sum_result  
             


while True :

                                                                                            ### deck을 섞는다

                                                                                            ## 딜러가 1장을 두번 받는다

                                                                                            ## 플레이어가 1장을 두번 받는다

                                                                                            ## 딜러의 첫번째 한장과 플레이어의 카드 전체를 보여준다

                                                                                            ##  카드를 한장 더 받으시겠습니까??

                                                                                            ## 예 -> 2번째줄            

                                                                                            ## 아니요 -> 딜러 17 이상일때까지 받는다 -> 승부를 낸다




    
    

    
