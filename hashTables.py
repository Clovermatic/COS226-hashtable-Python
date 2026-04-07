import csv as csv
import time

#Brook St Laurent
#COS 226
#HW 5
#Hash tables, optimization, and analysis
#Date last edited: 4/6/26
#Version description: 1st version of a hash table program where the movie title
# is the key. First focuses on the linear probing method to store the data from the csv file
# into the hash table.

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
    #creates a hash key by multiplying the len of hashData to ord of hashData at 0, then adds prime number
    #prime number reduces chance of collisions
    key = len(hashData) * ord(hashData[0]) + 929
    return key
    
    #inserts data into hash table with linear probing method.
    #returns total collisions
def linearProbing(hashTable, index, data):
    #variable for determining if a spot is empty or not
    foundSpot = False
    #variable to track number of collisions
    collisions = 0

    while foundSpot == False:
        #if spot in table is full, increment collisions counter
        #elif the next index would be outside the length of the table, return to beginning of hash table
        #else, move to next index in hashTable
        if hashTable[index] != None:
            collisions += 1
            if index + 1 >= len(hashTable):
                index = 0
            else:
                index += 1
        #else, when a spot is empty and data can be added
        else:
            foundSpot = True
            hashTable[index] = data
    return collisions

#shell of function that will later be used to implement the linked list
#insertion method
def linkedList(data, index, hashTable):
    pass
            
#main function where all other functions are run.
def main():
    file = "MOCK_DATA.csv"
    titleWastedSpace = 0
    quoteWastedSpace = 0

    hashSize = 20000
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

            #get title keys
            titleKeys = hashMath(movie.title)
            #get indexes of the data in the rows for hash table with title keys
            titleIndex = titleKeys % len(hashTableTitle)

            #get quote keys
            quoteKeys = hashMath(movie.quote)
            #get indexes of the indexes in rows for hash table with quote keys
            quoteIndex = quoteKeys % len(hashTableQuote)

            #insert Data into hash tables
            hashTitleCollisions = linearProbing(hashTableTitle, titleIndex, movie)
            hashQuoteCollisions = linearProbing(hashTableQuote, quoteIndex, movie)

            #calculate wasted space in both hash tables
            titleWastedSpace += hashSize - len(hashTableTitle)
            quoteWastedSpace += hashSize - len(hashTableQuote)
    
    #hash table construction complete, end timer
    end = time.time()

    runningTime = end - start

    #state which version this is and what method was used
    print("Iteration 1 using linear probing insert method\n")

    #state total time it took to construct hash tables
    #use 0.2f for formatting
    print("It took ", runningTime, " time to construct the hash tables\n")

    #state how many collisions happened in both hash tables
    print("There were ", hashTitleCollisions, " collisions in the title hash table\n")
    print("There were ", hashQuoteCollisions, " collisions in the quote hash table\n")

    #state how much wasted space is left in each hash table
    #format to have 0.2f decimal places for formatting
    print("There is ", format(titleWastedSpace, ".2f"), " wasted space in the title hash table")
    print("There is ", format(quoteWastedSpace, ".2f"), " wasted space in the quote hash table")


#thing to get the main function running properly
if __name__ == "__main__":
    main()
    
