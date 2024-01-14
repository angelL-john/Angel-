

from transformers import * 
import math 

def remove_nonwords(s):
    "Removes nonwords from list"
    nlist = []
    for word in s:
        if word.isalpha() == True:
            list.append(word)
    return list

def count_occ(lis):
    "returns count of each word or creates a new entry"
    d = {} 
    for number in lis:
        if str(number) in d: # add to counter if entry already included
            d[str(number)] += 1
        else: # create new entry if not already included
            d[str(number)] = 1
    return d

def auto_tokenise(section, tokens):
    "This function goes through the text created in q1 in sections and creates a list of tokens"
    encoded = tokenizer.encode(' '.join(section))
    for j in encoded:
        if j != 101 or j != 102:
            tokens.append(j) # add tokens to list

with open('output_data.txt', 'r') as file: 
    long_string = file.read() 

    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased") 


    long_string.lower() 
    long_string.strip() 
    list_words = long_string.split() 
    list_words = remove_nonwords(list_words)

    # VARIABLES
    list_tokens = [] 
    length = len(list_words) # number of words
    split = 10000 # the number of pieces the text will processed in
    size_chunk = math.ceil(length / split) # length of each chunk of text rounded up

    # PROCESS TEXT
    for i in range(0, split):
        if i * size_chunk + size_chunk < length:
            current_section = list_words[i * size_chunk : i * size_chunk + size_chunk]
        else:
            current_section = list_words[i * size_chunk : length]
        auto_tokenise(current_section, list_tokens)

    all_tokens = count_occ(list_tokens)
    top_tokens = sorted(all_tokens, key=all_tokens.get, reverse=True)[:30]
    
    print("TOP 30 WORDS AND COUNTS")
    for token in top_tokens:
        word = tokenizer.decode(int(token))
        print(word + "  " + str(all_tokens[token])) # print word and its occurence count