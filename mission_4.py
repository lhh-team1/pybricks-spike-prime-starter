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
    robot.attachment_1.run_angle(100, -90)
    robot.drive_base.settings(straight_speed=Speed.FAST,turn_rate=999)
    robot.drive_base.arc(inches(-10.), distance=inches(-9))
    robot.drive_base.straight(inches (-6.5))
    robot.attachment_1.run_until_stalled(100, then=Stop.HOLD)
    robot.drive_base.straight(inches (18))
 
# Lets you run JUST this mission: open this file and press F5.
if __name__ == "__main__":
    run(Robot())
