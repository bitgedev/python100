class Car:
    # self는 만들어지고있는.초기화되고 있는 객체
    def __init__(self, seats):
        self.seats = seats
my_car = Car(5) #my_car.seats는 5
print(my_car.seats)

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self, user): #self 매개변수가 있어야한다.
        user.followers += 1
        self.following += 1

user_1 = User("001", "goeun")
user_2 = User("002", "jack")

user_1.follow(user_2)

print(user_1.following)
print(user_2.followers)