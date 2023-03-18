# the list of all bids, containing bidding records (a list of dictionaries) 
bids = [] 

def main():
    print("Welcome to the auction!")

    get_bid()

    # break game loop only when there is no other bidder
    while True:
        resp = input("Any other bidders? Type [Y]es or [N]o ")
        if resp.lower() not in ['y', 'yes']:
            break
        
        get_bid()

    # print(bids)
    get_winner()

def get_bid():
    ''' get bid info from user input, create a dictionary containing bidding record, and add to the list of all bids.'''
    name = input("What is your name? ")
    amount = float(input("What is your bid? "))

    bids.append({'name': name, 'amount': amount})

    
def get_winner():
    if len(bids) == 0: print("No valid bids, no winner.")

    max_bid = bids[0]['amount']
    winner = "No winner"
    for bid in bids:
        if bid['amount'] > max_bid: 
            max_bid = bid['amount']
            winner = bid['name']
    
    print(f"🌟 The winner is {winner} with a bid of {max_bid}.")



if __name__ == "__main__" :
    main()
