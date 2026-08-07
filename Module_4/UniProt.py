import requests

url = "https://rest.uniprot.org/uniprotkb/P38398.json"
response = requests.get(url)

with open(
    "Module_4/BRCA1_Uniprot.json",
    "w"
) as file:

    file.write(response.text)

print("Downloaded successfully!")

data = response.json()

print(data["primaryAccession"])

print(
    data["proteinDescription"]
    ["recommendedName"]
    ["fullName"]
    ["value"]
)

print(
    data["organism"]
    ["scientificName"]
)

print(
    data["genes"][0]
    ["geneName"]
    ["value"]
)

