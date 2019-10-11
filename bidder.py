# import socket
# import asyncio

#HOST = '127.0.0.1'  # The server's hostname or IP address
#PORT = 65432        # The port used by the server

import random


class Bidder:
    def __init__(self,product_id,price_ceiling,bank_capacity,will_power):
        self.product_id = product_id
        self.price_ceiling = price_ceiling
        self.bank_capacity = bank_capacity
        self.will_power = will_power
    
    def interact(self,message,auction,currentPrice,FIPAProtocol,agent_id=0):
        
        if FIPAProtocol == "performative":
            if  auction == "english":
                if self.will_power == 1 :
                    #sting-o-meter level 1
                    price_increase_percentage = round(random.uniform(0.02,0.03),2)

                elif self.will_power == 2 :
                    #sting-o-meter level 2
                    price_increase_percentage = round(random.uniform(0.08,0.09),2)

                elif self.will_power == 3 :
                    #sting-o-meter level 3
                    price_increase_percentage = round(random.uniform(0.12,0.13),2)

                elif self.will_power == 4 :
                    #sting-o-meter level 4
                    price_increase_percentage = round(random.uniform(0.15,0.17),2)
                
                currentPrice = float(currentPrice)
                if currentPrice < self.price_ceiling :
                    bid  =  currentPrice + (price_increase_percentage * currentPrice)
                    bid = int(bid)

                elif currentPrice >= self.price_ceiling :
                    bid  =  self.price_ceiling
                    bid = int(bid)
                
                
            if auction == "dutch":            
                #price_decrease_percentage = 0.15
                if self.will_power == 1 :
                    #sting-o-meter level 1
                 price_decrease_percentage = round(random.uniform(0.15,0.17),2)   

                elif self.will_power == 2 :
                    #sting-o-meter level 2
                    price_decrease_percentage = round(random.uniform(0.12,0.13),2)

                elif self.will_power == 3 :
                    #sting-o-meter level 3
                    
                    price_decrease_percentage = round(random.uniform(0.08,0.09),2)

                elif self.will_power == 4 :
                    #sting-o-meter level 4
                    
                    price_decrease_percentage = round(random.uniform(0.02,0.03),2)
                
                currentPrice = float(currentPrice)
                if currentPrice < self.price_ceiling :
                    bid  =  currentPrice - (price_decrease_percentage * currentPrice)
                    bid = int(bid)
                elif currentPrice >= self.price_ceiling :
                    bid  =  self.price_ceiling
                    bid = int(bid)


            return bid

        elif FIPAProtocol == "inform":
            print("received message -->" + message )

            #return message
        elif FIPAProtocol == "request":
            print("Transferring money to account")             
            print("Purchase Ceiling-- ",self.price_ceiling)   
            print("Initial Bank Balance-- ",self.bank_capacity)    
            current_balance  = self.bank_capacity - int(currentPrice) 
            current_utility  = self.price_ceiling - int(currentPrice)   
            print("Amount  Paid-- ",currentPrice)
            print("Final Bank Balance-- ",current_balance)
            print("Utility (Initial Ceiling - Price bought) = ",current_utility)
            
            
            #print("broad-bid")
            # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #     s.connect((HOST, PORT))
            #     s.sendall(b'Hello, world')
            #     data = s.recv(1024)

            # print('Received', repr(data))
            
                
        
            # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #     s.connect((HOST, PORT))
            #     s.sendall(b'Hello, world')
            #     data = s.recv(1024)

            # print('Received', repr(data))
           
                
        #if auction == "english":
        #    print("English auction")
        #elif auction == "dutch":
        #    print("Dutch auction")
    