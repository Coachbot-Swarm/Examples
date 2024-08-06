# Coachbot Swarm Testbed Example Submissions
Welcome to the examples repository! This is a great reference point for different robot API calls and contains submission examples to help get familiar with the platform. For a more detailed walk-through of the platform, please refer to the description in the *submission_repo* of this organization.

## Getting Started with an Example
To get familiar with the system, we recommend using/referencing the example submissions presented here. 

### To Use the Simple Example 
1. Clone this Example repository to your local system
2. Navigate to the "Simple Example" Folder and view the 4 files present which make up a submission
3. Clone your private repository to your local system (this will be the repository named with your github username that you received access to once you accepted the invitation to join the Coachbot-Swarm organization)
4. Copy these 4 files to your private repository (without the folder)
5. Open the email_simple_example.txt file and enter in the email address you would like to be associated with this submission
6. Change the name of the github_username.json file to be the github username that matches the name of your private repository (ex. if my github username/repo name is dornadulavaishnavi, then my new file would be dornadulavaishnavi.json)
7. Push these 4 files to the main branch of the private repository
8. Clone the *submission_repo* repository to your local system
9. Copy just the renamed .json file to the *submission_repo* and push to the main branch
10. Your example code has now been submitted to run on the Coachbot Swarm Testbed

#### Expected Results
This simple example program will have active robots print to a log file, change LED colors, and move around. Robots will first turn the LED green, move forward for 1 second, then backwards for 1 second. The LED will then be set to blue, and the robots will turn right, then left for 1 second each. Finally, the robots will change the LED to red, wait for 1.5 seconds, and then end the experiment.

#### Easy Ways to Customize the Simple Example
- Change the commanded speed of the robot by changing the values in the API call, robot.set_vel(). Remember that this value needs to be an integer between 10 and 50.
- Change the robot LED color by changing the values in the API call, robot.set_LED(). These three values need to be between 0 and 100.
- Add more logging statements in the code.
- Change the starting points or angles of the robots or change the number of robots participating in the experiment. (Check the User Guide for the restrictions on these initial positions being specified)
