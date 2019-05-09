import logging

logging.basicConfig(
    filename='pizza.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
    )

class Pizza():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        # print("Pizza created: {} (${}).". format(self.name, self.price))
        logging.debug("Pizza created: {} (${}).". format(self.name, self.price))
    
    def make(self, quantity=1):
        # print("Made {} {} pizza(s).".format(quantity, self.name))
        logging.debug("Made {} {} pizza(s).".format(quantity, self.name))
        
    def eat(self, quantity=1):
        # print("Ate {} pizza(s).".format(quantity, self.name))
        logging.debug("Ate {} pizza(s).".format(quantity, self.name))
        
        
pizza_01 = Pizza("Ham and pineapple", 12)
pizza_01.make()
pizza_01.eat()

pizza_02 = Pizza('Pepperoni', 10)
pizza_01.make(5)
pizza_01.eat(2)