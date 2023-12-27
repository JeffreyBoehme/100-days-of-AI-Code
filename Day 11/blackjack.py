import random
import time

cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

deck = [
    "A♠",
    "2♠",
    "3♠",
    "4♠",
    "5♠",
    "6♠",
    "7♠",
    "8♠",
    "9♠",
    "10♠",
    "J♠",
    "Q♠",
    "K♠",
    "A♣",
    "2♣",
    "3♣",
    "4♣",
    "5♣",
    "6♣",
    "7♣",
    "8♣",
    "9♣",
    "10♣",
    "J♣",
    "Q♣",
    "K♣",
    "A♦",
    "2♦",
    "3♦",
    "4♦",
    "5♦",
    "6♦",
    "7♦",
    "8♦",
    "9♦",
    "10♦",
    "J♦",
    "Q♦",
    "K♦",
    "A♥",
    "2♥",
    "3♥",
    "4♥",
    "5♥",
    "6♥",
    "7♥",
    "8♥",
    "9♥",
    "10♥",
    "J♥",
    "Q♥",
    "K♥",
]
FRESHDECK = [
    "A♠",
    "2♠",
    "3♠",
    "4♠",
    "5♠",
    "6♠",
    "7♠",
    "8♠",
    "9♠",
    "10♠",
    "J♠",
    "Q♠",
    "K♠",
    "A♣",
    "2♣",
    "3♣",
    "4♣",
    "5♣",
    "6♣",
    "7♣",
    "8♣",
    "9♣",
    "10♣",
    "J♣",
    "Q♣",
    "K♣",
    "A♦",
    "2♦",
    "3♦",
    "4♦",
    "5♦",
    "6♦",
    "7♦",
    "8♦",
    "9♦",
    "10♦",
    "J♦",
    "Q♦",
    "K♦",
    "A♥",
    "2♥",
    "3♥",
    "4♥",
    "5♥",
    "6♥",
    "7♥",
    "8♥",
    "9♥",
    "10♥",
    "J♥",
    "Q♥",
    "K♥",
]

# 1 the game begins
# 2 2 cards are dealt to each player (one player?) and the Dealer (one of the dealers cards remains hidden but is dealt)
# 3 Player decides to hit or stand
# 3a if Player goes over 21, they are out
# 4 once all players decide to stand, Dealer plays
# 5 Scores are calculated, if a player is NOT out, and scores higher than the dealer, the player wins.

players = []
number_of_players = 0
playing = True


def calculate_score(player, hand):
    """_summary_
    Calculates the score of a players hand.
    If the player is bust, their status is changed to bust.
    If the player is not bust, their score is updated.

    Args:
        player (dict): The player to calculate the score for
        hand (list): The players hand
    """
    score = 0
    aces = 0
    for card in hand:
        card = card[:-1]
        if card == "A":
            aces += 1
        score += cards[card]
    while score > 21 and aces > 0:
        score = score - 10
        aces = aces - 1

    if score > 21:
        print(f"{player} is Bust!")
        player["status"] = "bust"
    else:
        print(f'{player["name"]}\'s score is {score}')
        player["score"] = int(score)


def deal(number, player):
    """_summary_
    Deal a number of cards to a player from the deck.
    Adds the card to the players hand and removes it from the deck.

    Args:
        number (Int): The number of cards to deal
        player (Dict): The player to deal the cards to
    """
    global deck
    for i in range(number):
        # print(player)
        if len(deck) < 1:
            deck = FRESHDECK
            print("Fresh Deck incoming!")
        drawn_card = deck[random.randint(0, len(deck) - 1)]
        player["hand"].append(drawn_card)
        deck.remove(drawn_card)
        if player["name"] == "dealer" and (i + 1) == 2:
            print(f"{player['name']} has drawn a *")
        else:
            print(f"{player['name']} has drawn a {drawn_card}")
        time.sleep(2)
    calculate_score(player, player["hand"])


new_players = []
moreplayers = True
players.append({"name": "dealer", "score": 0, "hand": [], "status": "dealer"})
while moreplayers:
    new_players.append(input("What is the players Name?\n"))
    more = input("Add another player? type 'yes' or 'no'\n")
    if more == "no":
        moreplayers = False

for person in new_players:
    players.append({"name": person, "score": 0, "hand": [], "status": "playing"})

while playing is True:
    # dealer Draws
    for player in players:
        deal(2, player)
        if player["name"] == "dealer":
            continue
        number_of_players += 1
        print(player["hand"])

        while player["status"] == "playing":
            hit_stand = input(f'Would {player["name"]} like to "hit" or "stand"? \n')
            if hit_stand == "hit":
                deal(1, player)
            else:
                print(f'{player["name"]} has chosen to stand.')
                player["status"] = "finished"

    playing = False

for player in players:
    keep_playing = False
    if player["status"] == "finished":
        keep_playing = True

if keep_playing == True:
    dealer_score = 0
    max_score = 0
    for player in players:
        if player["name"] == "dealer":
            dealer_score = int(player["score"])
        if player["status"] == "finished":
            if player["score"] > max_score and player["name"] is not "dealer":
                max_score = player["score"]
    if max_score > dealer_score:
        while dealer_score <= 16:
            deal(1, players[0])
            if dealer_score <= 21:
                dealer_score = int(players[0]["score"])
    else:
        print("Dealer wins.")

    if players[0]["status"] == "dealer":
        for player in players:
            if player["score"] > dealer_score and player["status"] == "finished":
                print(f'{player["name"]} wins!')
            elif player["name"] != "dealer":
                print(f'{player["name"]} loses!')

    else:
        for player in players:
            if player["status"] == "finished":
                print(f'{player["name"]} wins!')
            else:
                print(player["name"])
else:
    print("Dealer wins.")
