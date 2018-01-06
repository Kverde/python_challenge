import string

text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

url = 'map'

def decode(source):
    alphabet = string.ascii_lowercase

    def convert(source_char):
        if source_char in alphabet:
            new_ind = (ord(source_char) - ord('a') + 2) % 26
            return alphabet[new_ind]
        else:
            return source_char

    result = map(convert, source)
    result = ''.join(result)

    print(result)

decode(text)
decode(url)