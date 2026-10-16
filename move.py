"""Mission 4: exploding seeds 
R: left orange "L" part lined up with first major line
A: Forks
P: 1
"""
#go from right lunch to lft lunch doing the sunroof on the way

from robot import Robot, inches, Speed
from pybricks.tools import wait
from pybricks.parameters import Stop

def run(robot):
    robot.drive_base.settings(straight_speed=Speed.FAST)
    robot.drive_base.straight(inches (75))

 
# Lets you run JUST this mission: open this file and press F5.
if __name__ == "__main__":
    run(Robot())
