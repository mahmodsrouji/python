# some information before make the project
# if I want to invert the words 
# I have to use [-1] to Start counting from the end
# example: 
# name = "Mahmoud"
# print(name[8:0:-1])
# but here we have a problem!. we can't count the end word because it's exclusive 
# So, The solution is:
# name = "Mahmoud"
# print(name[8::-1])
# # We have to keep the place where the zero is empty.
# name = "Mahmoud"
# print(name[::-1])
# So, With these spaces "[::-1]", Python understands that it must count from beginning to end.

# The project is: 

sentence = input("Enter a sentence: ").split()
inverted_words = (sentence[::-1])
print(inverted_words)
inverted_sentence = " ".join(inverted_words)
print("Reserved sentence:", inverted_sentence)

# in another way.
def invert_sentence(sentence):
    return ' '.join(reversed(sentence.split()))

# Example usage
input_sentence = input("Enter a sentence: ")
inverted_result = invert_sentence(input_sentence)
print(f"Inverted sentence: {inverted_result}")

