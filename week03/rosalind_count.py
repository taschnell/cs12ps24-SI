#!/usr/bin/env python

dna_string = input()

A_count = dna_string.count("A")

C_count = dna_string.count("C")

G_count = dna_string.count("G")

T_count = dna_string.count("T")


print(
    f"A's:\t{A_count}\nB's:\t{C_count}\nC's:\t{G_count}\nB's:\t{T_count}\nLength:\t{len(dna_string)}"
)
