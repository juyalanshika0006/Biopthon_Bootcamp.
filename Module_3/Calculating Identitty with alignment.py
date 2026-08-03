from Bio.Align import PairwiseAligner


sequence1 = "MSTPARRK"

sequence2 = "MSTPARKK"

identical=0
for a,b in zip(sequence1, sequence2):
    if a==b:
        identical+=1
    print("Identical residues:", identical)
    Identity_percentage=identical/len(sequence1)*100
    print("Identity%:", Identity_percentage)
