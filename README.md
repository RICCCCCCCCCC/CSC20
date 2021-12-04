10.1 Readme
GitHub Link
https://github.com/RICCCCCCCCCC/CSC20/commit/419d4918919f9eb5d345a598c58f6c29979c5624
Class Documentation
Class Rider: The rider class uses object oriented programming to emulate a skier or snowboarder. There are 4 class variables: victory, failure, feeling, and instructions.
Init Constructor:
	The init constructor sets several instance variables. These are :
self.__ride: Determines whether the rider is a skier or a snowboarder.
Self.__successes: Keeps track of the successes in the minigame.
self.__days: Tracks of “days” practice. It is a simple score counter.
self.__id: Tracks of the rider’s name.
self.__exp: Tracks experience points throughout the minigame.
self.__skill: It is a string classification for the experience level.


Methods:
get_id(self): Displays the name of the rider. No additional arguments are needed.
set_id(self, id): Allows users to set the rider name using a single argument.
practice(self, days): This is a fancy name for set_exp. It sets the experience under the guise of “days practiced.”
set_skill_level(self): Displays the broad classification of the self.__exp value.
jump(self): Creates a random number, between 0 and 5, and compares it against the user’s self.__exp value. If the exp value is higher, then a success message is printed and multiple stats are increased. If the exp value is lower, a failure message is displayed and “days” are added to the self.__days value.
box(self): Creates a random number, between 0 and 10, and compares it against the user’s self.__exp value. If the exp value is higher, then a success message is printed and multiple stats are increased. If the exp value is lower, a failure message is displayed and “days” are added to the self.__days value.
rail(self): Creates a random number, between 10 and 15, and compares it against the user’s self.__exp value. If the exp value is higher, then a success message is printed and multiple stats are increased. If the exp value is lower, a failure message is displayed and “days” are added to the self.__days value.
check_successes(self): returns the self.__successes value. It is used within the minigame.
get_ride(self): Displays the ride type for the user’s convenience
set_ride(self, ride): The user is able to change the ski or board value for the self.__ride variable.
see_days(self): Shows the user how many days have been spent on the hill.
get_instructions(self): Displays useless instructions to the user.
get_failure(self): Returns the failure class variable
victory_feeling(self): Returns a list of the victory and feeling class variables.
reset(self): Resets the self.__successes value.

How To use the Demo Program
	The demo program is a skiing/boarding minigame. To initiate it the user must input:
python3 <rider name> <ski/board> <experience level [0-15]>
Example: 
python3 101.py Billybob ski 3
Then you will be greeted by a pleasant message and then be queued to practice, try the run, or check the stats. In reality, there are many more commands than that. Most of the commands are accompanied by entertainingly radical commentary. Here is a full list:
exit: Terminates the program.
help: Gives the user a useless help message.
change_name: Allows the user to change the name of the rider referenced in the game.
got_concussion: Prints out the current name of the player
practice: Adds a user inputted number to both the experience points value and the days practices value
check_before_you_wreck: Prints out the referenced rider’s skill level
look_at_feet: Displays the type of ride the user is currently using. It is ski or board.
switch_things_up: Allows the user to switch between board and skis. It also erases the experience points and resets skill level.
shread_the_gnar: This activates the minigame. More information on the minigame below.
Minigame Objective:
	The objective of the minigame is to clear the jump, the box, and the rail in the minipark with the least days of practice.. The user chooses to do this by inputting “shread_the_gnar” when prompted to enter a command. The difficulty of the features is determined using the randint method. Every time a feature is cleared, the experience stat is bumped up 1 to 3 points. Every time a feature is failed, a day of riding is added on to the running total. If a player cannot just clear the jumps first try (It is impossible when starting from 0, which is where any self respecting person would start.), then they must use the practice command to add experience to the referenced rider. The game has no definite end, but several positive messages will pop up if all three jumps are cleared. Good luck playing.
