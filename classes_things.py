
class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print('дышит')
    def move(self):
        print('двигается')
    def eat_food(self):
        print('ест')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('кормит детенышей молоком')

class Giraffes(Mammals):

    def __init__(self, spots):
        self.giraffe_spots = spots

    def eat_leaves_from_trees(self):
        print('ест листья')

    def find_food(self):
        self.move()
        print("Я нашел еду!")
        self.eat_food()

    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()

    def left_foot_forward(self):
        print('левая нога впереди')

    def left_foot_back(self):
        print('левая нога позади')

    def right_foot_forward(self):
        print('правая нога впереди')

    def right_foot_back(self):
        print('левая нога позади')

    def new_dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_back()
        self.right_foot_back()
        self.right_foot_forward()
        self.left_foot_forward()


reginald = Giraffes(100)
harold = Giraffes(150)

reginald.eat_leaves_from_trees()
harold.find_food()
reginald.dance_a_jig()

print(reginald.giraffe_spots)
print(harold.giraffe_spots)

harold.new_dance()