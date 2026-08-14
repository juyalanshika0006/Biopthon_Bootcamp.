from Bio import Phylo
import matplotlib.pyplot as plt

tree = Phylo.read(
    "Module_4/BRCA1_tree.nwk",
    "newick"
)


print("=" * 60)
print("PHYLOGENETIC TREE ANALYSIS")
print("=" * 60)


print("\nTree:")
print(tree)


# Get terminal nodes
terminals = tree.get_terminals()


print(
    "\nNumber of sequences:",
    len(terminals)
)


# Print sequence names
print("\nSequences in tree:")

for terminal in terminals:

    print(terminal.name)


# Tree depth
print(
    "\nTree depth:",
    tree.depths()
)


# Branch lengths
print("\nBranch Lengths:")

for terminal in terminals:

    print(
        terminal.name,
        "→",
        terminal.branch_length
    )


# Internal nodes
print("\nInternal Nodes:")

for clade in tree.get_nonterminals():

    print(
        "Name:",
        clade.name,
        "| Branch Length:",
        clade.branch_length
    )


# Total branch length
print(
    "\nTotal branch length:",
    tree.total_branch_length()
)


# Find sequences
human = tree.find_any(
    name="Human_BRCA1"
)

chimp = tree.find_any(
    name="Chimpanzee_BRCA1"
)

mouse = tree.find_any(
    name="Mouse_Brca1"
)

rat = tree.find_any(
    name="Rat_Brca1"
)

dog = tree.find_any(
    name="Dog_BRCA1"
)


# Evolutionary distances
print("\nEvolutionary distances:")

print(
    "Human - Chimpanzee:",
    tree.distance(human, chimp)
)

print(
    "Mouse - Rat:",
    tree.distance(mouse, rat)
)

print(
    "Human - Mouse:",
    tree.distance(human, mouse)
)

print("\nClosest sequence pairs:")

for clade in tree.get_nonterminals():

    terminals = clade.get_terminals()

    if len(terminals) == 2:

        print(
            terminals[0].name,
            "<->",
            terminals[1].name
        )

# Draw the tree
Phylo.draw(
    tree,
    do_show=False
)

plt.savefig(
    "Module_4/BRCA1_phylogenetic_tree.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()