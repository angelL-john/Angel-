# This program compares the drug and disease entities extracted by en_core_sci_sm and en_ner_bc5cdr_md

import spacy
import scispacy
import math

def remove_nonwords(s):
    "Removes nonwords from list s"
    new_list = []
    for word in s:
        if word.isalpha() == True:
            new_list.append(word)
    return new_list

def extract(temp, l):
    "Extracts drug and disease entities and adds to list l"
    for i in temp.ents:
        if i not in l: # don't add the same word twice
            l.append(i)

model1 = spacy.load("en_core_sci_sm")
model2 = spacy.load("en_ner_bc5cdr_md")

word_list_1 = [] # for entities extracted with en_core_sci_sm
word_list_2 = [] # for entities extracted with en_ner_bc5cdr_md

with open('output_data.txt', 'r') as file:
    long_string = file.read()

    # prepare text for processing
    long_string.lower() 
    long_string.strip() 
    list_words = long_string.split() 
    list_words = remove_nonwords(list_words)

   
    length = len(list_words) 
    split = 1000
    size_chunk = math.ceil(length / split) # length of each chunk of text rounded up

    # process text
    for i in range(0, split): # split the text into processable chunks
      
      if i * size_chunk + size_chunk < length:
        current_section = list_words[i * size_chunk : i * size_chunk + size_chunk]
      else:
        current_section = list_words[i * size_chunk : length]
        
      temp = model1(' '.join(current_section)) # initially use en_core_sci_sm
      extract(temp, word_list_1)

      temp = model2(' '.join(current_section))  # now use en_ner_bc5cdr_md
      extract(temp, word_list_2)

print("en_core_sci_sm extracted " + str(len(word_list_1)) + " words")
print("en_ner_bc5cdr_md extracted " + str(len(word_list_2)) + " words")