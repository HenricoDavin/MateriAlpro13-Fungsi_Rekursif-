def palindrome_perulangan(input_string):
    input_string = input_string.lower()
    reversed_input_string = input_string[::-1]
    if input_string == reversed_input_string:
        return True
    else:
        return False
    
def palindrome_rekursif(input_string, depan, belakang):
    if  depan == belakang:
            return True
    elif belakang == depan + 1:
        if input_string[depan] == input_string[belakang]:
            return True
        else:
             return False
    else:
        if input_string[depan] == input_string[belakang]:
             return palindrome_rekursif(input_string, depan + 1, belakang - 1)
        else:
             return False

print(palindrome_perulangan('KaSur RuSAk'))
print(palindrome_perulangan('prak alpro'))

kalimat = 'KaSur RuSAk'
print(palindrome_rekursif(kalimat.lower(), 0, len(kalimat)-1))

kalimat = 'prak alpro'
print(palindrome_rekursif(kalimat.lower(), 0, len(kalimat)-1))