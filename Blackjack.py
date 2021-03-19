#Declaring variables to store
import random 
suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','King','Queen','Jack','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'King':10,'Queen':10,'Ace':11}
playing=True
#create a card class
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank+' of '+self.suit+' '
class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        self.aces+=1 if values[card.rank]==11 else 0
    def adjust_for_ace(self):
        while self.value>21 and self.aces>0:
            self.value-=10
            self.aces-=1
#create a deck class
class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp+='\n'+card.__str__()
        return "The Deck has: "+deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card=self.deck.pop()
        return single_card
class Chips:
    def __init__(self,total=100):
        self.total=total
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet
def  take_bet(chips):
    while True:
        try:
            chips.bet=int(input('How many chips would you like to bet: '))
            print(chips.bet)
        except:
            print('sorry provide an integer')
        else:
            if chips.bet>chips.total:
                print(f'sorry you dont have enough chips {chips.total}')
            else:
                break
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
def hit_or_stand(d,h):
    global playing
    x=int(input('enter 1 or 0 : '))
    if x==1:
        hit(d,h)
    elif x==0:
        print('stand')
        playing=False
def player(p,chips):
    if p==1:
        print('Win')
        chips.win_bet()
    elif p==0:
        print('lose')
        chips.lose_bet()
    else:
        print('tie')
def show_some(p,d):
    print('Player')
    print(*p.cards)
    print('Dealer')
    print(*d.cards)
print('Welcome to BlackJack Game !')
while True:
    p=Deck()
    t=Hand()
    d=Hand()
    p.shuffle()
    t.add_card(p.deal())
    t.add_card(p.deal())
    d.add_card(p.deal())
    d.add_card(p.deal())
    show_some(t,d)
    s=Chips()
    take_bet(s)
    while playing:
        hit_or_stand(p,t)
        show_some(t,d)
        if t.value>21:
            player(0,s)
            break
    if t.value<=21:
        while d.value<=17:
            hit(p,d)
            show_some(t,d)
        if d.value>21:
            player(0,s)
        elif d.value<t.value:
            player(1,s)
        elif d.value>t.value:
            player(0,s)
        else:
            player(2,s)
    print(f'\n player total chips are at {s.total} ')
    newgame=input('y/n ')
    if newgame=='y':
        playing=True 
        continue
    else:
        print('End of game')
        break

