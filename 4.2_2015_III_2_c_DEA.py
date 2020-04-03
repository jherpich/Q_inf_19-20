from enum import Enum


class State(Enum):
    START = 0
    LOWER = 1
    LOWER_LOWER = 2
    LOWER_DIGIT = 3
    LOWER_SPECIAL = 4
    DIGIT = 5
    DIGIT_LOWER = 6
    DIGIT_DIGIT = 7
    DIGIT_SPECIAL = 8
    END = 9


def passwortTesten(eingabe):
    state = State.START
    if len(eingabe) != 3 and not isinstance(eingabe, str):
        return False
    for char in eingabe:
        if state == State.START:
            if ord(char) in range(97, 123):
                state = State.LOWER
            elif ord(char) in range(48, 58):
                state = State.DIGIT

        elif state == State.LOWER:
            if ord(char) in range(97, 123):
                state = State.LOWER_LOWER
            elif ord(char) in range(48, 58):
                state = State.LOWER_DIGIT
            elif set(r' !"#$%&\'()*+,-./:;<=>?@\[\]\^_`{|}~').intersection(char):
                state = State.LOWER_SPECIAL

        elif state == State.DIGIT:
            if ord(char) in range(97, 123):
                state = State.DIGIT_LOWER
            elif ord(char) in range(48, 58):
                state = State.DIGIT_DIGIT
            elif set(r' !"#$%&\'()*+,-./:;<=>?@\[\]\^_`{|}~').intersection(char):
                state = State.DIGIT_SPECIAL

        elif state == State.LOWER_LOWER:
            if ord(char) in range(48, 58):
                state = State.END

        elif state == State.LOWER_DIGIT:
            if ord(char) in range(97, 123):
                state = State.END
            elif ord(char) in range(48, 58):
                state = State.END
            elif set(r' !"#$%&\'()*+,-./:;<=>?@\[\]\^_`{|}~').intersection(char):
                state = State.END

        elif state == State.LOWER_SPECIAL:
            if ord(char) in range(48, 58):
                state = State.END

        elif state == State.DIGIT_LOWER:
            if ord(char) in range(97, 123):
                state = State.END
            elif ord(char) in range(48, 58):
                state = State.END
            elif set(r' !"#$%&\'()*+,-./:;<=>?@\[\]\^_`{|}~').intersection(char):
                state = State.END

        elif state == State.DIGIT_DIGIT:
            if ord(char) in range(97, 123):
                state = State.END

        elif state == State.DIGIT_SPECIAL:
            if ord(char) in range(97, 123):
                state = State.END

    if state == State.END:
        return True
    else:
        return False


print(passwortTesten('2~q'))
