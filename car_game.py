command = ""
started = False # simple yes/no true/false boolean that can change to reflect the status of the car

while True:
    command = input("> ").lower()
    if command == "start":
        if started:  # if the boolean value "started" is True
            print("Car is already started!")  #  then this will print
        else:
            started = True  # else it sets the boolean "started" to True
            print("Car started...")  # then this will print
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped...")
    elif command == "help":
        print("""
Start - Starts the Engine
Stop - Stops the Engine
Quit - To quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand")
