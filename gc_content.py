# #!/usr/bin/python
"""
gc_content.py
This program computes the GC content of a given DNA sequence.
"""

__author__ = "Kamryn Chan"
__version__ = "2024-05-16"

dna = 'acgctcgcgcggcgatagctgatcgatcggcgcgctttttttttaaaag' # get sequence
c = dna.count('c') # count C's in sequence
g = dna.count('g') # count G's in sequence
dna_length = len(dna) # get length of sequence
gc_percent = (c + g) * 100.0 / dna_length # compute GC percentage
print('Expected result: 26/49 = 53.06%')
print('GC%: ' + (str(gc_percent))) # print GC% to screen