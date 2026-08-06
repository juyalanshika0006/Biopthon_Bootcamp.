from Bio import SeqIO
from Bio.Restriction import EcoRI
from Bio.Restriction import  BamHI
from Bio.Restriction import HindIII
from Bio.Restriction import NotI
from Bio.Restriction import XhoI

record = SeqIO.read(
    "Module_3/BRCA1_record.fasta",
    "fasta"
)

sequence = record.seq


print("=" * 60)
print("RESTRICTION ENZYME ANALYSIS")
print("=" * 60)


enzymes = [

    EcoRI,

    BamHI,

    HindIII,

    NotI,

    XhoI

]


for enzyme in enzymes:

    sites = enzyme.search(
        sequence
    )

    print(
        "\nEnzyme:",
        enzyme
    )

    print(
        "Recognition Site:",
        enzyme.site
    )

    print(
        "Number of Cuts:",
        len(sites)
    )

    print(
        "Positions:",
        sites
    )