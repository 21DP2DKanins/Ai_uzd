from textblob import TextBlob

# Teikumi
sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

# Noskaņojuma analīze
for sentence in sentences:
    sentiment = TextBlob(sentence).sentiment.polarity
    mood = "pozitīvs" if sentiment > 0 else "negatīvs" if sentiment < 0 else "neitrāls"
    print(f"Teikums: {sentence} => Noskaņojums: {mood}")
