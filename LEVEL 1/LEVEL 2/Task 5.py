def count_words(filename):
    word_count = {}

    with open(filename, "r") as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                word = word.strip(".,!?;:")
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    for word in sorted(word_count):
        print(word, ":", word_count[word])


filename = input("Enter the file name: ")
count_words(filename)
