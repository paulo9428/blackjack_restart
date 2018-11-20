class Deck:                                       ##instance 없이 쓰는 static method로 Deck.make_deck()

   
    deck = []                           
    
    def make_deck():                               ## deck 을 만든다
        
        shape = ["S","D","H","C"]
        number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        
        for i in range (0,4):
            res_shape = shape[i]
            for n in range (0, 13):
                res_number = number[n]

                card = res_shape + res_number
                
                deck.append(card)
        
    def shuffle():                         ## deck 을 섞는다

    
        random.shuffle(deck)  

###########---------------------------------------------------------------

class Participant:

    received_card = []

    def __init__(self):
        
        self.received_card = received_card

    
    def hit(self):                             ## hit 하는거
        
        self.received_card.append(deck.pop())
        



class Player(Participant):

    def __init__(self):

        self.name = 'player'

   

class Dealer(Participant):

    def __init__(self):

        self.name = 'dealer'
    
    
    def machine_hit(self):
        
        while self.sum_result =< 17:
            
            self.received_card.append(deck.pop())

            if self.sum_result > 17:

                break

###-----------------------------------------------------------------------------------            

class Sum:                                          ## Match 클래스에 상속?????

    
    def sum(self):

        self.sum_result = 0
        
        for i in self.received_card:
            
            self.sum_result += int(i[1])
       

        

    def a_decision(self):
        
        if i[1] == 'A' and self.sum_result + 11 > 21:
            
            a = i[1]
            a = 1

            sum_result += a
            
        elif i[1] == 'A' and self.sum_result + 11 < 21:
            
            a = i[1]
            a = 11

            sum_result += a
             
             
             
    def jqk_decision(self):
        
        if i[1] == 'J' or i[1] == 'Q' or i[1] == 'K':
            
            a = i[1]
            a = 10

            self.sum_result += a
        

            

            
class Match(Sum):                     ## Match 클래스가 Sum 클래스를 상속
    
    def fail(self):                   ## 가진 카드의 합이 21이 넘으면 패한다
    
    if self.sum_result > 21:

        print(self.name, "Lose!!!")



    def match():                            ## sum 을 비교하여 승부를 낸다

        if player.sum_result - dealer.sum_result > 0:

            print("You win!!")

        elif player.sum_result - dealer.sum_result == 0:

            print("Draw!!")

        else:

            print("You lose~")


    
    






                                                            
#---------------Main Flow-------------------

invite = input('게임에 참석하시겠습니까? (Yes / No)/n')       ## 시작

if invite == 'Yes':

    player = Player(), Match()
    dealer = Dealer(), Match()

    Deck.make_deck().shuffle()
    
    
    player.received_card.extend([deck.pop(), deck.pop()])   ## pop 두번 어떻게??
    dealer.received_card.extend([deck.pop(), deck.pop()])

    
    print("P>>>", player.received_card)
    print("D>>>", dealer.received_card[0])


elif invite == 'No':

    print('>>>','다음에 만나요')


while True:                                                ## 둘째 턴 ~ 종료
    
    gesture = input('카드를 한장 받으시겠습니까? (Yes / No)/n')

    if gesture == 'Yes':

        player.hit()
        
        print("P>>>", player.received_card)
        print("D>>>", dealer.received_card[0])

        continue
    
    elif gesture == 'No':

        dealer.machine_hit()
        
        print("P>>>", player.received_card)
        print("D>>>", dealer.received_card)

        Match.match()

        
        break

        
                
             
                
                
            

                                                   
            
            
            
            
    



