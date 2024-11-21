import re

# Ievades teksts
raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

# Teksta tīrīšana
clean_text = re.sub(r'@\w+|http\S+|[^\w\s]', '', raw_text).lower().strip()

# Rezultāts
print(clean_text)
