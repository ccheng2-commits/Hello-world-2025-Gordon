# My NYC Running Story 

# let the user know what's going on
print("Welcome to the NYC Running Story!")
print("Answer the questions below to build your own adventure.")
print("-----------------------------------")

# collect user inputs
yourName = input("What's your name?: ")
direction = input("Do you want to run north or west?: ")
dogName = input("Guess the name of a cute dog you see (Nancy/Tony/Adam): ")
clownAction = input("Do you stop to watch a fire-breathing clown? (yes/no): ")
snack = input("After the run, will you eat a hot dog or ice cream?: ")

# the story
story = "Although IXD studies are tough, " + yourName + " decides to make time to run and explore New York City. " \
"Starting from SVA IXD at 136 W 21st Street, " + yourName + " runs toward the " + direction + ". " \
"Along the way, there’s a cute dog — you guess the name is " + dogName + ". " \
"Farther ahead, a clown performs a fire show. You " + clownAction + " stop to watch. " \
"After completing a full 10KM run, " + yourName + " feels happy and buys a " + snack + " to celebrate. " \
"Then it’s time to head back to the IXD classroom and finish the Hello World assignment."

# print the story
print("-----------------------------------")
print(story)