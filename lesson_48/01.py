from langdetect import detect
from langdetect import detect_langs

string_1 = 'Ćwiczenia doskonalące umiejętność rozumienia ze słuchu'
string_2 = 'Der Streit um das Klimaschutzgesetz schwelt weiter und hat Bundesverkehrsminister Volker Wissing zu einer dramatischen Warnung veranlasst: Ohne baldige Einigung seien bundesweite Auto-Fahrverbote an den Wochenenden die letzte Lösung.'
string_3 = 'Schon früh hat der sgv vor den finanziellen Folgen einer 13. AHV-Rente gewarnt. Die Finanzierungsvorschläge des Bundesrates, die eine Anhebung der Lohnprozente vorsahen, werden vom Verband als inakzeptabel bezeichnet. Der sgv spricht sich stattdessen für ein ausgewogenes Gesamtpaket aus, das eine moderate Erhöhung des Rentenalters sowie eine leichte Anhebung der Mehrwertsteuersätze beinhaltet'
string_4 = 'Дом стоит на земле.'


print(detect(string_1))
print(detect(string_2))
print(detect(string_3))
print(detect(string_4))

print(detect_langs(string_1))
print(detect_langs(string_2))
print(detect_langs(string_3))
print(detect_langs(string_4))

# IP.v4   4B ->  32 bit  0.0.0.0 -> 256.256.256.256 (ff.ff.ff.ff)
# IP.v6  16B -> 128 bit
