#!/bin/bash

# Define the output file
outputFile="summary.txt"

# Start fresh by rewriting the file
> "$outputFile"
echo "You will help me build grpc application"  >> "$outputFile"

# Section 1: Project tree
echo "Project tree:" >> "$outputFile"
echo "###" >> "$outputFile"
tree -a -I '__pycache__' woolyherdz/ | grep -vE '^[0-9]+ directories, [0-9]+ files$' >> "$outputFile"
echo "###" >> "$outputFile"
tree -a -I '__pycache__' tests/ | grep -vE '^[0-9]+ directories, [0-9]+ files$' >> "$outputFile"
echo "###" >> "$outputFile"

# Section 2: List file names and their content
echo "Files and their contents:" >> "$outputFile"
echo "###" >> "$outputFile"
echo "./woolyherdz/proto/woolyherdz.proto" >> "$outputFile"
cat ./woolyherdz/proto/woolyherdz.proto >> "$outputFile"
echo "###" >> "$outputFile"
echo "./woolyherdz/grpc.py" >> "$outputFile"
cat ./woolyherdz/grpc.py >> "$outputFile"
echo "###" >> "$outputFile"
echo "./tests/test_grpc.py" >> "$outputFile"
cat ./tests/test_grpc.py >> "$outputFile"
echo "###" >> "$outputFile"
