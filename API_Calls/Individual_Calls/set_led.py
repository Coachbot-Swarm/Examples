''' An example of using the API call, robot.set_led(r,g,b) 

    Parameters: r,g,b should be integers between and 0 and 100 to set the color and brightness of the onboard LED
    Output: none
    Example: robot.set_led(30,100,0)

    Expected behavior: The robot's LED will cycle through all combinations of allowable rgb values and then blink green for 5 seconds
'''

def usr(robot):
    while True:
        robot.delay()

        # Use a nested for loop to cycle through all possible led colors
        delta = 15
        for r_value in range(0,100, delta):
            for g_value in range(0,100, delta):
                for b_value in range(0,100, delta):
                    robot.set_led(r_value, g_value, b_value) # set the LED values through variables
                    robot.delay(100)

        # blink the LED green for 5 seconds
        for i in range(5):
            robot.set_led(0,100,0) # turn the LED to green
            robot.delay(1000) # wait 1 second
            robot.set_led(0,0,0) # turn the LED off
            robot.delay(1000) # wait 1 second

        return
