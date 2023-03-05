def greater(a,b):
    return a > b

def less(a,b):
    return a < b

def bubbleSort(aList, op):
    for passnum in range(len(aList)-1 ,0 ,-1):
        for i in range(passnum):
            if op(aList[i], aList[i+1]):
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp
    return aList

#aList = ['a', 'aa', 'aaaaa', 'aaa', 'aaaa']
#print("Original list:" + str(aList))
#print("Sorted list Increasing:" + str(bubbleSort(aList, greater)))
#print("Sorted list Decreasing:" + str(bubbleSort(aList, less)))

def doYourHomework():
    print('Do your homework!!!')

def discordYourBuddy():
    print('Discord your buddy!!!')

import time

def reminderAfterNSeconds(n, callback):
    time.sleep(n)
    callback()

reminderAfterNSeconds(4, discordYourBuddy)
reminderAfterNSeconds(5, doYourHomework)