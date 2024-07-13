# Solution for config file management

import re

# in_file = input('Enter the complete Patch of the Config file to read ')

# read_file = open (input_file, 'r')
# read_lines = read_file.readlines()
# print (read_lines) 

file = open('sample_file.txt', 'r')
print(file.read()) 
file.close()

with open('sample_config_file.txt', 'r') as f:
    num_lines = 0 
    for line in f:
        words=line.split()
        num_words=len(words)
        if num_words == 1:
            
            res = {}
            for line in lines:
                (key, value) = line.strip().split('=')
                res[key.strip()] = value.strip()

    print ("Dictionary Created")
    print (res)


