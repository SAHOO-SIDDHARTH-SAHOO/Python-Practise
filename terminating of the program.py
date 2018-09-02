#Terminating a program using sys.exit() which is in sys module.
import sys
while True:
    print("Write your response either to exit or continue the program")
    response=input()
    if response == "continue":
        continue
    elif response == "exit":
        print("System is shuting down.")
        sys.exit()

