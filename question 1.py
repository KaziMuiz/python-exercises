def string_ops(text):
    return text[::-1], text[::2]

# Usage
rev, sec = string_ops("Hello")
print(rev)  # olleH
print(sec)  # Hlo