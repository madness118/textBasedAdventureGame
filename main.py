import time


class Room:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_details(self):
        print()
        print(" You have entered {" + self.name + "}")
        print(" Room Level: {" + str(self.level) + "}")
        print()
        if self.name == "The Void":
            print("The Void has consumed you. Nice try.")
        elif self.name == "The End":
            print("Congratulations. You have reached The End.")


inventory = []


def the_room():
    r1 = Room("The Room", 1)
    r1.get_details()

    count = 0
    while count < 3:
        choice = int(input("Stay (1) or Leave (2). Try not to stay for too long.\n"))
        if choice == 1:
            print("Are you sure?")
            count += 1
        elif choice == 2:
            break
        time.sleep(1)
    if count >= 3:
        print("I see you have made your choice...")
        the_void()
        return

    chooseDoor = int(input("There are two doors. An oak door lies to the left (1), and a white one to the right (2)\n"))
    if chooseDoor == 2:
        rNext = "kitchen"
    if chooseDoor == 1:
        rNext = "hall"
    return rNext


def the_kitchen():
    r2 = Room("The Kitchen", 2)
    r2.get_details()

    print("It's dark in here")
    openItem = int(input("\nOpen cupboard (1) or Open fridge (2): "))
    print()
    if openItem == 1:
        print("You have opened the cupboard. You find Cheese.")
        inventory.append("Cheese")
        print("+1 Moldy Cheese")
    elif openItem == 2:
        print("You have opened the fridge. You find a Flashlight.")
        inventory.append("Flashlight")
        print("+1 Flashlight")

    leaveTo = int(input("\nExit to Hall (1) or Window (2): "))
    if leaveTo == 1:
        kNext = "hall"
    elif leaveTo == 2:
        kNext = "forest"
    return kNext


def the_hall():
    r3 = Room("The Hall", 2)
    r3.get_details()

    print("It's hard to see in here. \nA dark figure brushes past.")
    print()
    time.sleep(1.5)
    if "Flashlight" in inventory:
        print("You turn on your Flashlight.")
        time.sleep(1)
        print("Thank god you picked it up earlier.")
        time.sleep(1.5)
        print("You carry on towards the end")
        time.sleep(1)
        the_forest()
    else:
        for i in range(3):
            time.sleep(1.5)
            print(".")
        the_void()


def the_forest():
    r4 = Room("The Forest", 3)
    r4.get_details()

    ending = int(input("Its scary out here.\nMake a decision, quick, Left (1) or Right (2): "))
    if ending == 1:
        r6 = Room("The End", 4)
        r6.get_details()
    elif ending == 2:
        the_void()


def the_void():
    r5 = Room("The Void", 4)
    r5.get_details()


def main():
    print("Greetings traveller. You have finally awoken.\nAll you see is a dimly lit room.")
    nextRoom = the_room()
    if nextRoom == "kitchen":
        nextRoom = the_kitchen()
        if nextRoom == "hall":
            the_hall()
        elif nextRoom == "forest":
            the_forest()
    elif nextRoom == "hall":
        the_hall()


main()

print()
print("Inventory: ")
print(inventory)
