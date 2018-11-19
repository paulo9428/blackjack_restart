import random

class Deck:
    deck = []
    shape = ["S","D","H","C"]
    number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def shuffle_cards(self, deck, shape, number):
        self.deck = deck
        self.shape = shape
        self.number = number
        for i in range (0,4):
            res_shape = shape[i]
            for n in range (0, 13):
                res_number = number[n]
                card = res_shape + res_number
                deck.append(card)
                random.shuffle(deck)          
        print (deck)
    shuffle = Deck()
    shuffle.shuffle_cards(deck, shape, number)
    
# class Sum(Deck):
    
#     def card_sum(self):
                
#         my_card = []

#         for i in range(1,3):
#             card = deck.pop(i)
#             a = card.split(' ')
#             my_card.append(card)

#         for res in my_card:                       # ===>>> 정수화 완료, My_card에 댁을 다 채운 뒤 sum(정수화 + 갖고있는 수 만큼 더해줌)test 파일 참고
#             a = res.split(' ')
#             result += int(a[1]) 


# sume = Sum()
# sume.card_sum()
