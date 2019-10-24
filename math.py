print "math is fun last I checked"


prefixes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
suffix = "after"

for letter in prefixes:
    if letter == "A":
        print suffix
    elif letter == "Q":
        print letter + "u" + suffix 
    else:
        print letter + suffix