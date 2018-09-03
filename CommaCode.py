#Comma Code
#+========+
#Say you have a list value like this:
#spam = ['apples', 'bananas', 'tofu', 'cats']
#Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space,
#with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
#But your function should be able to work with any list value passed to it.

def commacode(listvalue):
    print("'", end='')
    for i in range(len(listvalue)-1):
        print(listvalue[i], end=", ")
    print('and ' +listvalue[-1],end="")
    print("'")

def read(length):
    for i in range(length):
        value=input()
        listvalue.append(value)
        i+=1
    print(listvalue)

length=int(input("Enter the number of values in the list: "))
listvalue=[]
read(length)
commacode(listvalue)







    




