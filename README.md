# Readers-Writers-Problem
A synchronisation problem where we can read and write into a data Structure with consistency in data.  
**About:**  
    Here we have two programs Assn5-rw-cs20btech11018.cpp,Assn5-frw-cs20btech11018.cpp respectively 
    simulating normal reader-writer(here writer may starve),fair reader-writer synchronisation solutions,
    They take input from the same file called inp-params.txt output there log into RW_log.txt,FRW_log.txt
    respectively.They also output average waiting time statistics into file called average_time.txt.  

**To Compile:**  
- rw:  
        /usr/bin/g++-11 -std=c++20 -g ./Assn5-rw-cs20btech11018.cpp -o ./Assn5-rw-cs20btech11018 -pthread  
- frw:  
        /usr/bin/g++-11 -std=c++20 -g ./Assn5-frw-cs20btech11018.cpp -o ./Assn5-frw-cs20btech11018 -pthread 
        
**To run:**
- rw:  
        ./Assn5-rw-cs20btech11018
- frw:  
        ./Assn5-frw-cs20btech11018
