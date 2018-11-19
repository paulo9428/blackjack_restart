    def hit(self):
        return my_card.append(deck.pop(1))
        print(my_card)

        cmd = input("한 장 더 받으시겠습니까? Yes : Yes, No : enter >>")
        
        if cmd == "Yes":
            my_card.append(deck.pop(2))
            print(my_card)

        if cmd == "No":
            pass

    def stay(self):
        return 
        # dealer 차례로 넘어간다(dealer.pop(1))
    
    import time
    def end(self):
        if sum(my_card) > 21:
            return sum(my_card)
            time.sleep(5) 
            print(sum(my_card), "다음 기회에")
    
    def a_count(self):
        if 11 + sum(my_card) < 21:
            int(a) = 11
        elif 11 + sum(my_card) > 21: #else
            int(a) = 1



for i in range(1,3):
    deck.pop(i)
        
            
             



