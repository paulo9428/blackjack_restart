import random


class Deck:                                       ##instance 없이 쓰는 static method로 Deck.make_deck()
    
    deck = []
    new1 = []         
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
        self.make_deck()   
        random.shuffle(self.deck)
        return self.deck

    
    def pop_card(self):
        self.new1 = self.shuffle()
        received_card = []
        for i in range(1,3):
            card = self.new1.pop(i)
            received_card.append(card)
        print(received_card)
        return received_card

    def jqk_decision(self,deck):
        score = []
        for i in deck:
            if 'J' or 'Q' or 'K' in i[1]:
                score.append(i[1:])
            
            else :
                score.append(i[1:])
            
        # print (score)
        return score
    # print (score)
   
    # def machine_hit(self):

    #     if Sum.make_score <= 17:
    #         self.hit()
    #     elif Sum.sum_result > 17:
    #         return dealer.received_card 
    
    # sum_result = 0   
   

  
    


class Player(Deck):
    def hit(self, player_deck):
                ## hit 하는거                
        player_deck.append(self.new1.pop(0))
        print("player_deck ----->", player_deck)
        return player_deck
    
    
    def to_int(self, score):
        num = []
        if 'A' in score:
            a_choice = input("A는 어떤 값으로 선택하시겠습니까? 1) 1 2) 11>> ")
            
        for i in score:
            if 'J' == i or 'Q' == i or 'K' == i:        ##### line 49로 옮기는게 낫지않을까? /// Chris
                i = 10                                      # reason why => def jqk_dec ()의 if 의미가없고 i[1:]로
                num.append(i)                          # 다 넣어버리면 될듯
            elif 'A' == i and a_choice == "1":
                i = 1
                num.append(i)
            elif 'A' == i and a_choice == "2":
                i = 11
                num.append(i)
            else :
                s = int(i)
                num.append(s)
        print("플레이어>>>>>>>>>", num)        
        return num


class Dealer(Deck):
    def dealer_auto_hit(self, dealer_deck):
        dealer_deck.append(self.new1.pop(0))
        print("Dealer_deck >> ", dealer_deck)
        return dealer_deck

    def to_int(self, score):
        num = []
        for i in score:

            if 'J' == i or 'Q' == i or 'K' == i:        ##### line 49로 옮기는게 낫지않을까? /// Chris
                i = 10                                      # reason why => def jqk_dec ()의 if 의미가없고 i[1:]로
                num.append(i)                          # 다 넣어버리면 될듯

            elif 'A' == i:
                continue 
            
            else: 
                s = int(i)
                num.append(s)

        if 'A' in score and sum(num) > 10:
            num.append(1)
        elif 'A' in score and sum(num) <= 10:
            num.append(11)
        print("딜러=======> " , sum(num))
        return(sum(num))



while True :
    invite = input('게임에 참석하시겠습니까? (Yes / No)'+'\n')       ## 시작

    if invite == 'Yes' :

        player = Player()
        dealer = Dealer()

        player_received_card = player.pop_card()
        
        dealer_received_card = dealer.pop_card()
        dealer_split_num = dealer.jqk_decision(dealer_received_card)
        dealer.to_int(dealer_split_num)

        
        print("P>>>", player_received_card)
        print("D>>>", dealer_received_card)

        # while True:
        
        #     dealer_score = finish.jqk_decision(dealer_received)
        #     finish.to_int(dealer_score)
        #     dealer_sum = sum(finish.to_int(dealer_score))
            
        #     print(dealer_sum)
            

        #     if dealer_sum <= 17:
        #         dealer.dealer_auto_hit(dealer_received)
                
        #         print(dealer_received)
        #         continue
          
        #     else:
        #         break
            
            
    elif invite == 'No':
        print('>>>>>>>>>>>','다음에 만나요')
        break

    else :
        print("=============================================Error!!! 다시 입력해주세요.===============================")
        continue
       
        
    
    while True:                                                ## 둘째 턴 ~ 종료
        
        gesture = input('카드를 한장 받으시겠습니까? (Yes / No)' + '\n')

        if gesture == 'Yes':
            
            player_cards = player.hit(player_received_card)

            if dealer.to_int(dealer_split_num) < 17:

                dealer_cards = dealer.dealer_auto_hit(dealer_received_card)
            
                
            player_split_num = player.jqk_decision(player_cards)
            player.to_int(player_split_num)

            dealer_split_num = dealer.jqk_decision(dealer_cards)
            dealer.to_int(dealer_split_num)
            
            # print("P>>>", dealer_cards)
            # player.score = finish.jqk_decision(player_cards)







            # finish.to_int()
            # finish.make_score()
           
        elif gesture == 'No':
            def stop()
            print("어쩌지")
            # No 하면 여기서 비교해서 승부 보기    ##### No 를 했을 때 finish.make_score 함수를 사용해주는게 어떨지 ///Chris
        
        else :
            print ("Error!!!!!! 다시입력해주세요.")
            continue

        

        





        # #자동 덱받기   >>> 오늘해야할일 중 카테고리 1번
        # def dealer_add_deck ():
        #     while True:
        #         if sum(self.dealer_num) >= 17:
        #             stop 함수
        #             break
        #         elif sum(self.dealer_num) < 17:    ##### dealer의 num과 score가 필요 (str->정수화, 덱의 합 구하기)
        #             d.player.hit(b[0],b[1])




        #### 오늘 해야할일
        # 1. Dealer의 자동 덱받기기능
        # 2. Player or Dealer가 4장 받았을 경우 일어나는 오류 처리
        # 3. Yes를 했을 때 바로 스코어가 sum으로 되는 상황 지우기 stop ==> sum    //// 딜러 => sum

        # 4. Dealer가 A를 받았을 경우는 input을 묻지 않고 바로 계산하게끔 하는 함수
        # 5. 딜러의 num, score가 없음
        # 6. 