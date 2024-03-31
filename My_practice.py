def invert_sentence_simple(sentence):
    return ' '.join(reversed(sentence.split()))

# Example usage
input_sentence = input("Enter a sentence: ")
inverted_result = invert_sentence_simple(input_sentence)
print(f"Inverted sentence: {inverted_result}")

