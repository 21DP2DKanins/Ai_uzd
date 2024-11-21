import re

# Teksti
text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

# Teksta tīrīšana un vārdu sadalīšana
set1 = set(re.findall(r'\b\w+\b', text1.lower()))
set2 = set(re.findall(r'\b\w+\b', text2.lower()))

# Sakritību aprēķins
common_words = set1 & set2
similarity = len(common_words) / len(set1 | set2) * 100

# Rezultāts
print(f"Kopējie vārdi: {common_words}")
print(f"Sakritības līmenis: {similarity:.2f}%")
