import asyncio
from message import Message
import threading

#threadLock = threading.Lock()

class Auction_env:
    def __init__(self,auctioneer,bidders,time_tick=20):
        #super().__init__()
        self.auctioneer = auctioneer
        self.bidders = bidders
        self.time_tick = time_tick

    
    def execute_auction(self):
        winner = [] #the result of the bidding
        product_sold = False 
        bids_and_agents = {}
        bids_and_agents2 = {}
        dutch_bids_and_agents = {}
        dutch_bids_and_agents2 = {}
        highest_bid = 0
        winner_index = []
        winner_index_dutch = []
        agent_number  = 0
        high_low_bid = 0

        no_of_participants  = len(self.bidders)
        #print("no_of_participants",no_of_participants)
        print("@"*20)
        print("participants")
        print("auctioner - product",self.auctioneer.product_id,"auctioner - price",self.auctioneer.product_price)
        print("bidders")

        #threadLock.acquire()

        p = 0 
        for participant in self.bidders:
            print("bidder ",p,"| (",participant.product_id,") will power = ",participant.will_power," -  amount in bank =",participant.bank_capacity, "bidding ceiling = ",participant.price_ceiling)
            p+=1

        while self.time_tick > 0 and product_sold == False:
            if self.time_tick > 10 :
                #highest_bid = 0

                print("******* English Auction **********")
                messageContent = self.auctioneer.broadcast_message("english")
                #print("messageContent",messageContent)
                #print("message Content -", messageContent)
                callForProposal = Message(messageContent,self.auctioneer.product_id,self.auctioneer,self.bidders,"broadcast","performative")
                broadCastbids = callForProposal.communicate()

                #bd_counter = 0
                #for bid in broadCastbids:
                #    bids_and_agents = {bd_counter:broadCastbids[bd_counter]}
                #    bd_counter+=1
                bids_and_agents2 = { i : broadCastbids[i] for i in range(0, len(broadCastbids) ) }

                #print("broadCastbids",broadCastbids)
                if highest_bid != 0:
                    print("&&&&&&&&& highest bid",highest_bid)

                if highest_bid == 0:
                    for bid in  broadCastbids:
                        if bid > highest_bid:
                            highest_bid = bid
            
                #print ("all bids ("+self.auctioneer.product_id+")" , broadCastbids)
                #print ("highest bid ("+self.auctioneer.product_id+")", highest_bid)
                #counter  = 2 
                if highest_bid < self.auctioneer.product_price:
                    
                    #print("step --- ",counter)
                    messageContent1 = self.auctioneer.interact(highest_bid,"english",no_of_participants)
                    callForProposal = Message(messageContent1,self.auctioneer.product_id,self.auctioneer,self.bidders,"message","performative")
                    broadCastbids1 = callForProposal.communicate()
                    bids_and_agents = { i : broadCastbids1[i] for i in range(0, len(broadCastbids1) ) }
                    for bid in  broadCastbids1:
                        if bid > highest_bid:
                            highest_bid = bid
                            print ("**all bids ("+self.auctioneer.product_id+")" , broadCastbids1)
                            print ("**highest bid ("+self.auctioneer.product_id+")", highest_bid)
                    #counter+=1
                
                elif highest_bid >= self.auctioneer.product_price:
                    product_sold = True
                    #bids_and_agents = { i : broadCastbids[i] for i in range(0, len(broadCastbids) ) }
                    #print ("^^ all bids ("+self.auctioneer.product_id+")" , broadCastbids)
                    print("end of auction")
                    print ("highest bid ("+self.auctioneer.product_id+")", highest_bid)
                    #break
                
                #print("*************product sold value --if",product_sold)
                print("*************timetick",self.time_tick)   
                

                #print(broadCastbids)
                #asyncio.run(self.auctioneer.broadcast_message("english"))
                
                #print(a)
                #english auction logic here
                
            elif self.time_tick <= 10:
                print("******* Dutch Auction **********")
                # b=self.auctioneer.broadcast_message("dutch")
                #self.auctioneer.broadcast_message("dutch")
                #print(b)
                #dutch auction logic here
                
                
                messageContent11 = self.auctioneer.broadcast_message("dutch")
                
                callForProposal1 = Message(messageContent11,self.auctioneer.product_id,self.auctioneer,self.bidders,"broadcast","performative")
                broadCastbids1 = callForProposal1.communicate()

                dutch_bids_and_agents2 = { i : broadCastbids1[i] for i in range(0, len(broadCastbids1) ) }
                if high_low_bid != 0:
                    print("&&&&&&&&& highest bid",high_low_bid)
                if highest_bid == 0:
                    for bid in  broadCastbids1:
                        if bid > high_low_bid:
                            highest_bid = bid
            
                # print ("all bids ("+self.auctioneer.product_id+")" , broadCastbids)
                # print ("highest bid ("+self.auctioneer.product_id+")", highest_bid)

                if high_low_bid < self.auctioneer.product_price:
                    # counter  = 2 
                #     print("step --- ",counter)
                    messageContent122 = self.auctioneer.interact(highest_bid,"dutch",no_of_participants)
                    callForProposal1 = Message(messageContent122,self.auctioneer.product_id,self.auctioneer,self.bidders,"message","performative")
                    broadCastbids1 = callForProposal1.communicate()
                    dutch_bids_and_agents = { i : broadCastbids1[i] for i in range(0, len(broadCastbids1) ) }
                    for bid in  broadCastbids1:
                        if bid > high_low_bid:
                            high_low_bid = bid
                            #print ("**all bids ("+self.auctioneer.product_id+")" , broadCastbids)
                            #print ("**highest bid ("+self.auctioneer.product_id+")", highest_bid)
                    #counter+=1
                elif high_low_bid >= self.auctioneer.product_price:
                    product_sold = True
                    
                    # print ("^^ all bids ("+self.auctioneer.product_id+")" , broadCastbids)
                    print("end of auction")
                    print ("highest bid ("+self.auctioneer.product_id+")", high_low_bid)
                print("*************time tick y",self.time_tick)

            self.time_tick -= 1

        #print("product sold value",product_sold)
        #print("all bidss1" ,len(dutch_bids_and_agents))
        #print("all bidss2" ,len(dutch_bids_and_agents2))
        
        if len(bids_and_agents) >= 1:
            for x, y in bids_and_agents.items():    
                 if y == highest_bid:
                     #print(x)
                     winner_index.append(x)
        elif len(bids_and_agents2) >= 1:
            for x, y in bids_and_agents2.items():   
                if y == highest_bid:
                     #print(x)
                    winner_index.append(x)

        if len(dutch_bids_and_agents) >= 1:
            for x, y in dutch_bids_and_agents.items():    
                 if y == high_low_bid:
                     #print(x)
                     winner_index_dutch.append(x)
        elif len(dutch_bids_and_agents2) >= 1:
            for x, y in dutch_bids_and_agents2.items():   
                if y == high_low_bid:
                     #print(x)
                    winner_index_dutch.append(x)
            
        if len(winner_index) > 0:
            pen_length = len(winner_index) - 1
            #print("winner index",winner_index)
            #print("pen_length",pen_length)
            winning_agent_index = winner_index[pen_length]
            agent_number = winner_index[pen_length] + 1 
            #print("winner index", winner_index)
            print("#"*50)
            
            print("WINNER ⭐️ ---The agent number "+ str(agent_number) + " has won the auction for "+self.auctioneer.product_id)
            messageContent3 = self.auctioneer.broadcast_end_of_auction(agent_number,highest_bid,"inform")
            informAgents = Message(messageContent3,self.auctioneer.product_id,self.auctioneer,self.bidders,"broadcast","inform")
            informAgents.inform()

            #print("bidder 10",self.bidders[1])
            messageContent4 = self.auctioneer.request_payment(winning_agent_index,highest_bid,"request")
            requestAgentPayment = Message(messageContent4,self.auctioneer.product_id,self.auctioneer,self.bidders,"message","request")
            requestAgentPayment.request(winning_agent_index)
            print("#"*50)

        elif len(winner_index_dutch) >0:
            pen_length = len(winner_index_dutch) - 1
            #print("winner index",winner_index_dutch)
            #print("pen_length",pen_length)
            winning_agent_index = winner_index_dutch[pen_length]
            agent_number = winner_index_dutch[pen_length] + 1 
            #print("winner index", winner_index)
            print("The agent number "+ str(agent_number) + " has won the auction")
            messageContent3 = self.auctioneer.broadcast_end_of_auction(agent_number,high_low_bid,"inform")
            informAgents = Message(messageContent3,self.auctioneer.product_id,self.auctioneer,self.bidders,"broadcast","inform")
            informAgents.inform()

            #print("bidder 10",self.bidders[1])
            messageContent4 = self.auctioneer.request_payment(winning_agent_index,high_low_bid,"request")
            requestAgentPayment = Message(messageContent4,self.auctioneer.product_id,self.auctioneer,self.bidders,"message","request")
            requestAgentPayment.request(winning_agent_index)


            #threadLock.release()

            

        
        return winner
