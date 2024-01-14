# This program finds the top 30 most common words from the output text file from question one and store into a new csv file called. 

import csv # to write new csv file

def remove_nonwords(s):
    wordlist = []
    for word in s:
        if word.isalpha() == True:
            wordlist.append(word)
    return wordlist

def count_occ(s):
      
    # process list of works making all the same lowercase, splitting the list and removing non words
    s.lower()
    words = s.split() # split into list of words
    words = remove_nonwords(words)

    counter = {} 
    for word in words:
        if word in counter: # add to counter if item already included
            counter[word] += 1
        else: # create new item if not included
            counter[word] = 1
    return counter

with open('output_data.txt', 'r') as file1: # read text file
    long_string = file1.read() # variable contains all text as single string
    
    all_words = count_occ(long_string)
    top_words = sorted(all_words, key=all_words.get, reverse=True)[:30] # take top 30 words
    
    with open('words_counts.csv', 'w', newline="") as file2: # write top 30 words and counts to .csv file
        for word in top_words:
            file2.write(word + "," + str(all_words[word]))
            file2.write("\n")