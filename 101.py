# Eric
# Assignment 10.1: Your Own Class
# 101.py
# Create a class

# Import modules
import sys
import random
import time

# Define Class Rider
class Rider():
    # Define class variables
    victory = ["Radical badical!", "Totally prime bro!"]
    failure = "The run was ended by a brutal wipeout."
    feeling = ["stoked", "hyped"]
    instructions = "It aint hard, fool, you should be able to figure it out on your own."
    # Define the init constructor
    def __init__(self, id, ride, exp):
        # Define the instance variables
        self.__ride = ride
        self.__successes = 0
        self.__days = 0
        self.__id = id
        # Concatinate id into and announcement statement
        self.__anouncement = f"{id} is at the top of the run. There's the drop in, lets see how this goes."
        # Make sure that ride is ski or board
        if self.__ride == "ski" or "board":
            # Do nothing
            pass
        # If ride is not ski or board
        else:
            # Raise an error
            raise ValueError("Woski my broski, you have got to have one plank or two!\nPlease input 'ski' or 'board'. Restarting program.")
        # Set the exp instance variable
        self.__exp = exp
        # If exp is less than 0
        if self.__exp < 0:
            # Raise Value error
            raise ValueError("You can't be worse than a Joey cheif.\nYour skill level must be within the range [0,15]. Restarting program.")
        # If exp is between 0 and 5
        if self.__exp >= 0 and self.__exp <= 5:
            # Set skill to noob
            self.__skill = "a noob"
        # If exp is between 10 and 6
        if self.__exp > 5 and self.__exp <= 10:
            # Set skill to ight
            self.__skill = "ight"
        # If skill is between 15 and 11
        if self.__exp > 10 and self.__exp <= 15:
            # Set skill to Brofessional
            self.__skill = "a straight up Brofessional"
        # If exp is greater than 15
        if self.__exp > 15:
            # Set exp to 15
            self.__exp = 15
            # Set skill to brofessional
            self.__skill = "a straight up Brofessional"

    # Def method
    def get_id(self):
        # Print data
        print(f"You clown, how did you forget that your name is {self.__id}.\nMaybe you should wear a brain bucket before you bail again.")
    
    # Def method
    def set_id(self, id):
        # Change self.id to id 
        self.__id = id
        # Print data
        print(f"{self.__id} is a goofy Brofessional name, but it kind of fits.")
    
    # Def method
    def practice(self, days):
        # Add the number of days "practiced" to self.exp
        self.__exp = self.__exp + days
        #Keep track of days
        self.__days += days
        # Self.exp housekeeping stuff
        if self.__exp < 0:
            # Raise Value error
            raise ValueError("You can't be worse than a Joey cheif.\nYour skill level must be within the range [0,15]. Restarting program.")
        # If exp is between 0 and 5
        if self.__exp >= 0 and self.__exp <= 5:
            # Set skill to noob
            self.__skill = "a noob"
        # If exp is between 10 and 6
        if self.__exp > 5 and self.__exp <= 10:
            # Set skill to ight
            self.__skill = "ight"
        # If skill is between 15 and 11
        if self.__exp > 10 and self.__exp <= 15:
            # Set skill to Brofessional
            self.__skill = "a straight up Brofessional"
        # If exp is greater than 15
        if self.__exp > 15:
            # Set exp to 15
            self.__exp = 15
            # Set skill to brofessional
            self.__skill = "a straight up Brofessional"
        # Print data
        print(f"You have shredded the slope for {days} days. You are now {self.__skill}")
        
    # Def method
    def get_skill_level(self):
        if self.__exp < 0:
            # Raise Value error
            raise ValueError("You can't be worse than a Joey cheif.\nYour skill level must be within the range [0,15]. Restarting program.")
        # If exp is between 0 and 5
        if self.__exp >= 0 and self.__exp <= 5:
            # Set skill to noob
            self.__skill = "a noob"
        # If exp is between 10 and 6
        if self.__exp > 5 and self.__exp <= 10:
            # Set skill to ight
            self.__skill = "ight"
        # If skill is between 15 and 11
        if self.__exp > 10 and self.__exp <= 15:
            # Set skill to Brofessional
            self.__skill = "a straight up Brofessional"
        # If exp is greater than 15
        if self.__exp > 15:
            # Set exp to 15
            self.__exp = 15
            # Set skill to brofessional
            self.__skill = "a straight up Brofessional"
        # Print data
        print(f"You are {self.__skill}")

    #  Def method
    def jump(self):
        # Print anouncement
        print(self.__anouncement)
        # context for minigame
        message = "You have decided to hit a jump. Best of luck. Shead the gnar bro!"
        # Print context for minigame
        print(message)
        # Make it interesting by adding commentary and delaying by second interverals
        print("The runup is perfect...")
        time.sleep(1)
        print(f"{self.__id} takes to the air...")
        time.sleep(1)
        # Detirmine the difficulty with the randint method
        chance = random.randint(0,5)
        # Detirmine if experience outweighs difficulty. If so, print success, otherwise, print failure
        if self.__exp <= chance:
            print("You bailed Brah.")
            # Add a day as punishment
            self.__days += 1
        if self.__exp > chance:
            print("Sick jump bro!")
            # Add expetiencs
            self.__exp += 1
            # Keep track if the jump was cleared for minigame
            self.__successes+= 1
    #  Def method
    def box(self):
        # The box method follows the exact same steps as the jump method. It merely has different data
        message = "You have decided to slide a box. Just act like you are going across ice. Best of luck. Shead the gnar bro!"
        print(message)
        print("The runup is perfect...")
        time.sleep(1)
        print(f"{self.__id} gets up on the box...")
        time.sleep(1)
        chance = random.randint(0,10)
        if self.__exp <= chance:
            print("You bailed Brah.")
            self.__days += 1
        if self.__exp > chance:
            print("Sick box hit bro!")
            self.__exp += 2
            self.__successes += 1

    # Def method
    def rail(self):
        # The box method follows the exact same steps as the jump method. It merely has different data
        message = "You have decided to slide a rail. Don't think about your teeth when you are sliding. Best of luck. Shead the gnar bro!"
        print(message)
        print("The runup is perfect...")
        time.sleep(1)
        print(f"{self.__id} pulls a 90 degree spin onto the rail...")
        time.sleep(1)
        print(f"{self.__id} is sliding down the rail...")
        chance = random.randint(7,15)
        if self.__exp <= chance:
            print("You bailed Brah.")
            self.__days += 1
        if self.__exp > chance:
            print("Sick box hit bro!")
            self.__exp += 3
            self.__successes +=1
    def check_successes(self):
        return(self.__successes)

    # Def method
    def get_ride(self):
        # Print out data
        print(f"You ride a {self.__ride} bruv, pay attension to what is on your tinkers.")

    # Def method
    def set_ride(self, ride):
        # Print warning message
        print("Caution, chaninging your ride will cause all your stats to go down.")
        # Ser ride to equal self.ride
        self.__ride = ride
        # Reset experience points
        self.__exp = 0
    
    # Def method
    def see_days(self):
        # Return data
        return(self.__days)

    # Def method
    def get_instructions(self):
        # Return data
        return(Rider.instructions)

    # Def method
    def get_failure(self):
        # Return data
        return(Rider.failure)

    # Def method
    def victory_feeling(self):
        # Return data
        return(Rider.victory[random.randint(0,1)], Rider.feeling[random.randint(0,1)])

    # Def method
    def reset(self):
        # Set self.__successes to 0
        self.__successes = 0

# Def main
def main():
    # Define greeting and print
    greeting = "Welcome to ski and board simulator 2021.\nIn this sumulation, you are trying to shread the minipark with the fewest practice days possible.\nGood luck!"
    print(greeting)
    # Use the argvalues method to take arguments from the origional input
    a = sys.argv[1] 
    b = sys.argv[2]
    c = int(sys.argv[3])
    # Create object YoMama
    YoMama = Rider(a, b, c)
    # Initiate while loop
    while True:
        # Print this line every time a command is entered for asthertics
        print("-----------------------------------------------------------------------")
        # Take user input for the command
        com = input("Do you want to practice, try the run, or check your stats?\nEnter help for more information.\nInput command>>> ")
        # Create exit command
        if com == "exit":
            break
        # Create useless help command
        if com == "help":
            print(YoMama.get_instructions())
        # Activate the change name method
        if com == "change_name":
            YoMama.set_id(input("Input your Brofessional name:\n>>>"))
        # Activate the get_id method
        if com == "got_concussion":
            YoMama.get_id()
        # Activate the parctice mathod
        if com == "practice":
            YoMama.practice(int(input("Input the number of days you practiced sending it:\n>>> ")))
        # Activate  method
        if com == "check_before_wreck":
            YoMama.get_skill_level()
        # Activate get_ride method
        if com == "look_at_feet":
            YoMama.get_ride()
        # Activate set_ride method
        if com == "switch_things_up":
            YoMama.set_ride(input("What do you want to ride?\n>>> "))
        # Initiate jump box and rail modules
        if com == "shread_the_gnar":
            # Initiate true loop to allow the use of breaks
            while True:
                # Reset the self.successes to 0
                YoMama.reset()
                # Execute jump module. If it passes, reward user by boosting stats. If it fails, print failure message and break.
                YoMama.jump()
                if YoMama.check_successes() != 1:
                    print(YoMama.get_failure())
                    break
                # Execute box module. If it passes, reward user by boosting stats. If it fails, print failure message and break.
                YoMama.box()
                if YoMama.check_successes() != 2:
                    print(YoMama.get_failure())
                    break
                # Execute rail module. If it passes, reward user by boosting stats. If it fails, print failure message and break.
                YoMama.rail()
                if YoMama.check_successes() != 3:
                    print(YoMama.get_failure())
                    break
                # Print congradulatory messages
                print(f"Congradulations rider, you have shredded the minipark without wrecking yourself.")
                victory = YoMama.victory_feeling()[0]
                feeling = YoMama.victory_feeling()[1]
                print(f"Your run was {victory}. Do you feel toatlly {feeling} or what?")
                print(f"You cleared the run with only {YoMama.see_days()} of practice!")
                break

# Name main thing
if __name__ == "__main__":
    # Execute main
    main()
