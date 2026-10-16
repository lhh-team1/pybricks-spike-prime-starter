"""Mission 
R: two first major lines clossest to the seed repository inbeteen the tires
A: Forks
P: 1
"""
#go from right lunch to lft lunch doing the sunroof on the way

from robot import Robot, inches, Speed
from pybricks.tools import wait, multitask, run_task
from pybricks.parameters import Stop


async def do_it(robot):
    await multitask(
        robot.drive_base.straight(inches (-2)),
        robot.attachment_2.run_angle(100, 110)
    )

def run(robot):
    robot.drive_base.settings(straight_speed=Speed.FAST)
    robot.drive_base.straight(inches (30))
    robot.drive_base.turn(-90)
    robot.attachment_1.run_angle(100, -110)
    robot.drive_base.straight(inches (-8.4))
    robot.attachment_1.run_angle(100,110)
    robot.drive_base.straight(inches (8))
    robot.drive_base.turn(90)
    run_task(do_it(robot))

# Lets you run JUST this mission: open this file and press F5.
if __name__ == "__main__":
    run(Robot())
