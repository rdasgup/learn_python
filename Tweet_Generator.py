# Tweet_Generator
# V. 14.Oct.2022

# random importieren
import random

# Tweet-Bausteine definieren
Part1 = ["Putin, ", "Hillary, ", "Obama, ", "Fake News, "]
Part2 = ["no talent ", "on the way down ", "realy poor numbers "]
Part3 = ["got destroyed by my ratings ", "rigged the election", "had a much smaler crowd "]
Part4 = ["So sad ", "Appologize ", "So true ", "Media won`t report "]

# Liste von der Liste erstellen
best_words = [Part1, Part2, Part3, Part4]

# Generator
sentence = []

for part in best_words:
    r = random.randint(0, len(part) - 1)
    sentence.append(part[r])

# Ausgabe des Satzes
print(sentence)
print(" ".join(sentence))

