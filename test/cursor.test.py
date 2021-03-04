import msvcrt


def windows_get_input(prefix="", underscores=20, blank_char='_'):

    word = ""

    print(prefix + (underscores - len(word)) * blank_char, end='\r', flush=True)
    # Reprint prefix to move cursor
    print(prefix, end="", flush=True)

    while True:
        ch = msvcrt.getch()
        if ch in b'\x08':
            # Remove character if backspace
            word = word[:-1]
        elif ch in b'\r':
            # break if enter pressed
            break
        else:
            if len(word) == underscores:
                continue
            try:
                char = str(ch.decode("utf-8"))
            except:
                continue
            word += str(char)
        # Print `\r` to return to start of line and then print prefix, word and underscores.
        print('\r' + prefix + word + (underscores - len(word)) * blank_char, end='\r', flush=True)
        # Reprint prefix and word to move cursor
        print(prefix + word, end="", flush=True)
    print()
    return word

print(windows_get_input("Name: ", 20, '_'))