# import socket 
# import asyncio

# HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
# PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

class Auctioneer:
    def __init__(self,product_id,product_price):
        self.product_id = product_id
        self.product_price = product_price
        #self.sales_product_price = product_price  - (product_price * 0.20)

    def broadcast_message(self,auction):
                
        #add the ontology too ! "performative" , declarative, blahblha
        # product id, product price , prototype name,

        if auction == "english":
            
            #initial_decrease_percentage = 0.20
            initial_decrease_percentage = 0.80
            starting_price  = self.product_price  - (initial_decrease_percentage * self.product_price)
            broadcast = str(starting_price)+":" + "auction of " +self.product_id+ " started :"+ auction +":" + "performative"


        elif auction == "dutch":
            
            initial_increase_percentage = 0.50
            starting_price  = self.product_price  + (initial_increase_percentage * self.product_price)
            broadcast = str(starting_price)+":" + "auction of " +self.product_id+ " started :"+ auction +":" + "performative"

        # print("broad-auc")
        # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #     s.bind((HOST, PORT))
        #     s.listen()
        #     conn, addr = s.accept()
        #     with conn:
        #         print('Connected by', addr)
        #         while True:
        #             data = conn.recv(1024)
        #             if not data:
        #                 break
        #             conn.sendall(data)
        
        return broadcast

    def interact(self,highest_price,auction,no_of_participants=3):
        if no_of_participants >= 3 and auction == "english":
            
            #initial_decrease_percentage = 0.1
            price_increase_percentage = 0.10

            new_price = highest_price + (highest_price * price_increase_percentage)
            message = str(new_price)+":" + "continuing auction of " +self.product_id+ ":"+ auction +":" + "performative"

        elif no_of_participants < 3 and auction == "english":
            #initial_decrease_percentage = 0.1
            price_increase_percentage = 0.12
            new_price = highest_price + (highest_price * price_increase_percentage)
            message = str(new_price)+":" + "auction of " +self.product_id+ " started :"+ auction +":" + "performative"


        if no_of_participants > 3 and auction == "dutch":
            #initial_increase_percentage = 0.1
            price_decrease_percentage = 0.12
            new_price = highest_price - (highest_price * price_decrease_percentage)
            message = str(new_price)+":" + "auction of " +self.product_id+ " started :"+ auction +":" + "performative"

        elif no_of_participants < 3 and auction == "dutch":
            #initial_increase_percentage = 0.1
            price_decrease_percentage = 0.15
            new_price = highest_price - (highest_price * price_decrease_percentage)
            message = str(new_price)+":" + "auction of " +self.product_id+ " started :"+ auction +":" + "performative"


        # if auction == "english":
        #     print("English auction")
        # elif auction == "dutch":
        #     print("Dutch auction")

        return message

    def broadcast_end_of_auction (self,winner,amount,FIPAProtocol):
        #message = "The agent" + winner + "is the winner of this product"+ "with amount" + str(amount)
        broadcast = str(amount)+":" + "auction of " +self.product_id+ " completed : winner->"+"Agent "+str(winner)+":"+ FIPAProtocol
        return broadcast

    def request_payment (self,winner,amount,FIPAProtocol):
        #message = "The agent" + winner + "is the winner of this product"+ "with amount" + str(amount)
        broadcast = str(amount)+":" + "auction of " +self.product_id+ " completed : requesting paymeny from winner->"+"Agent "+str(winner)+":"+ FIPAProtocol
        return broadcast
        