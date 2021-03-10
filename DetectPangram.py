import string

def is_pangram(s):
    abecedario = "abdcdefghijklmnopqrstuvwxyz"
    pangram = s.lower()
    for i in abecedario:
        if(pangram.find(i)==-1):
            return False;
    return True
