from typing import Type
from collections import defaultdict
import random

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
          '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}

# define Global for favorable/fair "hit" probability and pre-defined indices

FAIRPROBABILITY = 0.5
VISIBLE_CARD_INDEX = 0
OCCURENCE_INDEX = 0
WINNING_INDEX = 1


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print(f'Invalid card: {suit} {rank}')

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_value(self):
        return VALUES[self.rank]


# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        ans = "Hand contains "
        for i in range(len(self.cards)):
            ans += str(self.cards[i]) + " "
        return ans
        # return a string representation of a hand

    def add_card(self, card):
        self.cards.append(card)
        # add a card object to a hand

    def get_value(self):
        value = 0
        aces = False
        for c in self.cards:
            rank = c.get_rank()
            v = VALUES[rank]
            if rank == 'A':
                aces = True
            value += v
        if aces and value < 12:
            value += 10
        return value
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video


# define deck class
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s, r))
        # create a Deck object

    def shuffle(self):
        random.shuffle(self.deck)
        # shuffle the deck

    def deal_card(self):
        return self.deck.pop()
        # deal a card object from the deck

    def __str__(self):
        ans = "The deck: "
        for c in self.deck:
            ans += str(c) + " "
        return ans
        # return a string representing the deck


def deal():

    global outcome, in_play, theDeck, playerhand, househand
    # deals the cards to the player and the dealer
    in_play = True
    theDeck = Deck()
    theDeck.shuffle()
    outcome = "Game ongoing"
    # initialize player and dealer hand and add cards to their hands
    playerhand = Hand()
    househand = Hand()
    playerhand.add_card(theDeck.deal_card())
    playerhand.add_card(theDeck.deal_card())
    househand.add_card(theDeck.deal_card())
    househand.add_card(theDeck.deal_card())


def hit():
    global in_play, outcome
    # method to hit (add card to player's heand)
    if in_play:
        playerhand.add_card(theDeck.deal_card())
        val = playerhand.get_value()
        # incase we bust, stop game as player loses automatically
        if val > 21:
            in_play = False
            outcome = "Loss"
    return None


def stand():
    global in_play, outcome
    # method to stand (player no longer wishes to add a card to their hand)
    if playerhand.get_value() > 21:
        # detects if player busted
        outcome = "Loss"
        in_play = False
        return None
    if not in_play:
        # in case stand is called but game is not ongoing (unlikely to happen here but kept snippet as precaution)
        outcome = "Game is over."
        return None
    # getting value of player's hand
    val = househand.get_value()
    while (val < 17):
        # while the value of the dealer's hand is less than 17 we should add card to the dealer's hand
        househand.add_card(theDeck.deal_card())
        val = househand.get_value()
    # comparing dealer's hand value to player's to determine win or loss
    if (val > 21):
        if playerhand.get_value() > 21:
            # in case both bust, house wins
            outcome = "Loss"
        else:
            outcome = "Win"
    else:
        if (val == playerhand.get_value()):
            # a tie is a loss
            outcome = "Loss"
        elif (val > playerhand.get_value()):
            outcome = "Loss"
        else:
            outcome = "Win"
    # reset in_play to mark end of game
    in_play = False
    return None


# define player class


class Player:

    def __init__(self):
        # learned matrix
        self.matrix = defaultdict(defaultdict)

    # helper function for sim(); runs one game at a time
    def sim_game(self) -> list:
        # first deal both hands
        deal()

        # while game is ongoing
        while in_play:
            options = ["hit", "stand"]
            actions_taken = []
            # randomly chose between hitting and standing
            choice = random.choice(options)
            # get the player's current value
            playerhandval = playerhand.get_value()
            # execute random action chosen unless player's hand is 21 and above
            if choice == "hit" and playerhandval < 21:
                hit()
            else:
                stand()
                choice = "stand"
            # record the outcome of the action taken as well the situation (dealer face card value and player hand value)
            result = outcome
            housecard = (househand.cards[VISIBLE_CARD_INDEX]).get_value()
            actions_taken.append((choice, result, housecard, playerhandval))
        # return all the actions taken and valuable datapoints about these actions
        return actions_taken

    def sim(self, trials: int) -> None:
        dealercardvalue = 1
        # initializing the matrix
        while dealercardvalue < 11:
            for playerhandvalue in range(2, 22):
                self.matrix[dealercardvalue][playerhandvalue] = [0, 0]
            dealercardvalue += 1

        # running the simulations using helper function sim_games()
        for trial in range(trials):
            game_result = self.sim_game()
            # update learning matrix
            for result in game_result:
                method, game_status, dealerkey, playervalkey = result
                # when hitting succeeds or standing fails increment winning occurence at matrix address
                # we are assuming that if standing failed, hitting could have succeeded, big assumption but viable strategy
                self.matrix[dealerkey][playervalkey][OCCURENCE_INDEX] += 1
                if method == "hit" and game_status != "Loss":
                    self.matrix[dealerkey][playervalkey][WINNING_INDEX] += 1
                elif method == "stand" and game_status != "Win":
                    self.matrix[dealerkey][playervalkey][WINNING_INDEX] += 1
                else:
                    continue

    def hitme(self, playerhand: Hand, dealerfacecard: Card) -> bool:
        # looks up address in matrix based on player hand value and dealer face card value
        playervalue = playerhand.get_value()
        dealervalue = dealerfacecard.get_value()
        # calculating probability of hit() success at address
        if self.matrix[dealervalue][playervalue][OCCURENCE_INDEX] != 0:
            chancetowin = self.matrix[dealervalue][playervalue][WINNING_INDEX] / \
                self.matrix[dealervalue][playervalue][OCCURENCE_INDEX]
        else:
            # take the risk of hitting hand value is less than 17
            if playervalue < 17:
                chancetowin = 0.5
            else:
                chancetowin = 0

        # if probability derived from data at address is favorable hit(), otherwise stand()
        if chancetowin >= FAIRPROBABILITY:
            return True
        else:
            return False
        # use the matrix to decide whether to hit

    def play(self, trials: int) -> float:
        # play out trials with learned matrix
        number_of_wins = 0
        game_counter = 0

        while game_counter < trials:
            # if game ended check the outcome and update number of wins accordingly
            if not in_play:
                if outcome == "Win":
                    number_of_wins += 1
                # restart game
                deal()
                game_counter += 1
            # use hitme() function to make decision
            choice = self.hitme(
                playerhand, househand.cards[VISIBLE_CARD_INDEX])
            # execute hitme() proposed decision unless player's hand value is 21, in that case stand
            if playerhand.get_value() == 21:
                stand()
            elif choice:
                hit()
            else:
                stand()
        # calculate winning probability from games played and return value
        winning_probability = float(number_of_wins) / float(trials)
        return winning_probability


if __name__ == "__main__":
    sim_num = int(
        input("How many simulations would you like to run for your learning matrix?\n>"))
    game_sim = int(input(
        "How many games would you like the player to run using your learned matrix?\n>"))
    player = Player()
    player.sim(sim_num)
    print("Matrix:", player.matrix, "Winning Rate:", player.play(game_sim))
