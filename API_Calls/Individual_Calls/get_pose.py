''' An example of using the API call, robot.get_pose(msg) 

    Parameters: none
    Output: a list with the [x,y,theta], check to see that this output is valid before using it or None if no position has been updated for 
    the robot
    Example: pose = robot.get_pose()

    Expected behavior: The robot(s) will move around and print its current position to the log for 60 seconds.
'''

def usr(robot):
    log = open("experiment_log", "w")
    
    log.write("an example write string\n")
    log.flush()

    time_to_run = 60 * 1000 # run this program for 60 seconds, multiplied by 1000 to convert to milliseconds
    program_start_time = robot.get_clock()

    while True:
        robot.delay()

        # first get our robot's current position
        curr_pose = robot.get_pose()
        while not curr_pose: # ensures that we get the pose, robot will return False if the position hasn't been updated
            curr_pose = robot.get_pose()
        curr_x = curr_pose[0]
        curr_y = curr_pose[1]
        curr_theta = curr_pose[2] 
        log.write("My current pose is " + str(curr_pose) + "\n") # print the position to the log
        log.flush()

        # do some motion to get to a new position
        robot.set_vel(30,30)
        robot.delay(750)
        robot.set_vel(-30,-40)
        robot.delay(900)
        robot.set_vel(-25,-25)
        robot.delay(500)

        if robot.get_clock() - program_start_time > time_to_run: # for the 60 seconds we set the program to run
            log.close() # close the file
            return