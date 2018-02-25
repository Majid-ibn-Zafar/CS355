from enum import Enum
from random import randint


class Light(Enum):
    LEFT = 1
    GREEN = 2
    RED = 3


class Intersection:
    def __init__(self, left_time, green_time, red_time):
        rand = randint(1, 3)
        if rand == 1:
            self.light = Light.LEFT
        elif rand == 2:
            self.light = Light.GREEN
        else:
            self.light = Light.RED

        self.left_time = left_time
        self.green_time = green_time
        self.red_time = red_time
        self.time_on_light = 0

    def update(self):
        if self.light == Light.LEFT and self.time_on_light == self.left_time:
            self.light = Light.GREEN
            self.time_on_light = 0
        elif self.light == Light.GREEN and self.time_on_light == self.green_time:
            self.light = Light.RED
            self.time_on_light = 0
        elif self.light == Light.RED and self.time_on_light == self.red_time:
            self.light = Light.LEFT
            self.time_on_light = 0
        else:
            self.time_on_light += 1


class Car:
    def __init__(self, current_intersection):
        self.current_intersection = current_intersection

# Right turn allowed at stop, adds 5 seconds
# Left turn allowed at green, 50% chance to add 10 seconds

# Strategy 1: Always turn left at four
total_time_one = 0
for _ in range(10000):
    one = Intersection(10, 40, 40)
    two = Intersection(15, 30, 50)
    three = Intersection(15, 55, 30)
    four = Intersection(10, 40, 35)

    travel_time = 0
    car = Car(four)

    while True:
        # Left turn on left light at four
        if car.current_intersection is four and four.light is Light.LEFT:
            car.current_intersection = three
            travel_time += 1

        # Left turn on green light at four
        elif car.current_intersection is four and four.light is Light.GREEN:
            if randint(0, 1) == 0:
                travel_time += 10
            else:
                travel_time += 1
            car.current_intersection = three

        # right turn on green light at three
        elif car.current_intersection is three and three.light is Light.GREEN:
            car.current_intersection = one
            travel_time += 1

        # right turn on red light at three
        elif car.current_intersection is three and three.light is Light.RED:
            car.current_intersection = one
            travel_time += 5

        # finish on green light at one
        elif car.current_intersection is one and one.light is Light.GREEN:
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
    one = Intersection(10, 40, 40)
    two = Intersection(15, 30, 50)
    three = Intersection(15, 55, 30)
    four = Intersection(10, 40, 35)

    travel_time = 0
    car = Car(four)

    while True:
        # Straight at green light at four
        if car.current_intersection is four and four.light is Light.GREEN:
            car.current_intersection = two
            travel_time += 1

        # Left at left light at two
        elif car.current_intersection is two and two.light is Light.LEFT:
            car.current_intersection = one
            travel_time += 1

        # Left at green light at two
        elif car.current_intersection is two and two.light is Light.GREEN:
            if randint(0, 1) == 0:
                travel_time += 10
            else:
                travel_time += 1
            car.current_intersection = one

        # Finish at green light at one
        elif car.current_intersection is one and one.light is Light.GREEN:
            travel_time += 1
            total_time_two += travel_time
            break

        # Finish at red light at one
        elif car.current_intersection is one and one.light is Light.RED:
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
    one = Intersection(10, 40, 40)
    two = Intersection(15, 30, 50)
    three = Intersection(15, 55, 30)
    four = Intersection(10, 40, 35)

    travel_time = 0
    from_two = False
    car = Car(four)

    while True:
        # Go straight at four if green
        if car.current_intersection is four and four.light is Light.GREEN:
            car.current_intersection = two
            travel_time += 1

        # Go left at two if left
        elif car.current_intersection is two and two.light is Light.LEFT:
            car.current_intersection = one
            from_two = True
            travel_time += 1

        # Go left at two if green
        elif car.current_intersection is two and two.light is Light.RED:
            if randint(0, 1) == 0:
                travel_time += 10
            else:
                travel_time += 1
            from_two = True
            car.current_intersection = one

        # Exit at one if green
        elif car.current_intersection is one and one.light is Light.GREEN:
            travel_time += 1
            total_time_three += travel_time
            break

        # Exit at one if red (coming from two)
        elif car.current_intersection is one and one.light is Light.RED and from_two:
            travel_time += 5
            total_time_three += travel_time
            break

        # Go left at four if left
        elif car.current_intersection is four and four.light is Light.LEFT:
            travel_time += 1
            car.current_intersection = three

        # Go right at three if green
        elif car.current_intersection is three and three.light is Light.GREEN:
            travel_time += 1
            car.current_intersection = one

        # Go right at three if red, exit at one if green already defined
        elif car.current_intersection is three and three.light is Light.RED:
            travel_time += 5
            car.current_intersection = one

        else:
            travel_time += 1

        one.update()
        two.update()
        three.update()
        four.update()

print("Strategy 3 (straight if green, otherwise left): " + str(total_time_three/10000))