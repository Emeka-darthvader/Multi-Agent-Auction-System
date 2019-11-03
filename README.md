# Multi-Agent Auction System
Auction System for English and Dutch Auction

To run the system, kindly run the ticket_auction.py file

1. The  ticket_auction.py file lets you define the utility of each bidder. Utility is a variable that captures various factos like the price ceiling, bank capacity and their will power. You can also set the auctioneers price there.
2. The auction_env.py file sets the environment variable for the auction including the time constraints
3. The message.py defines the messaging protocols and content sent between bidders and auctioneers.
4. The auctioneer.py and bidder.py files details actions available to auctioneers and bidders respectively
5. Multiple bids can take place at the same time. To enable / disable multithreading kindly check the ticket_auction.py file
