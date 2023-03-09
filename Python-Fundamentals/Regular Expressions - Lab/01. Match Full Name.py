import re
text_input = input()
#\b at the beginning and the end makes sure this is the boundary of the word and names like PEter Smith does'n match as Eter Smith.
#[A-Z] we start with exactly 1 uppercase letter
#[a-z]+ we receive at least 1 lowercase letter
#\s we receive exactly 1 space
#[A-Z] we start with exactly 1 uppercase letter
#[a-z]+ we receive at least 1 lowercase letter
pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'
print(" ".join(re.findall(pattern, text_input)))
