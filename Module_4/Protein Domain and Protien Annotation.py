import requests


accession = "P38398"



url = (
    "https://rest.uniprot.org/"
    f"uniprotkb/{accession}.json"
)

response = requests.get(url)

response.raise_for_status()

data = response.json()



print("=" * 60)

print("BRCA1 FUNCTIONAL ANNOTATION")

print("=" * 60)

print(
    "Accession:",
    data["primaryAccession"]
)



protein_name = (
    data["proteinDescription"]
    ["recommendedName"]
    ["fullName"]
    ["value"]
)

print(
    "Protein:",
    protein_name
)



print("\nProtein Domains:")

for feature in data["features"]:

    if feature["type"] == "Domain":

        description = feature.get(
            "description",
            "Unknown"
        )

        location = feature[
            "location"
        ]

        print(
            "\nDomain:",
            description
        )

        print(
            "Location:",
            location
        )