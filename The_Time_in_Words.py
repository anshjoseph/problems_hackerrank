"""
Given the time in numerals we may convert it into words, as shown below:

At , use o' clock. For , use past, and for  use to. Note the space between the apostrophe and clock in o' clock. Write a program which prints the time in words for the input given in the format described.

Function Description

Complete the timeInWords function in the editor below.

timeInWords has the following parameter(s):

int h: the hour of the day
int m: the minutes after the hour
Returns

string: a time string as described
Input Format

The first line contains , the hours portion The second line contains , the minutes portion
"""


def timeInWords(H,M):
    minutes = ['zero','one','two','three','four','five',
           'six','seven','eight','nine','ten',
           'eleven','twelve','thirteen','fourteen',
           'fifteen','sixteen','seventeen','eighteen',
           'nineteen','twenty','twenty one', 'twenty two',
           'twenty three','twenty four','twenty five',
           'twenty six','twenty seven','twenty eight',
           'twenty nine', 'thirty']
    hours = ['zero','one','two','three','four','five',
         'six','seven','eight','nine','ten','eleven','twelve']
    return_str = ""
    if M == 0:
        return_str += f"{hours[H]} o' clock"
    elif M == 15:
        return_str += f"quarter past {hours[H]}"
    elif M == 30:
        return_str +=f"half past {hours[H]}"
    elif M == 45:
        if H == 12:
            return_str += f"quarter to {hours[1]}"
        else:
            return_str += f"quarter to {hours[H+1]}"
    elif M > 0 and M < 30:
        return_str += f"{minutes[M]} minutes past {hours[H]}"
    elif M > 30 and M < 60:
        if H == 12:
            return_str += f"{minutes[60-M] } minutes to {hours[1]}"
        else:
            return_str += f"{minutes[60-M] } minutes to {hours[H + 1]}"
    return return_str
if __name__ == "__main__":
    Hour = int(input())
    Min = int(input())
    print(timeInWords(Hour,Min)) 