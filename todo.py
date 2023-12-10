print(
    """  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
   
   
********************************

      """)

todo = []
completed_list = []

while True:
    command = input("Enter a command. Type 'h' for help: \n")
    if command.isnumeric():
        indx = int(command)-1
        if indx >= len(todo):
            print("THIS IS NOT ON YOUR LIST!")
        else:
            completed_list.append(todo[indx])
            todo.pop(indx)
            for num in range(len(todo)):
                print(f"{num+1}. {todo[num]}")
    elif command == "h":
        print("""
        TODO LIST HELP 
        Type 'q' to quit 
        To add a todo to the list, type it and hit enter 
        To complete a todo enter its number
              """)
    elif command == "q":
        print(f"Today you completed {len(completed_list)} todos: ")
        for thing in completed_list:
            print(f"* {thing}")
        break
    else:    
        todo.append(command)
        for num in range(len(todo)):
            print(f"{num+1}. {todo[num]}")
