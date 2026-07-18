from Bio.Seq import Seq
dna=Seq("AAAATGGCTTTTTAAGGG")
start=dna.find("ATG")
stop=dna.find("TAA")
if start != -1 and stop!=-1:
    orf=dna[start:stop+3]
    print("ORF:", orf)
    print("Protein:",orf.translate())
else:
    print("No ORF founded!!")    