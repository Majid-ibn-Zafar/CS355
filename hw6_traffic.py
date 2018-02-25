from enum import Enum
from random import randint


class Light(Enum):
    Left = 1
    Green = 2
    Red = 3


class Intersection:
    def __init__(self, name, left_time, green_time, red_time):

        self.name = name
        self.light = Light(randint(1, 3))
        self.left_time = left_time
        self.green_time = green_time
        self.red_time = red_time

        if self.light is Light.Left:
            self.time_on_light = randint(0, self.left_time)
        elif self.light is Light.Green:
            self.time_on_light = randint(0, self.green_time)
        else:
            self.time_on_light = randint(0, self.red_time)

    def __str__(self):
        return "Intersection " + self.name + ": " + self.light.name + " for " + str(self.time_on_light) + " seconds."

    def update(self):
        if self.light == Light.Left and self.time_on_light == self.left_time:
            self.light = Light.Green
            self.time_on_light = 0
        elif self.light == Light.Green and self.time_on_light == self.green_time:
            self.light = Light.Red
            self.time_on_light = 0
        elif self.light == Light.Red and self.time_on_light == self.red_time:
            self.light = Light.Left
            self.time_on_light = 0
        else:
            self.time_on_light += 1


class Car:
    def __init__(self, current_intersection):
        self.current_intersection = current_intersection

    def __str__(self):
        return "Currently at intersection " + self.current_intersection.name + "."

# Right turn allowed at stop (red or left), adds 5 seconds
# Left turn allowed at green, 50% chance to add 10 seconds


# Strategy 1: Always turn left at four
total_time_one = 0
for _ in range(10000):
    one = Intersection('1', 10, 40, 40)
    two = Intersection('2', 15, 30, 50)
    three = Intersection('3', 15, 55, 30)
    four = Intersection('4', 10, 40, 35)

    travel_time = 0
    car = Car(four)

    while True:
        # Left turn on left light at four
        if car.current_intersection is four and four.light is Light.Left:
            car.current_intersection = three
            travel_time += 1

        # Left turn on green light at four
        elif car.current_intersection is four and four.light is Light.Green:
            if randint(0, 1) == 0:
                travel_time += 10
            else:
                travel_time += 1
            car.current_intersection = three

        # right turn on green light at three
        elif car.current_intersection is three and three.light is Light.Green:
            car.current_intersection = one
            travel_time += 1

        # right turn on not green light at three
        elif car.current_intersection is three and three.light is not Light.Green:
            car.current_intersection = one
            travel_time += 5

        # finish on green light at one
        elif car.current_intersection is one and one.light is Light.Green:
            travel_time += 1
            total_time_one += travel_time
            break

        else:
            travel_time += 1

        one.update()
        two.update()
        three.update()
        four.update()

print("Strategy 1 (always left at 4): " + str(total_time_one/10000))


# Strategy 2: Always go straight at four
total_time_two = 0
for _ in range(10000):
    one = Intersection('1', 10, 40, 40)
    two = Intersection('2', 15, 30, 50)
    three = Intersection('3', 15, 55, 30)
    four = Intersection('4', 10, 40, 35)

    travel_time = 0
    car = Car(four)

    while True:
        # Straight at green light at four
        if car.current_intersection is four and four.light is Light.Green:
            car.current_intersection = two
            travel_time += 1

        # Left at left light at two
        elif car.current_intersection is two and two.light is Light.Left:
            car.current_intersection = one
            travel_time += 1

        # Left at green light at two
        elif car.current_intersection is two and two.light is Light.Green:
            if randint(0, 1) == 0:
                travel_time += 10
            else:
                travel_time += 1
            car.current_intersection = one

        # Finish at green light at one
        elif car.current_intersection is one and one.light is Light.Green:
            travel_time += 1
            total_time_two += travel_time
            break

        # Finish at not green at one
        elif car.current_intersection is one and one.light is not Light.Green:
            travel_time += 5
            total_time_two += travel_time
            break

        else:
            travel_time += 1

        one.update()
        two.update()
        three.update()
        four.update()

print("Strategy 2 (always straight at 4): " + str(total_time_two/10000))

# Strategy 3: Go straight if green, otherwise turn left
total_time_three = 0
for _ in range(10000):
    one = Intersection('1', 10, 40, 40)
    two = Intersection('2', 15, 30, 50)
    three = Intersection('3', 15, 55, 30)
    four = Intersection('4', 10, 40, 35)

    travel_time = 0
    from_two = False
    car = Car(four)

    while True:
        # Go straight at four if green
        if car.current_intersection is four and four.light is Light.Green:
            car.current_intersection = two
            travel_time += 1

        # Go left at two if left
        elif car.current_intersection is two and two.light is Light.Left:
            car.current_intersection = one
            from_two = True
            travel_time += 1

        # Go left at two if green
        elif car.current_intersection is two and two.light is Light.Green:
            if randint(0, 1) == 0:
                travel_time += 10
            else:
                travel_time += 1
            from_two = True
            car.current_intersection = one

        # Exit at one if green
        elif car.current_intersection is one and one.light is Light.Green:
            travel_time += 1
            total_time_three += travel_time
            break

        # Exit at one if not green (coming from two)
        elif car.current_intersection is one and one.light is not Light.Green and from_two:
            travel_time += 5
            total_time_three += travel_time
            break

        # Go left at four if left
        elif car.current_intersection is four and four.light is Light.Left:
            travel_time += 1
            car.current_intersection = three

        # Go right at three if green
        elif car.current_intersection is three and three.light is Light.Green:
            travel_time += 1
            car.current_intersection = one

        # Go right at three if not green
        elif car.current_intersection is three and three.light is not Light.Green:
            travel_time += 5
            car.current_intersection = one

        # exit at one if green is already defined
        else:
            travel_time += 1

        one.update()
        two.update()
        three.update()
        four.update()

print("Strategy 3 (straight if green, otherwise left): " + str(total_time_three/10000))
