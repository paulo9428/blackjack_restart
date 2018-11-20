import random

class Deck:                                       ##instance 없이 쓰는 static method로 Deck.make_deck()

    deck = []                           
    
    def make_deck():                               ## deck 을 만든다
        
        shape = ["S","D","H","C"]
        number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] "J" = "10"
        
        for i in range (0,4):
            res_shape = shape[i]
            for n in range (0, 13):
                res_number = number[n]

                card = res_shape + res_number
                
                deck.append(card)
        
    def shuffle():                         ## deck 을 섞는다
        random.shuffle(deck)    

class Sum:

    def sum(self):
        
        sum_result = 0
        
        
        for i in self.received_card:
            sum_result += int(i[1:2])


    def a_decision():

        'A' = 11

        if i[1] == 'A' and sum_result + A > 21:               ## A의 숫자를 정한다                   
            
            int(i[1]) = 1

        elif i[1] == 'A' and sum_result =< 21:
            
            int(i[1]) = 11
            
    def jqk_decision():

        if i[1] == 'J' or i[1] == 'Q' or i[1] == 'K':
            
            int(i[1]) = 10
    

class Match:
    
    def fail(self):                   ## 가진 카드의 합이 21이 넘으면 패한다
        if self.received_card.sum() > 21:
            print(self.name "==>>   Lose!!!")
            continue
        
        



    def match(self):                            ## sum 을 비교하여 승부를 낸다

        if player.received_card.sum() - dealer.received_card.sum() > 0:

            print("You win!!")

        elif player.received_card.sum() - dealer.received_card.sum() == 0:

            print("Draw!!")

        else:

            print("You lose~")


    
    



class Part:
    received_card = []
    def pop_card ():
        for i in range(1,3):
            card = deck.pop(i)
            my_card.append(card)

    

    def __init__(self):
        
        self.received_card = received_card

    
    def hit(self):                             ## hit 하는거
        
        return self.received_card.append(deck.pop(1))
        
        print(self.received_card)



class Player(Part):
    def __init__(self):
        self.name = "player"
   

    

class Dealer(Part):
    def __init__(self)
        self.name = "dealer"

    
    
    def machine_hit(self):
        if bot_card.sum() > 17:
            #카드 안 받는다
        else:
            #카드 받는다





                                                            
                
             
                



#---------------Main Flow-------------------

invite = input('게임에 참석하시겠습니까? (Yes / No)/n')

if invite == 'Yes':

    player = Player()
    dealer = Dealer()

    Deck.make_deck().shuffle()
    
    
    player.received_card.extend([deck.pop(), deck.pop()])   ## pop 두번 어떻게??
    dealer.received_card.extend([deck.pop(), deck.pop()])

    
    print("P>>>", player.received_card)
    print("D>>>", dealer.received_card[0])


elif invite == 'No':

    print('>>>','다음에 만나요')

while True:
    
    gesture = input('카드를 한장 받으시겠습니까? (Yes / No)/n')

    if gesture == 'Yes':

        player.received_card.append(deck.pop())
        
        print(player.received_card)

        continue
    
    elif gesture == 'No':

        dealer.machine_hit()
        
        print("P>>>", player.received_card)
        print("D>>>", dealer.received_card)

        break



        
    
    
    
    
        
    
