#Q3-Write a program to check if two strings are a rotation of each other?

def rotation_str(str1,str2):
    #first we can check lengths of both string if they are not equal then no rotation
    #we can first creat a variable to store concatination of string 1
    #and then see if string 2 is a substring of temp or not
    #if substring then its a rotation 
    #if no, then no rotation

    size1 = len(str1)
    size2 = len(str2)

    if size1 != size2:
        return 0



    temp = str1+str1

    if (temp.count(str2)>0):
        return 1
    else:
        return 0

str1  = "ABCD"
str2 = "CDAB"

if rotation_str(str1, str2):

    print("rotation")
else:
    print("no rotation")