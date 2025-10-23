''' An example of using the API call, robot.delay(time_ms) 

    Parameters: an integer value in milliseconds, default is 20ms but a different integer parameter can be specified
    Output: none
    Example: robot.delay(500)

    Expected behavior: The robot(s) will blink its LED different colors at various rates.
'''
import random

def usr(robot):
    log = open("experiment_log.txt", "w")
    # log = open("experiment_log.txt", "wb") # some systems work with w, some with wb, please check what works for your system and use accordingly
    
    log.write("an example write string\n")
    log.flush()

    time_to_run = 3 * 60 * 1000 # run this program for 3 minutes, multiplied by 1000 to convert to milliseconds
    program_start_time = robot.get_clock()
    
    while True:
        robot.delay()

        rand_red = random.randint(0,100)
        rand_green = random.randint(0,100)
        rand_blue = random.randint(0,100)
        robot.set_led(rand_red, rand_green, rand_blue) # change the LED color based on the randomly selected rgb values above
        robot.delay(1000)

        if robot.get_clock() - program_start_time > time_to_run: # for the 60 seconds we set the program to run
            log.close() # close the file
            return
