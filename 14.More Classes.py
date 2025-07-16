class Mobile:
    def __init__(self):
        self.model = 'Apple'
    def set_model(self, model):
        self.model = 'Banana'

realme = Mobile()
print(realme.model)
realme.set_model("Realme 7 Pro")
print(realme.model)

class Mobile:
    @classmethod
    def show_model(cls):
        print("Realme X")

realme = Mobile()
realme.show_model()

# need a class variable and acces it inside the fucntion and display outside the class using class method

class Mobile:
    model = 'Nothing Phone 1'

    @classmethod
    def show_model(cls):
        print(cls.model)
realme = Mobile()
realme.show_model()


# staticmethod
class Mobile:
    @staticmethod
    def show_model():
        print("Apple iPhone 14")
        print(Mobile.model)

realme = Mobile()
realme.show_model()