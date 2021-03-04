def array_over_under_load_error(l_bound, u_bound, arr):
    if len(arr) > u_bound:
        print("[OVERLOAD] Input overload!")
        return True
    elif len(arr) < l_bound:
        print("[UNDERLOAD] Input underload!")
        return True
    return False

def char_compare_at_pos_error(char, pos, str):
    if str[pos] != char:
        return True
    return False