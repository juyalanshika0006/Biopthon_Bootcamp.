from Bio.Seq import Seq
rna = Seq("AUGGCC")
protein = rna.translate()
print("RNA :", rna)
print("Protein :", protein)