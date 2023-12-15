def main():
    read_write_file()


def read_write_file():
    file_path = r'C:\Users\Vinayak Ganesh\Projects\PythonProjects\exersises\poem.txt'
    words = {}
    with open(file_path) as file:
        split_words = file.read().lower().split()
        for word in split_words:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    
    max_count = max(words.values())
    most_frequent_words = [word for word,count in words.items() if count == max_count]
    print(f'the most frequent word in the poem is \'{most_frequent_words[0]}\'')

if __name__ == "__main__":
    main()