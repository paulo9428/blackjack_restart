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
        
        shuffled_deck = deck
        

class Part:

    def card_sum():
        return sum(my_card)

    def hit():
        return # card.pop
    
    def stay():
    
    def fail():
        if sum(my_card) > 21:

            print("fail!!!")
            
            print                    ## 상대의 승으로 표시된다

    
class Player(Part):

    my_card = []

    def __init__(self):
        self.name = name

    def question(self):
        a = input("카드를 뽑으시겠습니까? (Usage: Yes / No / Stand\n")
        if a == "Yes":
            return #card.pop (새로 카드를 뽑는다.)
        elif a == "No":
            exit() #끝낸다.

class Dealer(Part):

    bot_card = []

    def machine_hit():
        if sum(my_card) > 17:
            #카드 안 받는다
        else:
            #카드 받는다
#---------------Main Flow-------------------




start = input("게임에 참석하시겠습니까? (Usage: Yes / No\n")

if start == "Yes":
    
    my_card = random.choice(shuffled_deck, k=2)    ##플레이어가 2장을 받는다
    
    bot_card                                       ##딜러가 2장을 받는다 
                                                   ##딜러의 카드 한장을 보여준다 
                                                     
elif start == "No":
    
    print("다음에 봐요")
    
    exit()

second_turn = input("카드를 한장 받으시겠습니까? (Usage: Yes / No)\n")

if second_turn == "Yes":

    my_card = my_card.append()

elif second_turn == "No":
                                                    ##둘의 숫자를 비교해 결과를 판정한다

    print() #결과
    exit()

third_turn = input("카드를 한장 받으시겠습니까? (Usage: Yes / No)\n")




    
    




    