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

class Participant:

    received_card = []

    def __init__(self):
        
        self.received_card = received_card

    
    def hit(self):                             ## hit 하는거
        
        self.received_card.append(new1.pop(1))
        



class Player(Participant):

    def __init__(self):

        self.name = 'player'

   

class Dealer(Participant):

    def __init__(self):

        self.name = 'dealer'
    
    
    def machine_hit(self):
        
        if Sum.sum_result() <= 17:
            self.hit()
        elif Sum.sum_result > 17:
            return dealer.received_card 

###-----------------------------------------------------------------------------------            

class Sum:                                          ## Match 클래스에 상속?????

    
    sum_result = 0   

    def sum(self):
        
        for i in self.received_card:
            
            sum_result += int(i[1])
        

    def a_decision():
        
        if i[1] == 'A' and sum_result + 11 > 21:
            a = i[1]
            a = 1
            d = a + sum_result
        elif i[1] == 'A' and sum_result + 11 < 21:
            a = i[1]
            a = 11
            d = a + sum_result  
             
             
    def jqk_decision():
        a = 0
        if i[1] == 'J' or i[1] == 'Q' or i[1] == 'K':
            a = i[1]
            a = 10
   

class Match(Sum):                     ## Match 클래스가 Sum 클래스를 상속
    
    def fail(self):                   ## 가진 카드의 합이 21이 넘으면 패한다
    
        if self.received_card.sum() > 21:

            print(self.name, "Lose!!!")


    def match():                            ## sum 을 비교하여 승부를 낸다

        if player.received_card.sum() - dealer.received_card.sum() > 0:

            print("You win!!")

        elif player.received_card.sum() - dealer.received_card.sum() == 0:

            print("Draw!!")

        else:

            print("You lose~")

                                             
#---------------Main Flow-------------------

invite = input('게임에 참석하시겠습니까? (Yes / No)'+'\n')       ## 시작

if invite == 'Yes':

    player = Deck()
    dealer = Deck()

    
    print("P>>>", player.pop_card())
    print("D>>>", dealer.pop_card())


elif invite == 'No':

    print('>>>','다음에 만나요')

else :
    print("=============================================Error!!! 다시 입력해주세요.===============================")

while True:                                                ## 둘째 턴 ~ 종료
    
    gesture = input('카드를 한장 받으시겠습니까? (Yes / No)/n')

    if gesture == 'Yes':
        
        player.hit()
        dealer.hit()


        print("P>>>", player.received_card)
        print("D>>>", dealer.received_card)

        continue
    
    elif gesture == 'No':

        dealer.machine_hit()
        
        print("P>>>", player.received_card)
        print("D>>>", dealer.received_card)

        Match.match()

        
        break