'''MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 


s='ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ZERO ONE ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ZERO ONE ZERO ONE ONE ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ZERO ZERO ONE ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ZERO ZERO ONE ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ZERO ZERO ONE ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ZERO ZERO ONE ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ZERO ONE ZERO ONE ONE ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ZERO ONE ZERO ONE ONE ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ZERO ONE ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ZERO ZERO ONE ZERO ONE ONE ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ZERO ZERO ZERO ONE ZERO ONE ONE ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ZERO ZERO ONE ONE ONE ZERO ONE ZERO ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ONE ZERO ONE ZERO ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ZERO ZERO ONE ONE ZERO ZERO ONE ONE ONE ZERO ONE ZERO ZERO ONE ONE ZERO ZERO ZERO ONE ZERO ONE ZERO ZERO ZERO ONE ZERO ZERO ONE ONE ONE ONE ZERO ONE ZERO ZERO ONE ONE ONE ONE ZERO ONE'
a = s.split(' ')
ls = []
for i in a:
    if i == 'ZERO':
        ls.append(0)
    elif i == 'ONE':
        ls.append(1)    
str1 = ''.join(str(e) for e in ls)
print(str1)
def decode_binary_string(s):
    global encoded
    encoded =  ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

decode_binary_string(str1)
# print(chr(int(str1:8], 2)))

import base64

data = base64.b64decode(encoded)
print(data)

def decrypt(message): 
    message += ' '
  
    decipher = '' 
    citext = '' 
    for letter in message: 
  
        if (letter != ' '): 
            i = 0
            citext += letter 
        else: 
            i += 1
            if i == 2 : 
                decipher += ' '
            else: 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                .values()).index(citext)] 
                citext = '' 
  
    return decipher 

data = data.decode("utf-8") 
print(type(data))
result = decrypt(data) 
print(result) '''

raw = '011100000111001001101001011110100110010101110011011100000110010101100011011010010110000101101100011000100111010101100010011000100110110001100101011101000110010101100001'

string = []
for i in raw:
    if i == '0':
        string.append('ZERO ')
    elif i == '1':
        string.append("ONE ")

str1 = ''.join(str(e) for e in string)
print(str1)
f = open('ZERO_ONE','w+')
f.write(f)
f.close()

