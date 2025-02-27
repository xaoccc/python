import codecs

# Your original text
input_file = r'C:\Users\mo3ak\Downloads\Breakaway - Abgerissen (2018) - Cheten-Release.srt'

with codecs.open(input_file, "r", encoding="latin1") as f:
    corrupted_text = f.read()

# Decode from Windows-1252 and re-encode to UTF-8
fixed_text = corrupted_text.encode("latin1").decode("windows-1251")

print(fixed_text)