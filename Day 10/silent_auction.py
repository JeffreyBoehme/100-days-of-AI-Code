print("Welcome to the Silent Auction")
Auction = True
bids = {}


def compareBids(bids):
    top_bid = 0
    top_bidder = ""
    for choice in bids:
        if bids[choice]["bid"] > top_bid:
            print(choice)
            print(bids[choice]["bid"])
            top_bid = bids[choice]["bid"]
            top_bidder = choice

    return top_bidder, top_bid


while Auction:
    bid = 0
    name = ""
    name = input("What is your name? \n")
    bid = input("What is your bid? \n")
    bids[name] = {"name": name, "bid": int(bid)}
    another = input("Are there more bidders? \n")
    if another == "no":
        Auction = False

winner = compareBids(bids)

print(f"The Winner Is: {winner[0]} with a bid of {winner[1]}")
