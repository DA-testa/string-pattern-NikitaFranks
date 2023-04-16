def read_input():
    input_type = input().lower()

    if "i" in input_type:
        pattern = input().strip()
        text = input().strip()
    elif "f" in input_type:
        while True:
            try:
                file_name = "tests/" + input().strip()
                with open(file_name, "r", encoding="utf-8") as f:
                    pattern = f.readline().strip()
                    text = f.readline().strip()
                break
            except FileNotFoundError:
                print("File not found")
    else:
        pattern = ""
        text = ""

    return pattern, text
    
def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p, t = len(pattern), len(text)
    base = 101
    pattern_hash = sum(ord(pattern[i]) * pow(base, i) for i in range(p))
    text_hash = sum(ord(text[i]) * pow(base, i) for i in range(p))
    index_list = []

    for i in range(t - p + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+p]:
                index_list.append(i)

        if i < t - p:
            text_hash = (text_hash - ord(text[i]) * pow(base, 0)) // base + ord(text[i+p]) * pow(base, p-1)

    return index_list

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

