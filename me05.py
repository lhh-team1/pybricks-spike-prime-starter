"""Mission 1: 
R: Right of first major line + 2 minor back wheels straddleing the first two thick black lines right front wheel in corner
A: Forks
P: 1
"""


from robot import Robot, inches, Speed

def run(robot):
    robot.drive_base.settings(straight_speed=Speed.FAST)
    robot.drive_base.straight(inches(26))  # drive forward 10 inches
    robot.drive_base.turn(-63)  # turn around (gyro keeps it accurate)
    robot.drive_base.straight(inches(13))
    robot.drive_base.turn(99)
    robot.drive_base.settings(straight_speed=Speed.Slow)
    robot.drive_base.straight(inches(4.5))
    robot.drive_base.settings(straight_speed=Speed.FAST)
    robot.drive_base.straight(inches(-3.8))
    robot.drive_base.turn(-80)
    robot.drive_base.straight(inches(-10.5))
    robot.drive_base.straight(inches(2))
    robot.drive_base.arc(inches(-5.5), distance=inches(19.5))
    robot.attachment_1.run_angle(700, -85)
    robot.drive_base.straight(inches(-7.7))
    robot.attachment_1.run_angle(900, -30)
    robot.drive_base.turn(-20)
    robot.drive_base.straight(inches(-2.7))
    robot.attachment_1.run_angle(50, 69)
    robot.drive_base.settings(straight_speed=Speed.Slow)
    robot.drive_base.straight(inches(3))

    robot.drive_base.stop()


# Lets you run JUST this mission: open this file and press F5.
if __name__ == "__main__":
    run(Robot())
