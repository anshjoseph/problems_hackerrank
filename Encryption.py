"""
An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let  be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:

Example


After removing spaces, the string is  characters long.  is between  and , so it is written in the form of a grid with 7 rows and 8 columns.

ifmanwas  
meanttos          
tayonthe  
groundgo  
dwouldha  
vegivenu  
sroots
Ensure that 
If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. .
The encoded message is obtained by displaying the characters of each column, with a space between column texts. The encoded message for the grid above is:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

Create a function to encode a message.

Function Description

Complete the encryption function in the editor below.

encryption has the following parameter(s):

string s: a string to encrypt
Returns

string: the encrypted string
Input Format

One line of text, the string 
"""
# import os
# import sys
# import re

def encryption(s):
    row = int(len(s)**0.5)
    col = row + 1
    data = list()
    temp = col
    index = 0
    for i in range((len(s)//col) + 1):
        if i == len(s)//col + 1:
            data.append(s[index:])
        else:
            data.append(s[index:col])
        col += temp
        index += temp
    # print(data)
    result = list()
    # result =data
    # print(row,temp)
    for c in range(len(data[0])):
        temp_str = ""
        for r in range(len(data)):
            try:
             temp_str += data[r][c]
            except:
                pass
        result.append(temp_str)
    result = " ".join(result) 
    return result

if __name__ == "__main__":
    data = input()
    result = encryption(data)
    print(result)
