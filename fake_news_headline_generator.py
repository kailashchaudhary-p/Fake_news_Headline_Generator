import random
subject = [
    "Vicky Kaushal",
    "Karan Aujla",
    "Virat Koli",
    "Cat",
    "Dog",
    "Scorpio"
]
action = [
    "jump From",
    "Singing a Song on",
    "Play Gulli Danda",
    "Jump From",
    "See Movie",
    "Read Book"
] 
place = [
    "Kullu",
    "bad",
    "Bathroom",
    "Mumbai",
    "Goa",
    "Jamuna"
]
while True:
    subject=random.choice(subject)
    action=random.choice(action)
    place=random.choice(place)

    Heading=f"BREAKING NEWS : {subject},{action},{place}"
    print("\n"+Heading)
    user_input=("\n Do You Want Another Headline yes/No".strip().lower())
    if user_input=="no":
        break
print("\n Thanks For Using Fake Headline Genrator Have a Fun Day")


