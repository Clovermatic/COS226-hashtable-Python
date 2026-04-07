# COS226-hashtable-Python

Description:
A simple program featuring the implementation of two hash tables, which both derive their key-value pairs from an external csv file called "MOCK_DATA.csv". The first hash table uses the title of the movie from each row of data as the key, while the second table uses the movie quote from each row of data as the key. Both the linear probing hash table method as well as the linked list hash table method will be implemented, and each method will be improved upon at least once. A total of 5 commits will be made to the main hashTables.py file, where each commit features a new update or implementation in order to improve upon the previous version of the program. Results will be logged both with screenshots of the run results from each version, as well as in the commit notes for each of the 5 commits.

Files Overview:
- hashTables.py: The main file where the program will reside. Will have a total of 5 commits, each featuring a different update to the hash tables in order to improve upon the previous version
- hashScreenshots folder: contains screenshots of the data printed in the terminal after running each version
- "MOCK_DATA.csv": the .csv file containing the data that is being stored in the hash tables

Version 1 Report:
The first method, linear probing, has been implemented. The hash tables took approximately 30 seconds to be constructed, which isn't terrible, but also isn't great. Both hash tables also experienced a lot of collisions; I believe that a major cause for this is due to my hashMath function being very rudimentary. I plan to try and improve the hashMath function by making the prime number larger and implementing a for loop in the next version in order to hopefully better optimize the linear probing method.
