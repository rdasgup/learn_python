# Diagramm über die Häufigkeit von Marry in CA
# V 16.Okt.2022
# Id,Name,Year,Gender,State,Count

import matplotlib.pyplot  as plt
# Variablen
x = [] # x-Werte (Jahre)
y = [] # y-Werte (Anzahl Marry)
Buffer = [6]
name = "Max"
state = "CA"
gender = "M"
max = 2000
min = 1950
count = 0
FileNameMac = "/Users/roni/python/Kursmaterialien/data/names.csv"

# Öffnen der Datei
with open(FileNameMac) as file:

    # Schleife
    n = 0
    for line in file:
        Buffer = line.strip().split(",")
        if Buffer[1] == name and Buffer[4] == state and Buffer[3] == gender and int(Buffer[2]) >= min and int(Buffer[2]) <= max:
            count = count + int (Buffer[5])
            n += 1
            x.append(int(Buffer[2]))
            y.append(int(Buffer[5]))

# Daten ausgeben
print ("Die Bedingung wurde " + str(n) + " mal erfüllt!")
print ("Die Anzahl der Max genannten lautet: " + str(count) + " Personen!")
plt.plot(x,y)
plt.show()
