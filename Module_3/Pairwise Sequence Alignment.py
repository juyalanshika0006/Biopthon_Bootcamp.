
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

print( "-" * 50)


#________________________________________________________________________________________________________

aligner=PairwiseAligner()
aligner.mode = "global"
aligner.match_score=1
aligner.mismatch_score=-1
alignment=aligner.align(
    sequence1,
    sequence2
)[0]
print(alignment)
print("score:", alignment.score)

print( "-" * 50)

#________________________________________________________________________________________________________
aligner=PairwiseAligner()
aligner.mode = "local"
aligner.match_score=1
aligner.mismatch_score=-1
alignment=aligner.align(
    sequence1,
    sequence2
)[0]
print(alignment)
print("score:", alignment.score)

print( "-" * 50)


