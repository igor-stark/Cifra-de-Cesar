# Caesar Cipher project
import unidecode


def caesar(msg, shift):
    if not msg:
        return ""
    else:
        if msg[0].isalpha():
            if msg[0] == msg[0].lower():
                msg = unidecode.unidecode_expect_ascii(msg)
                y = ord(msg[0]) - 97
                y += shift
                y = y % 26
                y = y + 97
                return chr(y) + caesar(msg[1:], shift)
            else:
                msg = unidecode.unidecode_expect_ascii(msg)
                y = ord(msg[0]) - 65
                y += shift
                y = y % 26
                y = y + 65
                return chr(y) + caesar(msg[1:], shift)
        else:
            return msg[0] + caesar(msg[1:], shift)


def caesar_decrypt(msg, shift):
    if not msg:
        return ""
    else:
        if msg[0].isalpha():
            if msg[0] == msg[0].lower():
                y = ord(msg[0]) - 97
                y -= shift
                y = y % 26
                y = y + 97
                return chr(y) + caesar_decrypt(msg[1:], shift)
            else:
                y = ord(msg[0]) - 65
                y -= shift
                y = y % 26
                y = y + 65
                return chr(y) + caesar_decrypt(msg[1:], shift)
        else:
            return msg[0] + caesar_decrypt(msg[1:], shift)


def pt_lista():
    lista = []
    with open("palavras.txt", "r") as f:
        for line in f:
            line = line.replace("\n", "")
            lista.append(line)
        f.close()
    return lista


def brute_force(msg):
    lista = pt_lista()
    for i in range(26):
        decrypted_msg = caesar_decrypt(msg, i + 1)
        words = decrypted_msg.split(" ")
        for word in words:
            for letter in word:
                if letter.isalnum() is False:
                    words = [word.replace(letter, "") for word in words]
            counter = 0
            for word in words:
                if word.upper() in lista:
                    counter += 1
                if counter > len(words) / 2:
                    return decrypted_msg
