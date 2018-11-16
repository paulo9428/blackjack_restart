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



