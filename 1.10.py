import random

suites = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
    "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14
}

class Card:
    def __init__(self, rank, suit):
        rank = rank.capitalize() if rank.isalpha() else rank  # Normalize rank
        suit = suit.capitalize()                              # Normalize suit

        if rank in ranks and suit in suites:
            self.rank = rank
            self.suit = suit
        else:
            raise ValueError("Invalid rank or suit.")

    
    def value(self):
        return ranks[self.rank]
    

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards=[]
      
        for suit in suites:
            for rank in ranks:  # rank is the string key, like "2", "Jack", etc.
                self.cards.append(Card(rank, suit))

        random.shuffle(self.cards)    

    def display_cards(self):

        for card in self.cards:
            print(card)

    def pick_card_from_deck(self):

        return self.cards.pop()
    
    def total_cards_left(self):
        return len(self.cards)



player_one_score=0
player_two_score=0

deck=Deck()

while True:

    if(deck.total_cards_left()==0):
        if(player_one_score>player_two_score):
            print("Player one won")
        elif(player_one_score==player_two_score):
            print("Game has been tied")    
        else:
            print("Player 2 won")    
        break

    first_player_choice=deck.pick_card_from_deck()
    second_player_choice=deck.pick_card_from_deck()

    print(f"The first player chooses {first_player_choice}")


    print(f"The second player chooses {second_player_choice}")




    

    if first_player_choice.value() > second_player_choice.value():
        print("Player 1 wins!")
        player_one_score+=1
    elif first_player_choice.value() < second_player_choice.value():
        print("Player 2 wins!")
        player_two_score+=1
    else:
        print("It's a tie!")



    print(f"The score is {player_one_score}:{player_two_score}")
