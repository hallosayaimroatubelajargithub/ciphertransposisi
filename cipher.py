def encrypt(text, key):
    encrypted_text = ""
    for i in range(key):
        for j in range(i, len(text), key):
            encrypted_text += text[j]
    return encrypted_text

def decrypt(text, key):
    decrypted_text = [""] * len(text)
    row, col = 0, 0

    for char in text:
        decrypted_text[row] += char
        row += 1
        if row == key or (row == key - 1 and col >= len(text) % key):
            row, col = 0, col + 1

    return "".join(decrypted_text)
