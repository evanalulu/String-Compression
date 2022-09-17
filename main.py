""" String Compression: Implement a method to perform basic 
string compression using the counts of repeated characters. For
example, the string aabcccccaaa would become a2blc5a3, If the 
"compressed" string would not become smaller than the original 
string, your method should return the original string. You can 
assume the string has only uppercase and lowercase letters (a- z). """

def stringCompression(s):
    compressedS = s[0]
    tempChar = s[0]
    count = 0

    for letter in s:
        if (letter != tempChar):
            compressedS = compressedS + str(count) + letter
            tempChar = letter
            count = 1
        else:
            count += 1
    
    compressedS += str(count)
    
    #final edge case
    if len(compressedS) > len(s):
        return (s)

    return (compressedS)

print(stringCompression("aaaaaabaaaaaaaaaaaCCC"))