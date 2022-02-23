# mypy tipado.py --check-untyped-defs

def is_palindrome(string: str) -> bool:
    string = string.replace(' ', '').lower()  # borro espacios
    return string == string[::-1]

if __name__ == '__main__':
    print(is_palindrome('oto'))