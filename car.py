class Car: ## works as an blue print
    
     ## attributes -  what describes an object is or has 
    def __init__(self,company,model,year,color):    ## constructs object for us
        self.company = company         ## self refers to the object that we are currently we working on
        self.model = model              
        self.year = year
        self.color = color

    ## method - what each object can do
    def drive(self):                          ## these are the methods
        print("This",self.model,"is drivivng")       

    def stop(self):
        print("This",self.model ,"is stopped")   ## in this place self refers to the variable that we are using which is replaced
