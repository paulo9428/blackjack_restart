import random

shape = ["S","D","H","C"]
number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
deck = []

def make_deck():                            ## deck 을 만든다
    
    for i in range (0,4):
        res_shape = shape[i]
        for n in range (0, 13):
            res_number = number[n]

            card = res_shape + res_number
            
            deck.append(card)
    
        
def shuffle():                         ## deck 을 섞는다
        
    make_deck()
    
    random.shuffle(deck)           
        
    
        

     
def fail():                   ## 가진 카드의 합이 21이 넘으면 패한다
    
    if my_list.sum() > 21:

        print("You Lose!!!")


    
    
def match():                            ## sum 을 비교하여 승부를 낸다

    if my_list.sum() - bot_list.sum() > 0:

        print("You win!!")

    elif my_list.sum() - bot_list.sum() == 0:

        print("Draw!!")

    else:

        print("You lose~")







    
    def hit(self):                             ## hit 하는거
        
        my_card.append(deck.pop())

    
    
    
    
    

    def machine_hit(self):                  ## 17 이상일때까지 받는다
        if bot_card.sum() > 17

            

        else:


    

    

#---------------Main Flow-------------------




start = input("게임에 참석하시겠습니까? (Usage: Yes / No)\n")        ## 첫째 턴

if start == "Yes":
    
    my_card =                                      ##플레이어가 2장을 받는다
    
    bot_card =                                     ##딜러가 2장을 받는다 
    
    print()                                        ##딜러의 카드 한장을 보여준다 
                                                     
elif start == "No":
    
    print("다음에 봐요!")
    
    exit()

while True:

    get_card = input("카드를 받으시겠습니까? (Usage: Yes / No)\n ")

    if get_card == "Yes":

                                    ## 플레이어가 한장 받는다
                                    ## 받은 카드를 보여준다            
        continue
    
    elif get_card == "No":
                                    
                                    ## 딜러가 17이상일때가지 받는다
                                    ## sum 을 비교하여 승패를 프린트한다
        
        break


    
    
    

    
