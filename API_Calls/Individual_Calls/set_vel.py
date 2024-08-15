''' An example of using the API call, robot.set_vel(l,r) 

    Parameters: left and right should be whole numbers between -50 and 50 that indicate wheel speeds corresponding to the respective wheel. 
    0 being no movement and 50 being the fastest possible speed. The negative values indicate that the wheel would spin backwards at that 
    speed. These values have no unit. This function sets the speed for 1 second before stopping.
    Output: none
    Example: robot.set_vel(30,-40)

    Expected behavior: The robot(s) will move forward for a three-fourths of a second, then backwards for half a second, turn left for 5 seconds, then right for another 5.
'''

def usr(robot):
    while True:
        robot.delay()

        for i in range(3):
            robot.set_vel(25,25) # move forward at half its maximum speed
            robot.delay(750) # wait for 750ms
            
            robot.set_vel(-25,-25) # move backwards at half its maximum speed
            robot.delay(500) # wait for 500 ms

            # one way to set the robot's velocity for an extended period of time is using the robot's API call, get_clock(). Python's time file can be used as well
            curr_time = robot.get_clock() # get the current time (since runtime started)
            while (robot.get_clock() - curr_time) < 5: # until 5 seconds has passed
                robot.set_vel(-25,25) # turn to the left at half the maximum speed

            curr_time = robot.get_clock() # get the current time (since runtime started)
            while (robot.get_clock() - curr_time) < 5: # until 5 seconds has passed
                robot.set_vel(25,-25) # turn to the right at half the maximum speed

        return