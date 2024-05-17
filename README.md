# ATCSIndProj
Final project for Advanced Topics in Computer Sciences

Project description: I'm interested in and want to study biology/genetics in college, so for this 
project, I explored ways to use Python to solve biological problems (field of bioinformatics).

-------------
DNA is made up of 4 bases: A, T, C, and G.
The first program I developed simply calculates the GC content of a given DNA sequence. Knowing the
GC content of a sequence is incredibly useful since it can reveal a lot of information from DNA
stability to species to protein expression.

I developed some very simple code to make gc_content.py, included in the zip file. 

-------------
The GC content program was not difficult at all, so I also learned about the Boyer-Moore algorithm. It is a 
searching algorithm that finds a small pattern in a larger text. Boyer-Moore takes information from 
character comparisons to skip unnecessary characters that will not match through two main methods: the bad 
character rule and the good suffix rule. 

Bad character rule: skips alignments until a mismatched character turns into a match or the pattern moves
all the way over the mismatch. 
* Make mismatches matches

Good suffix rule: given a small section of a matching chunk, skips until there are no mismatches between
the pattern and text or when the pattern moves all the way over the small section.
* Keeps matches

In Boyer-Moore, alignments go from left to right while character comparisons go from right to left.

Sources:
