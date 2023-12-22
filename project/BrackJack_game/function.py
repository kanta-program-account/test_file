#function
from BlackJack_class import Card
from BlackJack_class import Deck
from BlackJack_class import Hand

def blackjack_game():
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    
    i = 0
    for i in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        i += 1
    
    game_over = False
    
    while not game_over:
        player_score = player_hand.calculate_score()
        dealer_score = dealer_hand.calculate_score()
        
        print('Your cards:' + str([card.rank for card in player_hand.cards]) + ' current score:' + str(player_score))
        print("Dealer's first card:" + str(dealer_hand.cards[0].rank))
        
        if player_score > 21 or dealer_score > 21:
            game_over = True
        else:
            hit_or_stay = int(input("Type 0:hit, 1:stay ⇒ "))
            if hit_or_stay == 0:
                player_hand.add_card(deck.deal_card())
            else:
                game_over = True
                
    #ディーラーのターン
    while dealer_score < 17:
          dealer_hand.add_card(deck.deal_card())
          dealer_score = dealer_hand.calculate_score()
          
    #勝者の判定
    print('Your final hands:' + str([card.rank for card in player_hand.cards]) + 'final score:' + str(player_score))
    print("Dealer's final hands:" + str([card.rank for card in player_hand.cards]) + 'final score:' + str(dealer_score))
    
    if player_score > 21:
        print('You went over. You lose.')
    elif dealer_score > 21:
        print('Dealer went over. You win!.')
    elif player_score == dealer_score:
        print("It's draw.")
    elif player_score > dealer_score:
        print('You win!')
    else:
        print('You lose.')

