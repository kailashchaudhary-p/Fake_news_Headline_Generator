import random

# List of subjects (people or things involved in the headline)
subject = [
    "Vicky Kaushal",
    "Karan Aujla",
    "Virat Koli",
    "Cat",
    "Dog",
    "Scorpio"
]

# List of actions to be randomly chosen
action = [
    "jump From",
    "Singing a Song on",
    "Play Gulli Danda",
    "Jump From",
    "See Movie",
    "Read Book"
] 

# List of places for the action to occur
place = [
    "Kullu",
    "bad",
    "Bathroom",
    "Mumbai",
    "Goa",
    "Jamuna"
]

# Infinite loop to keep generating headlines until user says "no"
while True:
    # Randomly choose one item from each list
    random_subject = random.choice(subject)
    random_action = random.choice(action)
    random_place = random.choice(place)

    # Create the fake breaking news headline
    heading = f"BREAKING NEWS: {random_subject} {random_action} {random_place}!"
    
    # Print the headline
    print("\n" + heading)

    # Ask the user if they want another headline
    user_input = input("\nDo You Want Another Headline? Yes/No: ").strip().lower()
    
    # If the user says 'no', exit the loop
    if user_input == "no":
        break

# Final thank-you message
print("\nThanks For Using Fake Headline Generator. Have a Fun Day!")
