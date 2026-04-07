# COS226-hashtable-Python

Description:
A simple program featuring the implementation of two hash tables, which both derive their key-value pairs from an external csv file called "MOCK_DATA.csv". The first hash table uses the title of the movie from each row of data as the key, while the second table uses the movie quote from each row of data as the key. Both the linear probing hash table method as well as the linked list hash table method will be implemented, and each method will be improved upon at least once. A total of 5 commits will be made to the main hashTables.py file, where each commit features a new update or implementation in order to improve upon the previous version of the program. Results will be logged both with screenshots of the run results from each version, as well as in the commit notes for each of the 5 commits.

Files Overview:
- hashTables.py: The main file where the program will reside. Will have a total of 5 commits, each featuring a different update to the hash tables in order to improve upon the previous version
- hashScreenshots folder: contains screenshots of the data printed in the terminal after running each version
- "MOCK_DATA.csv": the .csv file containing the data that is being stored in the hash tables

Version 1 Report:
The first method, linear probing, has been implemented. The hash tables took approximately 30 seconds to be constructed, which isn't terrible, but also isn't great. Both hash tables also experienced a lot of collisions; I believe that a major cause for this is due to my hashMath function being very rudimentary. I plan to try and improve the hashMath function by making the prime number larger and implementing a for loop in the next version in order to hopefully better optimize the linear probing method.

Version 2 Report:
In this 2nd version I changed the hashMath function to use a for loop instead, with the hopes that the loop would improve efficiency and allow the program to take less time to run. However, I was proven wrong because the hash table construction time increased by about 8 seconds. However, with the hopes of trying to improve the runtime again after this discovery, I edited the size variable in the main function to be a prime number. Because of the nature of hash tables and prime numbers, this somehow caused the run time to go down by about 3 seconds, meaning this final iteration of version 2 takes about 35 seconds to construct the hash tables. However, there were also more collisions in this version, which I presume also has something to do with the for loop in the hashMath function. There is also still no wasted space, which I assume means the entirety of the dataset is being entered into the hash tables without any empty spaces remaining.
