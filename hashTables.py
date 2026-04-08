import csv as csv
import time

#Brook St Laurent
#COS 226
#HW 5
#Assignment: Hash something out
#Date last edited: 4/7/26
#Version description: 5th and final version of hash map program. Try to decrease
# amount of wasted space caused by what I suspect is the hashMath function being so
# rudimentary. Linked list method is still being used.

#will be used for linked list insertion
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#stores each movie's stats into individual list
class Data:
    def __init__(self, category):
        self.title = category[0]
        self.genre = category[1]
        self.release_date = category[2]
        self.director = category[3]
        self.revenue = float(category[4][1:])
        self.ratings = float(category[5])
        self.duration = int(category[6])
        self.company = category[7]
        self.quote = category[8]


def hashMath(hashData):
    #create variable for prime number to be used
    prime = 23
    key = 0

    #try different math formula that calculates the key differently
    for i in hashData:
        key = key * prime + ord(i) #remember: ord returns the unicode value
    return key

    #old version 2 for loop (inefficient)
    #calculates a new key using new prime number and a for loop
    # for i in hashData:
    #     newKey = (prime < 5) + prime + ord(i)
    #     key = newKey
    #     return key
    
    #inserts data into hash table with linear probing method.
    #returns total collisions
def linearProbing(hashTable, index, data):
    #variable for determining if a spot is empty or not
    foundSpot = False

    while foundSpot == False:
        #if spot in table is full, increment collisions counter
        #elif the next index would be outside the length of the table, return to beginning of hash table
        #else, move to next index in hashTable
        if hashTable[index] != None:

            if index + 1 >= len(hashTable):
                index = 0
            else:
                index += 1
        #else, when a spot is empty and data can be added
        else:
            foundSpot = True
            hashTable[index] = data

#calculates and then displays wasted space
def displayWastedSpace(hashTable):
    #capacity for tracking total number of key-value pairs in the hash tables
    wastedSpace = 0
    for i in hashTable:
        if i == None:
            wastedSpace += 1
    return wastedSpace

#calculates and displays total number of collisions for linear probing method
def displayLinearCollisions(hashTable, index):
    foundSpot = False
    collisions = 0
    index = 0
    #while loop to increment collisions counter when a spot that is full is found
    while foundSpot == False:
        if hashTable[index] != None:
            collisions += 1
            index += 1
        else:
            foundSpot = True

    return collisions

#calculates and displays total number of collisions for linked list method
def displayLinkedCollisions(hashTable, index):
    collisions = 0
    curData = hashTable[index]
    #skip first data element since no collision will happen here with linked list method
    curData = curData.next
    #while loop to count collisions
    while curData.next != None:
        collisions += 1
        curData = curData.next

    return collisions


#shell of function that will later be used to implement the linked list
#insertion method
def linkedList(data, index, hashTable):
    #create variable for current data location
    curData = hashTable[index]
    #if/else statement to determine if a spot in the hash table is empty
    #if the spot is full, move elsewhere
    #if the spot is empty, insert the data into that spot
    if hashTable[index] != None:
        while curData.next != None:
            curData = curData.next
        curData.next = data
    else:
        hashTable[index] = data
            
#main function where all other functions are run.
def main():
    file = "MOCK_DATA.csv"
    titleWastedSpace = 0
    quoteWastedSpace = 0

    hashSize = 19391
    hashTableTitle = [None] * hashSize
    hashTableQuote = [None] * hashSize

    #begin counter for tracking time it takes to construct hash table
    start = time.time()

    #open csv file, read data
    with open(file, "r", newline = "", encoding = "utf8") as csvFile:
        #reading data from file and making a data item for each row read
        data = csv.reader(csvFile)
        #skip header row
        next(data)

        for row in data:
            movie = Data(row)
            count = 0

            #get title keys
            titleKeys = hashMath(movie.title)
            #get indexes of the data in the rows for hash table with title keys
            titleIndex = titleKeys % len(hashTableTitle)

            #get quote keys
            quoteKeys = hashMath(movie.quote)
            #get indexes of the data in rows for hash table with quote keys
            quoteIndex = quoteKeys % len(hashTableQuote)

            #insert Data into hash tables using linear probing method
            # linearProbing(hashTableTitle, titleIndex, movie)
            # linearProbing(hashTableQuote, quoteIndex, movie)

            #insert data into hash tables using linked list method
            linkedList(Node(movie), titleIndex, hashTableTitle)
            linkedList(Node(movie), quoteIndex, hashTableQuote)
    
    #hash table construction complete, end timer
    end = time.time()

    #state which version this is and what method was used
    print("Version 5 using linked list insertion method, updated hashMath function\n")

    #calculate wasted space in both hash tables using displayWastedSpace function
    # titleWastedSpace = displayWastedLinearSpace(hashTableTitle)
    # quoteWastedSpace = displayWastedLinearSpace(hashTableQuote)

    #calculate linked list method collisions in both hash tables using displayCollisions function
    hashTitleCollisions = displayLinkedCollisions(hashTableTitle, titleIndex)
    hashQuoteCollisions = displayLinkedCollisions(hashTableQuote, quoteIndex)


    #calculate wasted space in both hash tables for linked list method
    titleWastedSpace = displayWastedSpace(hashTableTitle)
    quoteWastedSpace = displayWastedSpace(hashTableQuote)

    #variable for total run time
    runningTime = end - start

    #state total time it took to construct hash tables
    #use 0.2f for formatting
    print("It took ", runningTime, " time to construct the hash tables\n")

    #state how many collisions happened in both hash tables
    print("There were ", hashTitleCollisions, " collisions in the title hash table\n")
    print("There were ", hashQuoteCollisions, " collisions in the quote hash table\n")

    #state how much wasted space is left in each hash table
    #format to have 0.2f decimal places for formatting
    print("There is ", titleWastedSpace, " wasted space in the title hash table")
    print("There is ", quoteWastedSpace, " wasted space in the quote hash table")


#thing to get the main function running properly
if __name__ == "__main__":
    main()
