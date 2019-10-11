from auction_env import Auction_env
from auctioneer import Auctioneer
from bidder import Bidder
import random

import threading

#put the code for multithreading and instantiation of the auctioneers and different bidders

##ticket one
#generate bidder

auctioneer_agent1 = Auctioneer('ticket1',1000)


#generate the different  12 agents for ticket  one   -> 3 for each type of sting-0-meter
#generate bidding agents
#bidding agent arguments are product_id,price_ceiling,bank_capacity,will_power

bidding_agents1 = []
#random agents will power 1 
for i in range(3):
    #bidding_agents.append(Bidder('ticket1',random.randint(995,1000),random.randint(990,1100),1))
    bidding_agents1.append(Bidder('ticket1',1200,2000,1))

#random agents will power 2
for i in range(3):
    #bidding_agents.append(Bidder('ticket1',random.randint(995,1000),random.randint(990,1100),2))
    bidding_agents1.append(Bidder('ticket1',1300,2000,2))

#random agents will power 3 
for i in range(3):
    #bidding_agents.append(Bidder('ticket1',random.randint(995,1000),random.randint(990,1100),3))
    bidding_agents1.append(Bidder('ticket1',1500,1900,3))

#random agents will power 4 
for i in range(3):
    #bidding_agents.append(Bidder('ticket1',random.randint(995,1000),random.randint(990,1100),4))
    bidding_agents1.append(Bidder('ticket1',1500,2500,4))


#run auction using the bidder and the agents
#comment this line and uncomment the lines below to witness multithreading instantiated with 4 auctions 
# the 4 auctions here include the 1 up already

# auction1 = Auction_env(auctioneer_agent,bidding_agents)
# auction1.execute_auction()





####uncomment to test multithreading 

##***********************************************************************
##ticket two
#generate bidder

auctioneer_agent2 = Auctioneer('ticket2',1000)


#generate the different agents for ticket  two  (8 - 2 for each type of sting-0-meter)
#generate bidding agents
#bidding agent arguments are product_id,price_ceiling,bank_capacity,will_power

bidding_agents2 = []
#random agents will power 1 
for i in range(3):
    #bidding_agents.append(Bidder('ticket1',random.randint(995,1000),random.randint(990,1100),1))
    bidding_agents2.append(Bidder('ticket2',1200,2000,1))

#random agents will power 2
for i in range(3):
    #bidding_agents.append(Bidder('ticket1',random.randint(995,1000),random.randint(990,1100),2))
    bidding_agents2.append(Bidder('ticket2',1300,2000,2))

#random agents will power 3 
for i in range(3):
    #bidding_agents.append(Bidder('ticket1',random.randint(995,1000),random.randint(990,1100),3))
    bidding_agents2.append(Bidder('ticket2',1500,1700,3))

#random agents will power 4 
for i in range(3):
    #bidding_agents.append(Bidder('ticket1',random.randint(995,1000),random.randint(990,1100),4))
    bidding_agents2.append(Bidder('ticket2',1500,2500,4))




##***********************************************************************
##ticket three
#generate bidder

auctioneer_agent3 = Auctioneer('ticket3',1000)


#generate the different agents for ticket  three  (8 - 2 for each type of sting-0-meter)
#generate bidding agents
#bidding agent arguments are product_id,price_ceiling,bank_capacity,will_power

bidding_agents3 = []
#random agents will power 1 
for i in range(3):
    #bidding_agents.append(Bidder('ticket1',random.randint(995,1000),random.randint(990,1100),1))
    bidding_agents3.append(Bidder('ticket3',1200,2000,1))

#random agents will power 2
for i in range(3):
    #bidding_agents.append(Bidder('ticket1',random.randint(995,1000),random.randint(990,1100),2))
    bidding_agents3.append(Bidder('ticket3',1300,2000,2))

#random agents will power 3 
for i in range(3):
    #bidding_agents.append(Bidder('ticket1',random.randint(995,1000),random.randint(990,1100),3))
    bidding_agents3.append(Bidder('ticket3',1500,1750,3))

#random agents will power 4 
for i in range(3):
    #bidding_agents.append(Bidder('ticket1',random.randint(995,1000),random.randint(990,1100),4))
    bidding_agents3.append(Bidder('ticket3',1500,2500,4))



##***********************************************************************
##ticket four
#generate bidder

auctioneer_agent4 = Auctioneer('ticket4',1000)


#generate the different agents for ticket  four  (8 - 2 for each type of sting-0-meter)
#generate bidding agents
#bidding agent arguments are product_id,price_ceiling,bank_capacity,will_power

bidding_agents4 = []
#random agents will power 1 
for i in range(3):
    #bidding_agents.append(Bidder('ticket1',random.randint(995,1000),random.randint(990,1100),1))
    bidding_agents4.append(Bidder('ticket4',1200,2000,1))

#random agents will power 2
for i in range(3):
    #bidding_agents.append(Bidder('ticket1',random.randint(995,1000),random.randint(990,1100),2))
    bidding_agents4.append(Bidder('ticket4',1300,2000,2))

#random agents will power 3 
for i in range(3):
    #bidding_agents.append(Bidder('ticket1',random.randint(995,1000),random.randint(990,1100),3))
    bidding_agents4.append(Bidder('ticket4',1500,1950,3))

#random agents will power 4 
for i in range(3):
    #bidding_agents.append(Bidder('ticket1',random.randint(995,1000),random.randint(990,1100),4))
    bidding_agents4.append(Bidder('ticket4',1500,2500,4))





#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#
#running the multithreading part
auction1 = Auction_env(auctioneer_agent1,bidding_agents1)
auction2 = Auction_env(auctioneer_agent2,bidding_agents2)
auction3 = Auction_env(auctioneer_agent3,bidding_agents3)
auction4 = Auction_env(auctioneer_agent4,bidding_agents4)

auction1.execute_auction()


t1 = threading.Thread(target=auction1.execute_auction)
t2 = threading.Thread(target=auction2.execute_auction)
t3 = threading.Thread(target=auction3.execute_auction)
t4 = threading.Thread(target=auction4.execute_auction)


t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$