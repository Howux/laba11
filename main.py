def one():
    class Restaurant:
        def __init__(self,restaurant_name,cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print("Название ресторана: ",self.restaurant_name ,"\nКухня ресторана: ",self.cuisine_type)
        def open_restaurant(self):
            print("Ресторан открыт к посещению!")
    newRestaurant = Restaurant(input(),input())
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()


def two():
    class Restaurant:
        def __init__(self,restaurant_name,cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print("Название ресторана: ",self.restaurant_name ,"\nКухня ресторана: ",self.cuisine_type)
        def open_restaurant(self):
            print("Ресторан открыт к посещению!")
    newRestaurant = Restaurant(input(),input())
    secondRestaurant=Restaurant(input(),input())
    thirdRestaurant=Restaurant(input(),input())
    newRestaurant.describe_restaurant()
    secondRestaurant.describe_restaurant()
    thirdRestaurant.describe_restaurant()


def three():
    class Restaurant:
        def __init__(self,restaurant_name,cuisine_type,rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating
        def describe_restaurant(self):
            print("Название ресторана: ",self.restaurant_name,"\nКухня ресторана: ",self.cuisine_type,"\nРейтинг",self.rating)
        def open_restaurant(self):
            print("Ресторан открыт к посещению!")
        def change_rating(self,newrating):
            self.rating=newrating

    newRestaurant = Restaurant("Aragawa","Японская",rating=3)
    newRestaurant.describe_restaurant()
    newRestaurant.change_rating(5)
    newRestaurant.describe_restaurant()

# one()
# two()
# three()