''' An example of using the API call, robot.send_msg(msg) 

    Sending and receiving messages is done through the robot.send_msg() and robot.recv_msg() functions explained further in the user guide. The messages that these 
    functions handle are created and read using struct.pack() and struct.unpack() so be sure to import struct at the top of your file if you plan 
    to use messaging. For best results, add in a short (50ms) delay between any send and receive function calls. Example usage of these functions
    are shown below.

    Parameters: msg should be a string that is less than 64 bytes or it will be truncated. This msg can be the output of the struct.pack() function explained in the section below.
    Output: True is successful, False if not
    Example: robot.send_msg(struct.pack(`fffii`, float_0, float_1, float_2, int_0, int_1))

    struct.pack() example:
    struct.pack(`fffii`, float_0, float_1, float_2, int_0, int_1)

    The first argument in the example above, `fffii`, specifies the type of variables being sent in what order and quantity. In this example, I 
    am sending three floats and two signed integers. The remaining parameters are the corresponding variables I am sending in the message.
    This line would be called in the following way, where the struct_pack() function is called and passed into the send_msg() function: 
    
    robot.send_msg(struct.pack(`fffii`, float_0, float_1, float_2, int_0, int_1))

    Expected behavior: The robot(s) will send a message and print it to the log file
'''
import struct

def usr(robot):
    log = open("experiment_log.txt", "w")
    
    log.write("an example write string\n")
    log.flush()
    
    id = robot.virtual_id()

    while True:
        robot.delay()

        for loop_count_variable in range(5):    # for 5 repetitions
            to_send = struct.pack('iif', id, loop_count_variable, robot.get_clock())    # create struct message
            robot.send_msg(to_send) # send message
            log.write(str(id) + " sending loop count of " + str(loop_count_variable) + " at " + str(robot.get_clock()) + "\n")
            log.flush()
            robot.delay(50) # add a short delay between sending messages for best results

            robot.delay(1000) # delay for 1 second between each loop

        log.close()
        return
