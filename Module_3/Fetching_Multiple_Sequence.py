from Bio import Entrez

Entrez.email = "juyalanshika6@gmail.com"

ids = [
    "2752784870",
"2716733736",
"3362004944"
    
]

batch_size = 100

with open("tp53_sequences.fasta", "w") as file:

    for start in range(0, len(ids), batch_size):

        batch_ids = ids[start:start + batch_size]

        print(f"Fetching sequences {start + 1} to {start + len(batch_ids)}...")

        fetch_handle = Entrez.efetch(
            db="Nucleotide",
            id=batch_ids,
            rettype="fasta",
            retmode="text"
        )

        fasta_data = fetch_handle.read()

        fetch_handle.close()

        file.write(fasta_data)

print("Sequences saved successfully!")