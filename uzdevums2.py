import langid

# Тексты
texts = ["Šodien ir saulaina diena.", "Today is a sunny day.", "Сегодня солнечный день."]

# Определение языка для каждого текста
languages = {text: langid.classify(text)[0] for text in texts}

# Результат
print(languages)
