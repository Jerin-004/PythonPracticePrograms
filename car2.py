class Car: 

    Wheels = 4  ## Class variable is declared inside the class but outside the constructer
     
    def __init__(self,company,model,year,color):    
        self.company = company  ## instance variable      ## these variable declared inside the constructor are known as instance variables and each object can have their own unique values assinged to each os these variables
        self.model = model      ## instance variable          
        self.year = year        ## instance variable  
        self.color = color      ## instance variable  