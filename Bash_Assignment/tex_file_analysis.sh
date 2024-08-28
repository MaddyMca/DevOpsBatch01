#!/bin/bash

# check if text file argument is provided
if [[ $# -eq 0 ]]; then
    echo "Please provide a file name."
    exit 1
fi

# Read the file name
file=$1

# Count the lines, words, and characters in the file
number_lines=$(wc -l < "$file")
number_words=$(wc -w < "$file")
number_chars=$(wc -c < "$file")

# Display the counts
echo "Lines: $number_lines"
echo "Words: $number_words"
echo "Characters: $number_chars"