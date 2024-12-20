
print("Welcome to the secret auction.")

def place_your_bid (dictionary):
    name = input("What is your name? ")
    bid = input("Place your bid: $")
    dictionary[name] = bid

def new_bid ():
    choice = input("Is there any more bidders? ")
    if choice.lower() == "yes":
        return True
    elif choice.lower() == "no":
        return False
    else:
        print('Please enter "yes" or "no".')
        new_bid()

def find_winning_bid (dictionary):
    max_bid = 0
    winner = ""
    for key in dictionary:
        if int(dictionary[key]) > max_bid:
            max_bid = int(dictionary[key])
            winner = key
    print(f"Winner of the auction is {winner} with a bid of ${max_bid}")

bidding_is_on = True
bids = {}

while bidding_is_on:
    place_your_bid(bids)
    bidding_is_on = new_bid()

find_winning_bid(bids)

