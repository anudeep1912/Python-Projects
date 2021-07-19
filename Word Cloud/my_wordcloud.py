def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being",
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how",
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

    frequencies = dict()

    for word in file_contents.split():
        print(word)
        if word.lower() in uninteresting_words:
            pass
        else:
            if word.isalpha() and word not in frequencies:
                frequencies[word.lower()] = 1
                print(frequencies)
            elif word.isalpha() and word in frequencies:
                frequencies[word.lower()] += 1
                print(frequencies)
            else:
                for letter in word:
                    if letter in punctuations:
                        index = word.index(letter)
                        print(index)
                        new_word = word.replace(letter, '')
                        if new_word not in uninteresting_words:
                            if new_word in frequencies:
                                frequencies[new_word.lower()] += 1
                            else:
                                frequencies[new_word.lower()] = 1
    return frequencies

text = "Hi i am anudeep, And i do coding. i like coding very much. How are you. Doesn't it effect you"
print(calculate_frequencies(text))