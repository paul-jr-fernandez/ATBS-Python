# Chapter 4: Lists - Comma Code
# Author: Paul Jr Fernandez
# Changelog:
# 18 Jan 2018 v1.0: Initial Release

# Function splitList that converts the input list into a comma/and separated string
def splitList(mirrorList):
    sentenceString = '' # Intialize empty string
    listLength = len(mirrorList)
    for i in range(listLength):
        if i == (listLength - 2): # Handle second last list item
            sentenceString += mirrorList[i] + ' and '
        elif i == (listLength - 1): # Handle last list item
            sentenceString += mirrorList[i]
        else: # Handle all other list items
            sentenceString += mirrorList[i] + ', '
    return sentenceString

# Main
inputString = input('Enter the list items of your list(Separate list items by SPACE. To stop press ENTER):\n')
inputList = [ str(x) for x in inputString.split(' ')] # Split input string on basis of spaces and feed into a list
while '' in inputList: # Remove extra spaces provided at input
    inputList.remove('')
print(' The List that has been provided:')
print(inputList)
outputString = splitList(inputList)
print(' The comma coded output string:\n' + outputString)
