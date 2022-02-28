class Item:
    def __init__(self):
        self.name = input("Name: ")
        print(self.name)
    def calculate_total_price(self,x,y):
        print(x*y)

item = Item()
item.price = 100
item.quantity = 5
item.calculate_total_price(item.price, item.quantity)