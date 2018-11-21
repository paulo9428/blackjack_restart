class Deck:                                       
    

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
        
        
        
        
    def shuffle(self):

        random.shuffle(self.deck)


###########---------------------------------------------------------------

class Participant:

    

    def __init__(self):
        
        received_card = []
        
        self.received_card = received_card

    
    def double_hit(self):
        
        
        for i in range(0,2):
            
            card = self.deck.pop(i)
            
            self.received_card.append(card)
        
        
    def hit(self):                             ## hit 하는거
        
        card = self.deck.pop()

        self.received_card.append(card)

    
    def fail(self):                         ## 가진 카드의 합이 21이 넘으면 패한다
        
        if self.sum_result > 21:

            print(self.name, "Lose!!!")
        
    
    
    
    



class Player(Participant):

    def __init__(self):

        self.name = 'player'

   

class Dealer(Participant):

    def __init__(self):

        self.name = 'dealer'
    
    
    def machine_hit(self):



##----------------------------------------------------------

class Sum:
     
    def __init__(self):

        for i in self.received_card:                                       #### j,q,k 결정
            
            if i[1] == 'J' or 'Q' or 'K':

                a = i[1]
                a = 10 

        
            elif i[1] == 'A' and sum_result + 11 > 21:                            ### a 결정
                
                a = i[1]
                a = 1
                
                sum_result += a
            
            elif i[1] == 'A' and sum_result + 11 < 21:
                
                
                sum_result += a 

        
        
                
            
    def calc_score(self):
       
        
       
        
        num.append(int(i[1]))
        
        num = []                                                            #### 환산한 점수를 num = [] 에 담아준다
        
        return sum(num)
        
            
        
            
               
            
        

    
    
        
             
    
    


    

class Match(Sum):

    
    def match():                            ## sum 을 비교하여 승부를 낸다

        if player.calc_score - dealer.calc_score > 0:

            print("You win!!")

        elif player.calc_score - dealer.calc_score == 0:

            print("Draw!!")

        else:

            print("You lose~")





        
        
        
    


























while True :

a = Deck()
a.make_deck(); a.shuffle()                                                                                           ### deck을 섞는다

##print(self.deck)

d = Dealer()
p = Player()



                                                                                           ## 딜러가 1장을 두번 받는다

                                                                                            ## 플레이어가 1장을 두번 받는다

                                                                                            ## 딜러의 첫번째 한장과 플레이어의 카드 전체를 보여준다

                                                                                            ##  카드를 한장 더 받으시겠습니까??

                                                                                            ## 예 -> 2번째줄            

                                                                                            ## 아니요 -> 딜러 17 이상일때까지 받는다 -> 승부를 낸다


