def encrypt(msg: str, key: int) -> str:
    res = []
    for alpha in msg:
        if alpha.islower():
            a = (ord(alpha) - ord('a') + key) % 26
            res.append(chr(a + ord('a')))
        elif alpha.isupper():
            a = (ord(alpha) - ord('A') + key) % 26
            res.append(chr(a + ord('A')))
        else:
            res.append(alpha)
        
    return ''.join(res)

def decrypt(code: str, key: int) -> str:
    res = []
    for alpha in code:
        if alpha.islower():
            a = (ord(alpha) - ord('a') - key) % 26
            res.append(chr(a + ord('a')))
        elif alpha.isupper():
            a = (ord(alpha) - ord('A') - key) % 26
            res.append(chr(a + ord('A')))
        else:
            res.append(alpha)

    return ''.join(res)

code = encrypt('I have a pen, and I went to Zoo yesterday.', 2)
print(code)
print(decrypt(code, 2))