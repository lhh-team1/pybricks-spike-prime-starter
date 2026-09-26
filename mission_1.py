"""Mission 1: 
R: Right of first major line + 2 minor back wheels straddleing the first two thick black lines right front wheel in corner
A: Forks
P: 1
"""


from robot import Robot, inches, Speed
from pybricks.tools import wait

def run(robot):
    #leaf cutter
    robot.drive_base.settings(straight_speed=Speed.FAST)
    robot.drive_base.straight(inches(24))  # drive forward 10 inches
    robot.drive_base.turn(-63)  # turn around (gyro keeps it accurate)
    robot.drive_base.straight(inches(14.8))
    robot.drive_base.turn(99)
    robot.drive_base.settings(straight_speed=Speed.SLOW)
    robot.drive_base.straight(inches(7))
    #window to the past
    robot.drive_base.settings(straight_speed=Speed.FAST)
    robot.drive_base.straight(inches(-4))
    robot.drive_base.turn(-80.04)
    robot.drive_base.straight(inches(-11))
    robot.drive_base.straight(inches(2.5))
    robot.drive_base.arc(inches(-5.5), distance=inches(19.2))
    #Biocentric Architecture
    robot.drive_base.turn(-5)
    robot.attachment_1.run_angle(700, -82)
    robot.drive_base.straight(inches(-7))
    robot.attachment_1.run_angle(900, -30)
    robot.drive_base.turn(-15)
    robot.drive_base.straight(inches(-2))
    robot.attachment_1.run_angle(70, 60)
    wait(2500)
    robot.drive_base.settings(straight_speed=Speed.SLOW)
    robot.drive_base.turn(35)
    robot.drive_base.settings(straight_speed=Speed.FAST)
    robot.drive_base.straight(inches(36))
    robot.drive_base.stop()


# Lets you run JUST this mission: open this file and press F5.
if __name__ == "__main__":
    run(Robot())
