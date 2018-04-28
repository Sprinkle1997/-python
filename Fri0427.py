class Things:
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    pass
class Animals(Animate):
    pass
class Mammals(Animals):
    pass
class Giraffes(Animals):
    pass
reginald=Giraffes()
def this_is_a_normal_function():
    print('i am a normal function')

class ThisIsMySillyClass:
    def this_is_a_class_function():
        print('i am a class function')
    def this_is_also_a_class_functiong():
        print('i am also a class function.see')
#print('dfhgs')
class Animals(Animate):
    def breathe(self):
        pass
    def move(self):
        pass
    def eat_food(self):
        pass
class Mammals(Animals):
    def feed_young_with_milk(self):
        pass
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        pass
reginald=Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()
harold=Giraffes()
class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')
class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('eating leaves')
harold=Giraffes()
reginald=Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()
class Giraffes(Mammals):
    def find_food(self):
        self.move()
        print('ive found food')
        self.eat_food()

harold=Giraffes()
harold.find_food()


class Giraffes:
    def __init__(self,spots):
        self.giraffes_spots=spots
ozwald=Giraffes(100)
print(ozwald.giraffes_spots)

