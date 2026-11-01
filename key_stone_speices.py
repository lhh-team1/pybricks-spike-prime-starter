"""Mission 1: 
R: Right of first major line + 2 minor back wheels straddleing the first two thick black lines right front wheel in corner
A: Forks
P: 1
"""
#go from right lunch to lft lunch doing the sunroof on the way

from robot import Robot, inches, Speed
from pybricks.tools import wait
from pybricks.parameters import Stop

def run(robot):

    robot.drive_base.settings(straight_speed=Speed.FAST)
    robot.drive_base.turn(87)
    robot.drive_base.straight(inches(8))
    robot.drive_base.turn(-83)
    robot.drive_base.straight(inches(32))
    robot.drive_base.straight(inches(-42))
    robot.drive_base.stop()

# Lets you run JUST this mission: open this file and press F5.
if __name__ == "__main__":
    run(Robot())
