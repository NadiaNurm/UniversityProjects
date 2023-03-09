
import random



card_int_values = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10': 10,
    'J' : 11,
    'Q' : 12,
    'K' : 13,
    'A' : 14,
}


class Suit:
    def __init__(self,name,image,value) -> None:
        self.name = name
        self.image = image
        self.value = value


card_suit = [
    Suit('Hearts'  , '\u2665', 4),
    Suit('Diamonds', '\u2666', 3),
    Suit('Clubs'   , '\u2663', 2),
    Suit('Spades'  , '\u2660', 1),
]

def get_suit(suit)-> Suit:
    for single_suit in card_suit:
        if single_suit.name == suit:
            return single_suit

class Card:
    def __init__(self,value,suit) -> None:
        self.value = value
        self.suit = get_suit(suit)
        self.int_value = card_int_values[self.value]

    def to_str(self):
        return f'{self.value}{self.suit.image}'
    
    def equal_suit(self,card:'Card'):
        if self.suit == card.suit:
            return True
        return False
    
    def more(self,card:'Card'):
        if self.int_value > card.int_value:
            return True
        if self.int_value < card.int_value:
            return False
        if self.suit.value > card.suit.value:
            return True
        return False

    def less(self,card:'Card'):
        if self.int_value < card.int_value:
            return True
        if self.int_value > card.int_value:
            return False
        if self.suit.value < card.suit.value:
            return True
        return False

class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.build()

    def build(self):
        for suit in card_suit:
            for value in card_int_values:
                self.cards.append(Card(value,suit.name))
        
    def shuffle(self):
        random.shuffle(self.cards)

    def show(self):
        output_string = f'deck[{len(self.cards)}]: '
        card_list = []
        for card in self.cards:
            card_list.append(card.to_str())
        print(output_string + ', '.join(card_list))

    def draw(self,x):
        drawn_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return drawn_cards

#test = Card('10','Clubs')
#test2 = Card('10','Diamonds')
#print(test.to_str())
#print(test2.to_str())
#print(test.less(test2))
test3=Deck()
test3.shuffle()
test3.show()
test3.draw(3)
test3.show()
