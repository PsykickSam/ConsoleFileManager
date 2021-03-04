import os
import msvcrt
import lib.memory as memory
from lib.memory import MEMORY_INF

cin_memory_data = memory.read_from_memory(MEMORY_INF["CIN"])
cin_memory_data_len = len(cin_memory_data)
current_mem_ptr = cin_memory_data_len

def input(initial, start=True, memo="", not_input_char=False):
    global current_mem_ptr

    cin_memory_data = memory.read_from_memory(MEMORY_INF["CIN"])
    prev_memo = ""
    if start:
        print(initial, memo, end='', flush=True)
        start = False

    input_char = msvcrt.getch()
    if input_char != b'\xe0' and not_input_char: 
        if len(cin_memory_data) > 0 and input_char == b'H': # up
            if current_mem_ptr > 0:
                current_mem_ptr -= 1
                prev_memo = memo
                memo = cin_memory_data[current_mem_ptr]
        elif len(cin_memory_data) > 0 and input_char == b'P': # down
            if current_mem_ptr < cin_memory_data_len - 1:
                current_mem_ptr += 1
                prev_memo = memo
                memo = cin_memory_data[current_mem_ptr]
        else:
            return input(initial, start, memo, False)
    elif input_char == b'\xe0' and not not_input_char:
        return input(initial, start, memo, True)
    elif input_char == b'\x08':
        temp = memo
        if len(memo[:-1]) >= 0:
            memo = temp[:-1]
            print("\b", end=' ')
    elif input_char == b'\x03':
        print()
        return False # To break for CTRL + C is pressed
    elif input_char == b'\r':
        if memo != '':
            memory.save_to_memory(memo, MEMORY_INF["CIN"])

        print()
        return memo
    else:
        memo += input_char.decode("utf-8")
        
    print(end='\r')
    # To remove the extra char from prev or next data [Up/Down Fix] at 'end'
    print(initial, memo, end=' ' * len(prev_memo) + '\b' * len(prev_memo), flush=True)
    return input(initial, start, memo, False)