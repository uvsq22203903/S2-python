def chiffrement(char, key):
    return chr(ord(char)+key)

texte ="toto"
cle = 3
chiffrement(texte, cle)