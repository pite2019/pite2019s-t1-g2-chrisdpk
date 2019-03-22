# Write a module that will simulate autonomic car.
# The simulation is event based, an example:
# car1 = Car()
# car1.act(event)
# print(car1.wheel_angle, car1.speed)
# where event can be anything you want, i.e. :
# `('obstacle', 10)` where `10` is a duration (time) of the event.
##The program should:
# - act on the event
# - print out current steering wheel angle, and speed
# - run in infinite loop
# - until user breaks the loop

#The level of realism in simulation is of your choice, but more sophisticated solutions are better.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to github repository.
#
#Delete these comments before commit!
#Good luck.
import time
class Event(object):
    name = ""
    seconds_away = 0
    avoidable = None

    def __init__(self, name="Unknown", seconds_away=0, avoidable=True):
        self.name = name
        self.seconds_away = seconds_away
        self.avoidable = avoidable
    def __repr__(self):
        return "<Event {}, {} seconds away, avoidable = {}>".format(self.name,
        self.seconds,self.avoidable)

class Car(object):
    wheel_angle = 0
    speed = 80
    event_queue = []

    def __init__(self):
        self.wheel_angle = 0
        self.speed = 80

    def tick(self):
        if not self.event_queue:
            pass
        else:

            if self.event_queue[0].seconds_away < 3:
                self.act(self.event_queue.pop())
            for i in self.event_queue:
                self.event_queue[i].seconds_away -= 1

    def act(self,event):
        if event.avoidable:
            self.steer("right")
            print("Argggggh.. Avoiding {}".format(event.name))

        else:
            print("{} was unavoidable, so we had to stop.".format(event.name))
            self.stop()

    def plan_event(self,event):
        print("We can see {} in the fog that is {} seconds away.".format(event.name, event.seconds_away))
        self.event_queue.append(event)

    def stop(self):
        self.speed = 0

    def steer(self,dir):
        if dir == "left":
            self.wheel_angle = (self.wheel_angle - 20) % 360
        elif dir == "right":
            self.wheel_angle = (self.wheel_angle + 20) % 360

    def __repr__(self):
        return "Driving at {} km/h, steering {}°".format(self.speed, self.wheel_angle)

def main():
    car1 = Car()
    dog = Event("Dog on the road", 6, avoidable=True)
    wall = Event("Great Wall of China", 20, avoidable=False)
    car1.plan_event(wall)
    car1.plan_event(dog)
    print(car1)
    car1.steer("right")
    print(car1)
    car1.steer("right")
    print(car1)
    car1.steer("left")
    print(car1)

    while True:
        print(car1)
        time.sleep(1)




if __name__ == '__main__':
    main()
