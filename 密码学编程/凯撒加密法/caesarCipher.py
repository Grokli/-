# Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

import pyperclip

message = 'This is my secret message.'
key = 13
mode = 'encrypt'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''
message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        translated = translated + LETTERS[num]

    else:
        translated = translated + symbol

print(translated)

# 复制加密或解密字符串到剪贴板
pyperclip.copy(translated)