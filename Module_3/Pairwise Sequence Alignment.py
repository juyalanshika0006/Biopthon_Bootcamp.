
from Bio.Align import PairwiseAligner


sequence1 = "MSTPARRK"

sequence2 = "MSTPARKK"


aligner = PairwiseAligner()


alignments = aligner.align(
    sequence1,
    sequence2
)


print(
    alignments[0]
)
print(alignments.score)