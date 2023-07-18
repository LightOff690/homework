class Product:
    def __init__(self, name='t-shirt', type_p='clothes', cost=100):
        if type_p not in ['одежда', 'обувь', 'украшение']:
            raise ValueError('type is not одежда, обувь, украшение')
        if cost < 0:
            raise ValueError('cost is below zero')
        if not isinstance(cost, (int, float)):
            raise ValueError('cost is not int or float')
        
        self.__name = name
        self.__type = type_p
        self.__cost = cost

    def show(self):
        print(self.__name, self.__type, self.__cost)

class ShoppingCart:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def remove_product(self, product):
        self.__products.remove(product)

    def calculate_total_cost(self):
        total_cost = 0
        for product in self.__products:
            total_cost += product._Product__cost  # Accessing private attribute directly
        return total_cost

# Example usage
product1 = Product('Jeans', 'одежда', 200)
product2 = Product('Shoes', 'обувь', 150)
product3 = Product('Necklace', 'украшение', 50)

cart = ShoppingCart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

print(cart.calculate_total_cost())  # Output: 400
