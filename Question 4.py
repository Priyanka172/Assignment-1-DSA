def non_repeateing(str):
    #traverse through the string
    #create empty dictionary to store the count 
    #then check for count in dictionary if its 1 then return that value
    counts = {}

    for chr in str:
        if chr in counts:
            counts[chr] += 1
        else:
            counts[chr] = 1
    for chr in counts:
        if counts[chr] == 1:
            return chr
    return None
str = "aabbcddcef"
print(non_repeateing(str))