import hashlib

zuknackendeDatei = "test.txt"
woerterliste     = "rockyou.txt"

tocrack = set()
wordlist = set()

counttocrack = 0
print("Öffne "+zuknackendeDatei+" Datei...")
tocrackdir = open(zuknackendeDatei, 'r')
for element in tocrackdir:
    element=element.strip('\n')
    tocrack.add(element)
    counttocrack += 1

print("Öffne "+woerterliste+" Datei...")
wordlistdir = open(woerterliste, 'r')
for element in wordlistdir:
    element=element.strip('\n')
    wordlist.add(element)

countcracked = 0
print("Starte..")
for xx in tocrack:
    for xxx in wordlist:
        if hashlib.md5(xxx.encode('utf-8')).hexdigest() == xx:
            print('Password found: '+xx+' -> '+xxx)
            countcracked += 1

print(str(countcracked)+' Passwörter von '+str(counttocrack)+' Gefunden')
