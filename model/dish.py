class Dish:

    def __init__(self, name, description, image, price, category):
        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.category = category

    def print(self):
        print("name: " + self.name)
        print("description: " + self.description)
        print("image: " + self.image)
        print("price: " + str(self.price))
        print("category: " + self.category)