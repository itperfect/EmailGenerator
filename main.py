import string
import random
from datetime import datetime

'''
Generating fake emails strings and write them into files
'''


def crop_dups(data: str = None) -> str:
    '''Clear doubled chars in data'''
    result = list(data)
    for ch in ('.', '_', '-'):
        indexes = [pos for pos, char in enumerate(data) if char == ch]
        if len(indexes) > 1:
            del indexes[0]
            for index in indexes:
                result[index] = ''

    return ''.join(ch for ch in result if ch != '')


def string_clear(data: str = None) -> str:

    ''' Check if data starts with disallowed chars '''

    result = True

    if data.startswith(('-', '_', '.')):
        result = False
    return result


def get_clear(data: str = None) -> str:
    ''' Crops disallowed chars from data '''
    result = data
    do_cycle = True

    while do_cycle:
        if string_clear(result):
            do_cycle = False
        else:
            result = result[1:]
    return result


def get_cleared(data: str = None) -> str:
    ''' Clear string from start and from end '''
    result = data
    for _ in range(2):
        result = get_clear(result)
        result = result[::-1]
    return result


def generate_string(min_len: int = None, max_len: int = None, additional_chars: str = None) -> str:
    '''

    :param min_len: minimum lenght of string name
    :param max_len: maximum lenght of string name
    :param additional_chars: string with additional characters to use
    :return: string
    '''
    amount = random.randint(min_len, max_len)
    result = get_cleared(''.join(random.choice(string.ascii_letters + str(additional_chars)) for _ in range(amount)))
    return crop_dups(result)


def generate_fake_email():
    return generate_string(4, 24, '.-_') + '@' + generate_string(4, 10, '.') + '.' + generate_string(2, 3)


if __name__ == '__main__':

    filename = str(datetime.timestamp(datetime.now())).replace('.', '')

    for ext in (10, "asdfadf", 1000, 25000, 50000, 100000):
        if not isinstance(ext, int):
            continue
        t0 = datetime.timestamp(datetime.now())
        with open(filename + '.' + str(ext), "w") as f_name:
            for _ in range(ext):
                email = generate_fake_email()
                f_name.write(email + '\n')
        print("Filename: {} - {} sec".format(f_name.name, datetime.timestamp(datetime.now()) - t0))
