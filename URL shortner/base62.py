BASE62_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def base62_encode(number):
    if number == 0:
        return BASE62_ALPHABET[0]

    result = ""
    while number > 0:
        result = BASE62_ALPHABET[number % 62] + result
        number //= 62
    return result


def base62_decode(code):
    result = 0
    for char in code:
        result = result * 62 + BASE62_ALPHABET.index(char)
    return result
