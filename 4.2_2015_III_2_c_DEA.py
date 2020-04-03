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
            if char.islower():
                state = State.LOWER
            elif char.isdigit():
                state = State.DIGIT

        elif state == State.LOWER:
            if char.islower():
                state = State.LOWER_LOWER
            elif char.isdigit():
                state = State.LOWER_DIGIT
            elif not char.isalnum():
                state = State.LOWER_SPECIAL

        elif state == State.DIGIT:
            if char.islower():
                state = State.DIGIT_LOWER
            elif char.isdigit():
                state = State.DIGIT_DIGIT
            elif not char.isalnum():
                state = State.DIGIT_SPECIAL

        elif state == State.LOWER_LOWER:
            if char.isdigit():
                state = State.END

        elif state == State.LOWER_DIGIT:
            if char.islower():
                state = State.END
            elif char.isdigit():
                state = State.END
            elif not char.isalnum():
                state = State.END

        elif state == State.LOWER_SPECIAL:
            if char.isdigit():
                state = State.END

        elif state == State.DIGIT_LOWER:
            if char.islower():
                state = State.END
            elif char.isdigit():
                state = State.END
            elif not char.isalnum():
                state = State.END

        elif state == State.DIGIT_DIGIT:
            if char.islower():
                state = State.END

        elif state == State.DIGIT_SPECIAL:
            if char.islower():
                state = State.END

    if state == State.END:
        return True
    else:
        return False


print(passwortTesten('2#c'))
