"""Mission 1: 
R: Right of first major line + 2 minor back wheels straddleing the first two thick black lines right front wheel in corner
A: Forks
P: 1
"""


from robot import Robot, inches, Speed
from pybricks.tools import wait

def run(robot):
    robot.attachment_1.run_angle(200, -69)

# Lets you run JUST this mission: open this file and press F5.
if __name__ == "__main__":
    run(Robot())
