#Write a program which will find all such numbers which are divisible by 7 but
#are not a multiple of 5, between 2000 and 3200 (both included).The numbers
#obtained should be printed in a comma-separated sequence on a single line.

#--------------1-----------------------
#for num in range(2000,3200):
#    if num % 7 == 0:
#        if num % 5 != 0:
#           print(num,end=" ", sep=",")



#--------------2-----------------------
l=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        l.append((i))

print(l, sep=",", end=" ")
