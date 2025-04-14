class Product:
    def __init__(self,id,name):  
        self.id = id
        self.name = name

    def display(self):    
        print(f"Product ID: {self.id} , Product name: {self.name}")


class Product_A(Product):
    def __init__(self, id, name,count,category):
        super().__init__(id, name)
        self.count = count
        self.category = category

    def display(self):
        super().display()
        print(f"Product ID: {self.id} , Product name: {self.name} , Product count: {self.count} , product catagary : {self.category}")


class Product_SUB_A(Product_A):
    def __init__(self, id, name, count, category,price):
        super().__init__(id, name, count, category)
        self.price = price

    def display(self):
        super().display()
        print(f"Product ID: {self.id} , Product name: {self.name} , product catagary : {self.category}")
        print(f"Total price {self.count * self.price}")


firstProduct = Product_SUB_A(1,"Laptop",15,"Electronics",45000)
firstProduct.display()

print('----------------------------------------------------------------------------')

class Product_B(Product):
    def __init__(self, id, name,count,category):
        super().__init__(id, name)
        self.count = count
        self.category = category

    def display(self):
        super().display()
        print(f"Product ID: {self.id} , Product name: {self.name} , Product count: {self.count} , product catagary : {self.category}")

class Product_SUB_B(Product_B):
    def __init__(self, id, name, count, category,price):
        super().__init__(id, name, count, category)
        self.price = price

    def display(self):
        super().display()
        print(f"Product ID: {self.id} , Product name: {self.name} , product catagary : {self.category}")
        print(f"Total price {self.count * self.price}")

secondProduct = Product_SUB_B(2,"Mobile",10,"Smartphones",20000)
secondProduct.display()


print('----------------------------------------------------------------------------')
class Product_C(Product):
    def __init__(self, id, name,count,category):
        super().__init__(id, name)
        self.count = count
        self.category = category

    def display(self):
        super().display()
        print(f"Product ID: {self.id} , Product name: {self.name} , Product count: {self.count} , product catagary : {self.category}")

tProduct = Product_C(3,"Milk",100,"Dairy")
tProduct.display()
