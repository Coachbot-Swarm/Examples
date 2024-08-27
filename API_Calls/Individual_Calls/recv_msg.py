''' An example of using the API call, robot.recv_msg() 

    Sending and receiving messages is done through the robot.send_msg() and robot.recv_msg() functions explained further in the user guide. The messages that these 
    functions handle are created and read using struct.pack() and struct.unpack() so be sure to import struct at the top of your file if you plan 
    to use messaging. For best results, add in a short (50ms) delay between any send and receive function calls. Example usage of these functions
    are shown below.

    Parameters: none
    Output: Returns the messages in the buffer since the last call of this function.
    Example: msgs = robot.recv_msg()

    struct.unpack() example:
    struct.unpack(‘fffii’, msg_received[0][:24])

    The first argument, ‘fffii’ specifies the expected message content types. The second parameter specifies the variable I am reading from. 
    Whatever variable I save the output of the robot.recv_msg() in will contain the entire buffer of messages. In this example, I am reading in 
    the first message in the buffer and the [:24] specifies the message length, which is the byte length of the expected message. Since floats 
    and integers are both four bytes each, we determine this message length by multiplying the number of variables expected in the message with 
    the size of each variable, therefore, 6 x 4 = 24.
    This function would be called in the following way, where the struct_unpack() function is called after receiving a message:

    msgs = robot.recv_msg()
    struct.unpack('ffi', msg[0][:12])

    Expected behavior: The robot(s) will send a message with its own id, progress in program, and current run time. It then looks to receive 
    messages from other active robots and will print those messages to the log file. If this program is run with just one robot, it will only
    print that no messages were received. To see the functional example, include at least two robots in the init_pose.csv file.
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
            robot.delay(50) # add a short delay between sending messages for best results

            msgs = robot.recv_msg()
            if len(msgs) > 0:
                received = struct.unpack('iif'. msgs[0][:12])
                log.write("Received the time " + str(received[2]) + ", from robot " + str(received[0]) + " who is in loop " + str(received[1]) + "\n")
                log.flush()
            else:
                log.write("No messages received")
                log.flush()
                
        log.close() # close the file
        return
