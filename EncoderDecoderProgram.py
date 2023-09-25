print("Hello, Press (E) to Encrypt and (D) to Decrypt the text: ")
code = {
    'A': 'vg6',
    'B': '%ht',
    'C': 'JYe',
    'D': 'm9z',
    'E': 'k$p',
    'F': 'a#7',
    'G': 'Qs2',
    'H': 'x&8',
    'I': 'o1n',
    'J': 'l5r',
    'K': 'z@3',
    'L': 'u6w',
    'M': 'c4v',
    'N': 'd0q',
    'O': 'f2i',
    'P': 'e#9',
    'Q': 'b7g',
    'R': 'p$x',
    'S': 'h%t',
    'T': 'y@5',
    'U': 'j6m',
    'V': 'n3o',
    'W': 'i9z',
    'X': 'r&l',
    'Y': 'v4s',
    'Z': 'w#x',
    'a': 'gh3',
    'b': '8fu',
    'c': '2wp',
    'd': '9ak',
    'e': '5ty',
    'f': 'v7n',
    'g': 'e$z',
    'h': 'u8q',
    'i': 'l%1',
    'j': '4i@',
    'k': '6xb',
    'l': 'q#o',
    'm': 'p9c',
    'n': 'm4r',
    'o': '7fd',
    'p': 'a3s',
    'q': 'c8j',
    'r': 'z5e',
    's': 'x#g',
    't': 'o2v',
    'u': 'n&h',
    'v': 'k$0',
    'w': 'w6y',
    'x': 'b1u',
    'y': 'i4t',
    'z': 'd@2'
}
reverse_code = {
    'vg6': 'A',
    '%ht': 'B',
    'JYe': 'C',
    'm9z': 'D',
    'k$p': 'E',
    'a#7': 'F',
    'Qs2': 'G',
    'x&8': 'H',
    'o1n': 'I',
    'l5r': 'J',
    'z@3': 'K',
    'u6w': 'L',
    'c4v': 'M',
    'd0q': 'N',
    'f2i': 'O',
    'e#9': 'P',
    'b7g': 'Q',
    'p$x': 'R',
    'h%t': 'S',
    'y@5': 'T',
    'j6m': 'U',
    'n3o': 'V',
    'i9z': 'W',
    'r&l': 'X',
    'v4s': 'Y',
    'w#x': 'Z',
    'gh3': 'a',
    '8fu': 'b',
    '2wp': 'c',
    '9ak': 'd',
    '5ty': 'e',
    'v7n': 'f',
    'e$z': 'g',
    'u8q': 'h',
    'l%1': 'i',
    '4i@': 'j',
    '6xb': 'k',
    'q#o': 'l',
    'p9c': 'm',
    'm4r': 'n',
    '7fd': 'o',
    'a3s': 'p',
    'c8j': 'q',
    'z5e': 'r',
    'x#g': 's',
    'o2v': 't',
    'n&h': 'u',
    'k$0': 'v',
    'w6y': 'w',
    'b1u': 'x',
    'i4t': 'y',
    'd@2': 'z'
}
def encoder():
    encodedText = ''
    data = input("Enter your text to encode: ")
    for i in range(0, len(data)):
        if data[i] in code.keys():
            encodedText += code[data[i]]
        else:
            encodedText += data[i]
    print("The Encoded Text is :", encodedText)
def decoder():
    decodedText = ''
    data = input("Enter your text to decode: ")
    i = 0
    while i < len(data):
        if data[i:i+3] in reverse_code.keys():
            decodedText += reverse_code[data[i:i+3]]
            i += 3
        else:
            decodedText += data[i]
            i += 1
    print("The Decoded Text is:", decodedText)
while True:
    choice = input("Enter your choice: ")
    if choice in ["E", "e"]:
       encoder()
    elif choice in ["D", "d"]:
       decoder()        
    else:
       print("Please Enter a valid choice E or D")
    break
