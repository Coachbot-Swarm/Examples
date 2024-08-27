''' An example of using the API call, robot.get_clock() 

    Parameters: none
    Output: a float of the number of seconds elapsed since the program started
    Example: curr_time = robot.get_clock()

    Expected behavior: The robot(s) will print various time stamps throughout the program, an initial time, a timestamp 5 seconds later, then the elapsed time
'''

def usr(robot):
    log = open("experiment_log.txt", "w")
    
    log.write("an example write string\n")
    log.flush()

    while True:
        robot.delay()

        start_time = robot.get_clock() # get the current elapsed time since the start of the program
        log.write("The current time is " + str(start_time) + "\n") # print to file
        log.flush()

        robot.delay(5000) # wait 5 seconds

        end_time = robot.get_clock() # get the elapsed time
        log.write("The end time is " + str(end_time) + "\n") # print to file
        log.flush()

        log.write("The elapsed time is " + str(end_time - start_time) + "\n") # print how long this part of the code took to run
        log.flush()

        log.close() # close the file
        return

