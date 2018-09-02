#use of random module
import random 
for i in range(0,5):
    print(str(i+1)+". "+str(random.randint(0,10)))
print("We are out of the loop now.")
