def character_frequencies(x):
  dict_frequencies= {}
  
  for char in x:
    if char in dict_friquencies:
      dict_friquencies[char] += 1
    else:
      dict_friquencies[char] = 1
    return dict_friquencies

def main():
    filename = sys.argv[1]

    with open(filename, "r", encoding="utf-8") as infile:
        text = infile.read()

    frequencies = character_frequencies(text)

    with open("frequencies.txt", "w", encoding="utf-8") as outfile:
        for char in frequencies:
            outfile.write(f"{char},{frequencies[char]}\n")


main()
