import sys
dna2rna = {"T":"A", "A":"U", "C":"G", "G":"C"}
sys.stdout.write("".join([dna2rna[dna] for dna in list(sys.stdin.readline().strip())])+"\n")
