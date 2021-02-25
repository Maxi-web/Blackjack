import random

#Creating a card class inc. Suit and value of card.
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        if self.value == 11:
            print("%s of %s" % ('Jack',self.suit))
            self.value = 10
        elif self.value ==12:
            print("%s of %s" % ('Queen', self.suit))
            self.value = 10
        elif self.value ==13:
            print("%s of %s" % ('King', self.suit))
            self.value = 10
        else:
            print("%s of %s" % (self.value, self.suit))


#Creates a full deck of cards.
class Deck:
    def __init__(self):
        self.cards = []
        self.build()


    def build(self):
        for s in ["Hearts", "Diamonds", "Spades", "Clubs"]:
            for val in range(1,14):
                #if val == 11:
                    #self.cards.append(Card(s,10))
                #elif val ==12:
                    #self.cards.append(Card(s,10))
                #elif val ==13:
                    #self.cards.append(Card(s,10))
                #else:
                    self.cards.append(Card(s,val))

    def show(self):
        for item in self.cards:
            item.show()

    def shuffle(self):
        for item in range(len(self.cards)-1, 0, -1):
            ran = random.randint(0,item)
            self.cards[item], self.cards[ran] = self.cards[ran], self.cards[item]

    def drawCard(self):
        return self.cards.pop()

#Creates the Player class. player has name and hand, can 'hit or 'stick', showHand,
#show one card, show score, DealerFinish method
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def hit(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def showHand_Dealer(self):
            self.hand[0].show()
            print("?")

    def score(self):
        s = 0
        for card in self.hand:
            s += card.value
        return s

    def hit_stick(self,deck):
        ans = input("Hit or Stick:")
        print(ans)
        if ans.lower() == "hit":
            self.hit(deck)
            if self.score() <= 21:
                print(self.score())
                self.hit_stick(deck)
            else:
                print(self.score())
                print("Bust")
        elif ans.lower() == "stick":
            if self.score() < 14:
                print(self.score())
                print(str(self.score())+" is too low to stick, you must hit atleast 14!")
                self.hit_stick(deck)
            else:
                print(self.score())
                print("Sticking with "+str(self.score())+" I see!")

        elif ans.lower() == "debug":
            print("hope you found the bug")
        else:
            print("ummmm there is a third option?")
            self.hit_stick(deck)

    def DealerFinish(self,deck,player):
         if player.score() > 21:
             print("The dealer has won")
             playAgain()
         elif self.score() <= 16:
             self.showHand()
             print(self.score())
             self.hit(deck)
             self.DealerFinish(deck,player)
         elif self.score() >= 21:
             self.showHand()
             print(self.score())
             print("Dealer Bust!")
             playAgain()
         else:
             self.showHand()
             print(self.score())
             winner(player, self)


def playAgain():
     ans = input("Play again? Y or N: ")
     print(ans)
     if ans.lower() == "y":
         play("Max", "Dealer")
     elif ans.lower() == "n":
         print("See Ya")
     else:
         print("Sorry what did you say? Did you want to")
         playAgain()


def winner(player, dealer):
    if (player.score() > dealer.score()) and (player.score() <= 21):
        print("Player wins")
        playAgain()
    else:
        print('The house always wins')
        playAgain()

def play(player, dealer):
    deck = Deck()
    deck.shuffle()
    p = Player(player)
    cpu = Player(dealer)
    p.hit(deck)
    p.hit(deck)
    cpu.hit(deck)
    cpu.hit(deck)
    p.showHand()
    cpu.showHand_Dealer()
    print(p.score())
    p.hit_stick(deck)
    cpu.DealerFinish(deck,p)



play("Max", "Dealer")
