command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:  # if the boolean value "started" is True this will print
            print("Car is already started!")
        else:
            started = True  # else it sets the boolean "started" to True and this will print
            print("Car started...")
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
