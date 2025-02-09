import art
print(art.logo)
bid_details = {}
condition = True
while condition:

    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))

    # TODO-2: Save data into dictionary {name: price}
    bid_details[name] = price
    # TODO-3: Whether if new bids need to be added
    check_other_bids = input("Are there any other bidders>? Type 'yes' or 'no'.\n").lower()
    print("\n" * 100)


    # TODO-4: Compare bids in dictionary
    def find_highest_bidder(bidding_dictionary):
        highest_bid = 0
        winner = ""
        for bidder in bid_details:
            if bid_details[bidder] > highest_bid:
                winner = bidder
                highest_bid = bid_details[bidder]
        print(f"The winner is {winner} with a bid of ${highest_bid}")


    if check_other_bids == 'no' :
        condition = False
        find_highest_bidder(bid_details)


