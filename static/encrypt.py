char = 'qwertyuiopasdfghjklzxcvbnm'
enc_str = #("encrypt string go here").lower()

enc = ''
dec = ''
def encrypt():
    global enc
    for i in enc_str:
        if i in char:
            check = ord(i) + shift
            if check > 97 and check < 122:
                new = check
            if check > 122:
                new = check -26
            new2 = chr(new)
            enc = enc + new2
        elif i not in char:
            enc = enc + i
    return enc 

def decrypt():
    pass

print(decrypt())