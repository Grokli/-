# Transposition Cipher Decryption
# http://inventwithpython.com/hacking (BSD Licensed)

import math, pyperclip

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)
    print(plaintext + '|')
    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    # 向上取整，获得解密列数
    numOfColumns = math.ceil(len(message) / key)
    # 获得解密行数
    numOfRows = key
    # 获得要涂黑的格子数，在最后一列最下面
    numOfShadedBoxes = numOfColumns * numOfRows - len(message)

    plaintext = [''] * numOfColumns
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1

        # 如果指针到了解密矩阵最后一列或者到了涂黑格子那一行的前一列，则下移一行
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)

if __name__ == '__main__':
    main()