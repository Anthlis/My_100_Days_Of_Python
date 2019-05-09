class Pizza():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print("Pizza created: {} (${}).". format(self.name, self.price))
    
    def make(self, quantity=1):
        print("Made {} {} pizza(s).".format(quantity, self.name))
        
    def eat(self, quantity=1):
        print("Ate {} pizza(s).".format(quantity, self.name))
        
        
pizza_01 = Pizza("Ham and pineapple", 12)
pizza_01.make()
pizza_01.eat()

pizza_02 = Pizza('Pepperoni', 10)
pizza_01.make(2)
pizza_01.eat()