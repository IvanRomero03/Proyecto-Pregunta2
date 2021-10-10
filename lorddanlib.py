#Esta es una libreria mia
def is_pow_of(number, root):
    transform = number / root
    if transform == 1:
        return True
    elif transform < 1:
        return False
    else:
        return is_pow_of(transform, root)
def parse_string_to_list(string_to_sort, sequence):

    arr = string_to_sort.strip()
    arrc = arr
    tam_array = len(arr)
    space_place = [tam_array]
    raw_words_arr = []
    final_words_arr = []

    if sequence in arr:
        for curr_pos in range(tam_array):
            if arr[curr_pos] == sequence:
                space_place.append(arr.index(arr[curr_pos], curr_pos, tam_array))
        space_place.sort()
        for palabra_actual in range(len(space_place)):
            trozo = arr[space_place[palabra_actual]:]
            pal = arrc.replace(trozo, "")
            raw_words_arr.append(pal)
        for pal_actual in range(len(raw_words_arr)):
            substr = raw_words_arr[pal_actual].replace(raw_words_arr[pal_actual-1], "").replace(sequence, "").strip()
            final_words_arr.append(substr)
    return final_words_arr
