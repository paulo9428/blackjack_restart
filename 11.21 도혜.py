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
        return self.deck
        
        
    def shuffle(self):
        
        new = self.deck
        random.shuffle(new)
        return new

    
    def pop_card(self):
        new1 = self.shuffle()
        
        for i in range(1,3):
            card = new1.pop(i)
            self.received_card.append(card)
        return self.received_card, new1
    
    def hit(self, received, new1):
                 ## hit 하는거                
        received.append(new1.pop(0))
        return received

class Sum:    
    score = []
    num = []
    def jqk_decision(self,f):
        for i in f:
            if 'J' or 'Q' or 'K' in i[1]:
                self.score.append(i[1:])
            
            else :
                self.score.append(i[1:])
            
        print (self.score)

    # def machine_hit(self):

    #     if Sum.make_score <= 17:
    #         self.hit()
    #     elif Sum.sum_result > 17:
    #         return dealer.received_card 
    
    sum_result = 0   
   
    def to_int(self):

        if 'A' in self.score:
            a_choice = input("A는 어떤 값으로 선택하시겠습니까? 1) 1 2) 11>> ")
        
        for i in self.score:
            if 'J' == i or 'Q' == i or 'K' == i:
                i = 10
                self.num.append(i)
            elif 'A' == i and a_choice == "1":
                i = 1
                self.num.append(i)
            elif 'A' == i and a_choice == "11":
                i = 11
                self.num.append(i)
            else :
                s = int(i)
                self.num.append(s)
        
        print(self.num)

        
    def make_score(self):

            print(sum(self.num))



while True :
    invite = input('게임에 참석하시겠습니까? (Yes / No)'+'\n')       ## 시작

    if invite == 'Yes' :

        player = Deck()
        dealer = Deck()
        finish = Sum()

        a = player.pop_card()
        b = dealer.pop_card()
        
        print("P>>>", a[0])
        print("D>>>", b[0])
        
    elif invite == 'No':
        print('>>>>>>>>>>>','다음에 만나요')
        break

    else :
        print("=============================================Error!!! 다시 입력해주세요.===============================")
        continue
    
    while True:                                                ## 둘째 턴 ~ 종료
        
        gesture = input('카드를 한장 받으시겠습니까? (Yes / No)' + '\n')

        if gesture == 'Yes':
            
            f = player.hit(a[0],a[1])

            print("P>>>", f)
            finish.jqk_decision(f)
            finish.to_int()
            finish.make_score()
           
        elif gesture == 'No':
            print("어쩌지")
            # No 하면 여기서 비교해서 승부 보기