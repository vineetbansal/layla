from importlib_resources import read_text


def greeting():
    return read_text('layla.data', 'greeting.txt')


def say_greeting():
    print(greeting())
