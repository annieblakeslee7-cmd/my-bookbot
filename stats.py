def get_word_count(text):
    words = len(text.split())
    return (f"Found {words} total words")

def get_char_count(text) -> dict[str, int]:
    chars = text.lower()
    return {char: chars.count(char) for char in set(chars)}

def sort_on(char_count: tuple[str, int]) -> int:
    return char_count[1]

def chars_dict_to_sorted_list(char_count: dict[str, int]) -> list[tuple[str, int]]:
    new_list = []
    for char, count in char_count.items():
        new_list.append((char, count))
    return sorted(new_list, key=sort_on, reverse=True)