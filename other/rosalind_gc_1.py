#!/usr/bin/env python

dna_string = input()
gc_count = 0
for char in dna_string:
    if char in "CG":
        gc_count += 1
gc_content = gc_count / len(dna_string) * 100
print(f"{gc_content:.3f}")
