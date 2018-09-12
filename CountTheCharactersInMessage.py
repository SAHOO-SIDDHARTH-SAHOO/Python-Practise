#Count the characters in the message using setdefault() method.

message=" I am blessed and greatful.Count the characters in the\
          \message using setdefault() method."
count={}
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1

print(count)
