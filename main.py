import pandas

# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {}
for (index, row) in nato_df.iterrows():
    nato_dict.__setitem__(row['letter'], row['code'])

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
code_list = []

for letter in word:
    code_list += [code for key, code in nato_dict.items() if letter.upper() == str(key)]
print(code_list)
