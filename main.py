import pandas

# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {}
for (index, row) in nato_df.iterrows():
    nato_dict.__setitem__(row['letter'], row['code'])

print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

