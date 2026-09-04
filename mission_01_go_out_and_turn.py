"""Mission 1: 
R: Right of first major line + 2 minor
A: Forks
P: 1
"""

from robot import Robot, inches


def run(robot):
    robot.drive_base.straight(inches(35))  # drive forward 10 inches
    #robot.drive_base.turn(180)  # turn around (gyro keeps it accurate)
    robot.drive_base.stop()


# Lets you run JUST this mission: open this file and press F5.
if __name__ == "__main__":
    run(Robot())
