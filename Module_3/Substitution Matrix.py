from Bio.Align import PairwiseAligner
from Bio.Align import substitution_matrices


sequence1 = "MKTAYIAKQRQISFVKSHFSRQ"

sequence2 = "MKTAYIAKQRQISFVKSHFTRQ"




aligner = PairwiseAligner()




aligner.mode = "global"




matrix = substitution_matrices.load(
    "BLOSUM62"
)




aligner.substitution_matrix = matrix




aligner.open_gap_score = -10

aligner.extend_gap_score = -0.5


alignment = aligner.align(
    sequence1,
    sequence2
)[0]


print(alignment)

print(
    "Score:",
    alignment.score
)
