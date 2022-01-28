import sys
from pickle import EMPTY_LIST
import string

def xor(str1, str2) -> str:
    result = []
    for i, j in zip(str1, str2):
        result.append(chr(ord(i) ^ ord(j)))
    return ''.join(result)


def get_xor_alpha_string(expected: str, valid_chars: list) -> tuple:
    """ 
    expected: string you wish to encode
    valid_chars: characters that are allowed
    return: (tupple), xored string and the string used to do the operation
    """

    result = ""
    valid_chars_used = ""
    
    for i in expected:
        for valid in valid_chars:
            res = chr(ord(i) ^ ord(valid))
            # print("{} = {} ^ {}\t{}".format(res, i, valid, res in valid_chars))
            if res in valid_chars:
                result += res
                valid_chars_used += valid
                break
    return result, valid_chars_used


def verify(expected: str, result: str, valid_chars_used: str) -> bool:
    return expected == xor(result, valid_chars_used)


def PHP_non_alpha_encoder(expected: str, valid_chars: list) -> str:
    """ Encode an alpha string to non alpha string. 
    
    expected: alpha word to encode. Must not contain non alpha char.
    valid_chars: list non alpha char
    return: (string) non alpha encoded word

    Examples:
    "phpinfo" => ("@"^"0").("["^"3").("@"^"0").("["^"2").("^"^"0").("^"^"8").("_"^"0")
    "phpinfo()" => incorrect output as '(' and ')' are non alpha char
    "sys2" => incorrect output as '2' is a non alpha char
    """

    result, char_used = get_xor_alpha_string(expected, valid_chars)
    isSuccess = verify(expected, result, char_used)
    if not isSuccess:
        return None
    non_alpha_string = ""
    for a, b in zip(result, char_used):
        # in case the valid char is '\', it may cause errors
        if a == "\\" : non_alpha_string += "(\"\\\\\"^"
        else: non_alpha_string += '("{}"^'.format(a)
        if b == "\\" : non_alpha_string += "\\\\\")."
        else: non_alpha_string += "\"{}\").".format(b)
    non_alpha_string = non_alpha_string[:-1]
    return non_alpha_string


# Generating list of non alpha char
global valid_char
valid_chars = [ ]
for item in string.printable:
  if item not in string.ascii_letters:
    valid_chars.append(item)
valid_chars = valid_chars[:len(valid_chars)-3]
valid_chars.remove('\n')

# checking the user input
if len(sys.argv) != 2:
    print("[ERROR] Usage: ./path_to_script <alpha_string_to_encode_in_PHP>")
    sys.exit()

for char in sys.argv[1]:
    if char in valid_chars:
        print("[ERROR] {} is not a non alpha char.".format(char))
        print("[ERROR] Please, only use string that only contains alpha char.")
        sys.exit()

string_to_encode = sys.argv[1]

# encode string to non alpha string for PHP
result = PHP_non_alpha_encoder(string_to_encode, valid_chars)
if result == None:
    print("[ERROR] Could not encode the string with xor. Not enough valid char.")
else:
    print("[SUCCESS] Here is your encoded string :\n")
    print(result)
