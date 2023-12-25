#class
import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
class Deck:
    #ゲーム開始時におけるデッキの箱生成
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in range(4) for rank in range(1, 14)]
        random.shuffle(self.cards)
        
    def deal_card(self):
        return self.cards.pop()#returnがpop関数であれば、ドロー後の山札を返り値にしなくても山札は更新される。テストコードで確認済み。

class Hand:
    #プレイヤーカードの箱生成
    def __init__(self):
        self.cards =[]
        
    def add_card(self, card):
        self.cards.append(card)
        return self.cards
        
    def calculate_score(self):
        score = 0
        num_aces = 0

        for card in self.cards:
            if card.rank >= 10:
                score += 10
            elif card.rank == 1:
                num_aces += 1
                score += 11
            else:
                score += card.rank

        while score > 21 and num_aces:
            score -= 10
            num_aces -= 1

        return score
        