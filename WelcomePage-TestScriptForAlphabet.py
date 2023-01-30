# -*- coding: utf-8 -*-
rune = ["ᚠ", "ᚢ", "ᚦ", "ᚩ", "ᚱ", "ᚳ", "ᚷ", "ᚹ", "ᚻ", "ᚾ", "ᛁ", "ᛄ", "ᛇ", "ᛈ", "ᛉ", "ᛋ", "ᛏ", "ᛒ", "ᛖ", "ᛗ", "ᛚ", "ᛝ", "ᛟ", "ᛞ", "ᚪ", "ᚫ", "ᚣ", "ᛡ", "ᛠ"]
letter = ["F", "V", "TH", "O", "R", "C", "G", "W", "H", "N", "I", "J", "EO", "P", "X", "S", "T", "B", "E", "M", "L", "NG", "OE", "D", "A", "AE", "Y", "IA", "EA"]
letterFull = ["F", "V(U)", "TH", "O", "R", "C(K)", "G", "W", "H", "N", "I", "J", "EO", "P", "X", "S(Z)", "T", "B", "E", "M", "L", "NG(ING)", "OE", "D", "A", "AE", "Y", "IA(IO)", "EA"]
decimal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]


def abstractionWarning():
    word = []
    wordFull = []
    for e in i:
        if e in rune:
            word.append(letter[28 - rune.index(e)])
            wordFull.append(letterFull[28-rune.index(e)])
        elif e == "/":
            word.append("\n")
            wordFull.append(" \\n")
        elif e == "-":
            word.append(" ")
            wordFull.append("[]")
        elif e == ".":
            word.append("; ")
            wordFull.append("! ")

    print(("".join(word)[:-1]))
    #print("".join(wordFull))
    
    return ("".join(word))



with open("text.txt", "r", 1, "utf-8") as f:
    fullPhrase = []
    for i in f.readlines():
        i = i.strip()
        print(i)
        fullPhrase.append(abstractionWarning())
    print("\n"*2)
    print("".join(fullPhrase))
