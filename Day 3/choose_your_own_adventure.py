print("Welcome To Treasure Island. \n")

print(
    "You are stranded on an island and need to find a way to get off. You awake to the strong Yellow rays of light shining in your eyes.\n"
)

print(
    "Before you, you see two paths. One to the Left which leads to the beach and one to the Right which leads to the jungle. \n"
)
left_or_right = input('Which path do you choose? Type "Left" or "Right" \n').lower()

if left_or_right == "right":
    print("You step into the thick jungle and are immediately attacked by a tiger. \n")
    print("You are dead. \n")
else:
    print(
        "You continue down the beach, and spot a small boat anchored off shore. You also hear a door blowing in the wind and rattling against it's frame as it flutters back and forth. \n"
    )
    print("Do you swim towards the boat or go towards the door? \n")
    swim_or_door = input('Type "Swim" or "Door" \n').lower()
    if swim_or_door == "swim":
        print("You swim out to the boat, but are attacked by a shark. \n")
        print("You are dead. \n")
    else:
        print(
            "You approach the sound of the clattering door, and see a building built in to the side of the mountain. \n"
        )
        print(
            "Inside the building there are three doors with different colored frames. One Red, one Blue, and one Yellow. \n"
        )
        print("Which door do you choose? \n")
        door = input('Type "Red", "Blue", or "Yellow" \n').lower()
        if door == "red":
            print("You open the Red door and are immediately engulfed in flames. \n")
            print("You are dead. \n")
        elif door == "blue":
            print("You open the Blue door and step in to the dimly lit room. \n")
            print(
                "As you breach the door the floor collapses and you plummet in to a pit filled with water. \n"
            )
            print("There is no escape, You are dead. \n")
        elif door == "yellow":
            print(
                "You open the Yellow door and see a shiny new boat with the keys in the ignition. \n"
            )
            print("You have escaped the island and won the game! \n")
        else:
            print("You are dead. \n")
