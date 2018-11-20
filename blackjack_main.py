import random

class Deck:          
    
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
        
    
        
class Match:
     
    def fail():                   ## 가진 카드의 합이 21이 넘으면 패한다
        if sum(my_card) > 21:
            return sum(my_card)
            time.sleep(5) 
            print(sum(my_card), "다음 기회에")


    def sum():                       ##가진 카드 문자열에서 정수를 추출하여 합을 낸다        

    


    def                             ## sum 을 비교하여 승부를 낸다







class Part:

    
    def hit(self):                             ## hit 하는거
        return my_card.append(deck.pop(1))
        print(my_card)

    cmd = input("한 장 더 받으시겠습니까? Yes : Yes, No : enter >>")
    
    if cmd == "Yes":
        my_card.append(deck.pop(2))
        print(my_card)

    if cmd == "No":
        pass

    
    
    
    
    def a_count(self):                   ## A의 숫자를 정한다                   
    if 11 + sum(my_card) < 21:
        int(a) = 11
    elif 11 + sum(my_card) > 21: #else
        int(a) = 1
    
    

    
class Player(Part):

    my_card = []

    def __init__(self):
        
        self.my_card = my_card

    def question(self):
        a = input("카드를 뽑으시겠습니까? (Usage: Yes / No / Stand\n")
        if a == "Yes":
            return                  #card.pop (새로 카드를 뽑는다.)
        elif a == "No":
            exit()                  #끝낸다.

class Dealer(Part):

    bot_card = []

    def __init__(self):
        
        self.bot_card = bot_card    
    
    
    def machine_hit(self):
        if sum(bot_card) > 17:
            #카드 안 받는다
        else:
            #카드 받는다

#---------------Main Flow-------------------

invite = input('게임에 참석하시겠습니까? (Yes / No)')

if invite == 'Yes':
    











    
    




    