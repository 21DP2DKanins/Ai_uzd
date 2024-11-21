from collections import Counter
import re

# Ievades teksts
text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

# Teksta tīrīšana un sadalīšana vārdos
words = re.findall(r'\b\w+\b', text.lower())

# Vārdu biežuma skaitīšana
word_counts = Counter(words)

# Rezultāts
print(word_counts)
