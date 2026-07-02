import sys


def read_frequencies(filepath):
    """
    Read a frequencies file in the format produced by character_frequencies.py.
    Each line is: char,count
    Non-printable characters are stored as escape sequences (e.g. \\n, \\t).
    Returns a dict mapping the actual character to its integer count.
    """
    frequencies = {}
    with open(filepath, "r", encoding="utf-8") as f:
        header = f.readline()  # skip "char,count" header
        for line in f:
            # Remove the trailing newline from the line itself,
            # then split on the LAST comma to handle the comma character as a key.
            line = line.rstrip("\n")
            last_comma = line.rfind(",")
            char_repr = line[:last_comma]
            # Unescape: convert escape sequences like \\n back to the real character.
            # char_repr.encode("raw_unicode_escape").decode("unicode_escape")
            # handles \n, \t, \r, etc. and works also for hebrew characters
            # and other unicode.
            actual_char =  \
                  char_repr.encode("raw_unicode_escape").decode("unicode_escape")

            count = int(line[last_comma + 1:])

            frequencies[actual_char] = count

    return frequencies


frequencies=read_frequence(sys.argv[1])
print(frequencies)
