from transformers import pipeline

# Текст
article = """
Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām.
Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm.
"""

# Инициализация модели для резюмирования
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Создание резюме с увеличением max_length
summary = summarizer(article, max_length=100, min_length=20, do_sample=False)

# Обработка вывода для устранения лишних символов
summary_text = summary[0]['summary_text'].strip()

# Вывод резюме
print(summary_text)
