from Bio import Phylo



tree = Phylo.read(
    "Module_4/BRCA1_tree.nwk",
    "newick"
)



print("=" * 60)
print("PHYLOGENETIC TREE ANALYSIS")
print("=" * 60)

print(tree)



terminals = tree.get_terminals()

print(
    "\nNumber of sequences:",
    len(terminals)
)



print(
    "\nSequences in tree:"
)

for terminal in terminals:

    print(
        terminal.name
    )



print(
    "\nTree depth:",
    tree.depths()
)



Phylo.draw(tree)