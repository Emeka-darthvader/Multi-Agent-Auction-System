class Message:
    def __init__(self,content,product_id,auctioneer,bidders,messageType,FCLprototype):
        self.content =  content
        self.auctioneer =  auctioneer
        self.bidders =  bidders
        self.messageType =  messageType
        self.FCLprototype =  FCLprototype
        self.product_id = product_id

    def communicate(self):
        if self.messageType == "broadcast":
            print("("+ self.product_id +")" +"sending "+self.messageType+ "...")
        elif self.messageType == "message":
            print("("+ self.product_id +")" +"sending "+self.messageType+ "...")
        
        bids = []
        

        
        contentSplit = self.content.split(":")
        
        #print("contentSplit",contentSplit)
        price = contentSplit[0]
        content = contentSplit[1]
        auction_type = contentSplit[2]
        fipa_protocol  = contentSplit[3]
        
        if self.messageType == "message":
            print("sending --> " + content)



        for bidder in self.bidders:
            bidders_bid = bidder.interact(self.content,auction_type,price,fipa_protocol)
            bids.append(bidders_bid)
        
        

        #print("bids",bids)
        #remember bis are [x,y]  where x is bid and y is bidder
        return bids

    def inform(self):
        if self.messageType == "broadcast":
            print("("+ self.product_id +")" +"sending "+self.messageType+ "...")

        contentSplit = self.content.split(":")
        
        #print("contentSplit",contentSplit)
        highest_bid = contentSplit[0]
        #content = contentSplit[1]
        #winner  = contentSplit[2]
        fipa_protocol = contentSplit[3]
        
        
        for bidder in self.bidders:
            #bidder.interact(self.content,auction_type,price,fipa_protocol)
            bidder.interact(self.content,"eng/dutch",highest_bid,fipa_protocol)
    
    def request(self,agent_id):
        if self.messageType == "message":
            print("("+ self.product_id +")" +"sending "+self.messageType+ "...")
        
        contentSplit = self.content.split(":")
        #print("contentSplit",contentSplit)
        highest_bid = contentSplit[0]
        #content = contentSplit[1]
        #winner  = contentSplit[2]
        fipa_protocol = contentSplit[3]
        
        #print ("agent_id",agent_id)
        self.bidders[agent_id].interact(self.content,"eng/dutch",highest_bid,fipa_protocol,agent_id)
            
        