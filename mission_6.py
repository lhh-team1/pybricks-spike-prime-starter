"""Mission 1: 
R: Right of first major line + 2 minor back wheels straddleing the first two thick black lines right front wheel in corner
A: Forks
P: 1
"""


from robot import Robot, inches, Speed
from pybricks.tools import wait
from pybricks.parameters import Stop

def run(robot):
 robot.drive_base.settings(straight_speed=Speed.FAST)
 robot.drive_base.straight(inches (-22.5))
 robot.drive_base.turn(90)
 robot.drive_base.straight(inches (-7.7))
 robot.drive_base.turn(-89)
 robot.attachment_1.run_angle(100, -100)
 robot.drive_base.straight(inches (-5))
# Lets you run JUST this mission: open this file and press F5.
if __name__ == "__main__":
    run(Robot())
