import random

class Deck:                                       
    
    def __init__(self):
        self.deck = []
    
    def make_deck(self):                               ## deck 을 만든다
        shape = ["S","D","H","C"]
        number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        
        for i in range (0,4):
            res_shape = shape[i]
            for n in range (0, 13):
                res_number = number[n]

                card = res_shape + res_number
                self.deck.append(card)
                
    
    def shuffle(self):                                 ## deck 을 섞는다

        random.shuffle(self.deck)
        
        
###########---------------------------------------------------------------

class Participant:
    
    def __init__(self):
        self.received_card = []

    def sum(self):
        self.sum_result = 0

        for i in self.received_card:                                            
            if i[1] == 'J' or  i[1] =='Q' or  i[1] =='K':                      #### j,q,k 결정
                self.sum_result += 10
            elif i[1] == 'A' and self.sum_result + 11 > 21:                    ### a 결정
                self.sum_result += 1
            elif i[1] == 'A' and self.sum_result + 11 <= 21:
                self.sum_result += 11
            else: 
                self.sum_result += int(i[1:])                                   ## 문자열 숫자를 정수화해서 더해준다
                
    
    def double_hit(self):                   ## 2장 hit 하는 것
        for i in range(0,2):
            card = deck.deck.pop()            
            self.received_card.append(card)
        
    def hit(self):                             ## 1장 hit 하는거
        card = deck.deck.pop()
        self.received_card.append(card)
        
class Player(Participant):

    def __init__(self):
        super().__init__() 
        self.name = 'player'

class Dealer(Participant):
    
    def __init__(self):
        super().__init__() 
        self.name = 'dealer'

    def machine_hit(self):

        while self.sum_result < 17:
            self.hit()

def decide_result():

    # 둘다 21 초과
    if player.sum_result > 21 and dealer.sum_result > 21:
        print("Play again!")
    
    # 둘 중 하나 21 초과
    elif dealer.sum_result > 21:
        print("Player win~")
    elif player.sum_result > 21:
        print("Player lose~")  
    
    # 둘이 합 비교
    elif player.sum_result - dealer.sum_result> 0:
        print("You win!!")
    elif player.sum_result - dealer.sum_result == 0:
        print("Draw!!")
    else:
        print("You lose~")
        
    
    
        
##----------------------main----------------------------------       
            
player = Player()
dealer = Dealer()
deck = Deck()    
        

deck.make_deck()
deck.shuffle()

# print(dk.deck)

player.double_hit()                                                  ### 시작하면 2장씩 준다
print("P>>>", player.received_card)
dealer.double_hit() 
print("D>>>", dealer.received_card[0])                               ### 딜러의 카드는 2장 중 한장만 보여준다.

player.sum()
dealer.sum()

print(player.sum_result)
print(dealer.sum_result)

while (player.sum_result <21 and dealer.sum_result < 21):
    choice = input("카드를 한장 더 받으시겠습니까? yes / no\n")

    if choice == "yes":                                                 ## 각자 한장씩 hit 하는 것

        player.hit()
        dealer.hit()
        print("P>>>", player.received_card)
        print("D>>>", dealer.received_card[0])

        player.sum()
        dealer.sum()
        continue
    
    elif choice == "no":
    
        dealer.machine_hit()
        
        print(player.received_card)
        print(dealer.received_card)
        
        player.sum()
        dealer.sum()
        print("P SCORE>>>",player.sum_result)
        print("D SCORE>>>",dealer.sum_result)
       
        decide_result()
        break
      
