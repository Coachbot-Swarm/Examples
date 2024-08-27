''' An example of using the API call, robot.virtual_id() 

    Parameters: none
    Output: An integer that is the virtual ID of the robot.
    Example: virt_id = robot.virtual_id()

    Expected behavior: The robot(s) will print their ID number to their corresponding log file
'''

def usr(robot):
    log = open("experiment_log.txt", "w")
    
    log.write("an example write string\n")
    log.flush()

    while True:
        robot.delay()

        id = robot.virtual_id() # get the integer value representing the robot's ID
        log.write("The robot ID is " + str(id) + "\n")   # cast the id value to a string to write to the file
        log.flush()

        log.close() # close the file
        return

